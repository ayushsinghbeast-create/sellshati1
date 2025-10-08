import streamlit as st

def show_dashboard():
    """Displays the main application dashboard and sidebar navigation after registration."""
    
    # Sidebar Navigation
    st.sidebar.title("Sellshati Menu")
    page = st.sidebar.radio(
        "Navigate", 
        ["Dashboard", "Stock", "Bill", "Business Analysis", "About"]
    )

    # Main content area based on sidebar selection
    if page == "Dashboard":
        st.title("Dashboard")
        st.header(f"Welcome, {st.session_state.user_name}!")
        st.write(f"Business: {st.session_state.business_name}")
        st.success("You have successfully registered!")
        st.info("Select an option from the sidebar to continue.")

    elif page == "Stock":
        st.title("Stock Management")
        st.write("Coming Soon...")
        st.info("This feature to manage your inventory will be available soon.")

    elif page == "Bill":
        st.title("Billing")
        st.write("Coming Soon...")
        st.info("This feature for creating and managing bills will be available soon.")

    elif page == "Business Analysis":
        st.title("Business Analysis")
        st.write("Coming Soon...")
        st.info("This feature for analyzing your business performance will be available soon.")

    elif page == "About":
        st.title("About Sellshati")
        st.write("Coming Soon...")
        st.info("Information about the Sellshati application will be available here.")

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
        
        # Form submission button
        submitted = st.form_submit_button("Confirm Register")

        if submitted:
            # Basic validation
            if not name or not email or not business_name or not business_type:
                st.error("Please fill in all the details to register.")
            else:
                # Store user details in the session and set registration flag
                st.session_state.registered = True
                st.session_state.user_name = name
                st.session_state.business_name = business_name
                st.rerun() # Rerun the script to redirect to the dashboard

# --- Main Application Logic ---

# Set page configuration
st.set_page_config(page_title="Sellshati", layout="wide")

# Initialize session state to check if the user is registered
if 'registered' not in st.session_state:
    st.session_state.registered = False

# Conditional rendering based on registration status
if st.session_state.registered:
    show_dashboard()
else:
    show_registration_page()
