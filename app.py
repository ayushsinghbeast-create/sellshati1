import streamlit as st
import pandas as pd

# --- Page Functions ---

def show_stock_page():
    """Displays the page for managing stock."""
    st.title("Stock Management")

    # Form to add a new item to the stock
    with st.expander("Add New Item", expanded=False):
        with st.form("new_stock_item_form", clear_on_submit=True):
            item_name = st.text_input("Item Name")
            quantity = st.number_input("Quantity", min_value=0, step=1)
            purchase_price = st.number_input("Purchase Price (per item)", min_value=0.0, format="%.2f")
            selling_price = st.number_input("Selling Price (per item)", min_value=0.0, format="%.2f")
            
            submitted = st.form_submit_button("Add Item")
            if submitted:
                if not item_name or quantity <= 0 or selling_price <= 0:
                    st.error("Please fill in all fields with valid values.")
                else:
                    # Create a new item dictionary
                    new_item = {
                        "Item Name": item_name,
                        "Quantity": quantity,
                        "Purchase Price": purchase_price,
                        "Selling Price": selling_price
                    }
                    # Add the new item to the stock list in session state
                    st.session_state.stock.append(new_item)
                    st.success(f"'{item_name}' has been added to your stock!")

    st.write("---")

    # Display the current stock
    st.header("Current Stock")
    if not st.session_state.stock:
        st.info("Your stock is empty. Add a new item using the form above.")
    else:
        # Convert list of dictionaries to a pandas DataFrame for better display
        stock_df = pd.DataFrame(st.session_state.stock)
        
        # Reorder columns for better readability
        stock_df = stock_df[["Item Name", "Quantity", "Purchase Price", "Selling Price"]]
        
        st.dataframe(stock_df, use_container_width=True)


def show_coming_soon_page(page_title):
    """A generic placeholder for pages that are not yet built."""
    st.title(page_title)
    st.write("Coming Soon...")
    st.info(f"The {page_title} feature will be available soon.")


def show_dashboard_page():
    """Displays the main application dashboard."""
    st.title("Dashboard")
    st.header(f"Welcome, {st.session_state.user_name}!")
    st.write(f"Business: {st.session_state.business_name}")
    st.success("You have successfully registered!")
    st.info("Select an option from the sidebar to continue.")
    # We will add summary cards and charts here later
    show_coming_soon_page("Dashboard")

# --- Main Application Logic ---

def main_app():
    """Controls the main application flow after registration."""
    st.sidebar.title("Sellshati Menu")
    page = st.sidebar.radio(
        "Navigate", 
        ["Dashboard", "Stock", "Bill", "Business Analysis", "About"]
    )

    if page == "Dashboard":
        show_dashboard_page()
    elif page == "Stock":
        show_stock_page()
    elif page == "Bill":
        show_coming_soon_page("Billing")
    elif page == "Business Analysis":
        show_coming_soon_page("Business Analysis")
    elif page == "About":
        show_coming_soon_page("About Sellshati")

def show_registration_page():
    """Displays the registration form for new users."""
    st.title("Sellshati")
    st.subheader("Register")

    with st.form("registration_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        business_name = st.text_input("Business Name")
        business_type = st.selectbox(
            "Business Type",
            ["", "Retail", "Wholesale", "Manufacturing", "Service", "Other"]
        )
        
        submitted = st.form_submit_button("Confirm Register")

        if submitted:
            if not name or not email or not business_name or not business_type:
                st.error("Please fill in all the details to register.")
            else:
                st.session_state.registered = True
                st.session_state.user_name = name
                st.session_state.business_name = business_name
                st.rerun()

# --- App Initialization ---

st.set_page_config(page_title="Sellshati", layout="wide")

# Initialize session state variables if they don't exist
if 'registered' not in st.session_state:
    st.session_state.registered = False
if 'stock' not in st.session_state:
    st.session_state.stock = [] # This will hold our stock data

# Conditional rendering based on registration status
if st.session_state.registered:
    main_app()
else:
    show_registration_page()
