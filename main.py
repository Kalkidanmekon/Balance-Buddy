import streamlit as st

# Function for the Welcome Page
def welcome_page():
    # Set the page configuration (optional)
    st.set_page_config(page_title="Balance Buddy", page_icon="⚖️")

    # Page title (Balance Buddy)
    st.title("Balance Buddy")

    # Logo (using HTML and CSS for stacked circles representing balance rocks)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <div style="font-size: 50px; font-weight: bold; color: #4A90E2;">
                Balance Buddy
            </div>
            <p style="font-size: 24px; color: #4A90E2;">Achieve harmony in health and work — Balance Buddy helps you take control of your life!</p>
        </div>
        
        <div style="display: flex; justify-content: center; align-items: center; height: 200px; flex-direction: column;">
            <!-- Three stacked circles to represent balance rocks -->
            <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #4A90E2; margin-bottom: 10px;"></div>
            <div style="width: 60px; height: 60px; border-radius: 50%; background-color: #4A90E2; margin-bottom: 10px;"></div>
            <div style="width: 70px; height: 70px; border-radius: 50%; background-color: #4A90E2;"></div>
        </div>
        """, unsafe_allow_html=True
    )

    # "Get Started" button
    if st.button('Get Started'):
        st.session_state.page = "login"  # Set the current page to 'login'
        st.experimental_rerun()  # Refresh the app to load the new page

# Function for the Login Page
def login_page():
    # Set the page configuration
    st.set_page_config(page_title="Login | Balance Buddy", page_icon="🔑")

    # Page title
    st.title("Login to Balance Buddy")

    # Login Form
    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')
        submit_button = st.form_submit_button(label="Log In")

    # Handle login logic (this is a placeholder, you can add actual validation later)
    if submit_button:
        if username and password:
            st.session_state.page = "dashboard"  # If login is successful, go to dashboard
            st.experimental_rerun()
        else:
            st.error("Please enter both username and password.")

    # Link to the signup page
    if st.button('Don’t have an account? Sign Up'):
        st.session_state.page = "signup"  # Set the page to 'signup'
        st.experimental_rerun()

# Function for the Signup Page
def signup_page():
    # Set the page configuration
    st.set_page_config(page_title="Sign Up | Balance Buddy", page_icon="📝")

    # Page title
    st.title("Sign Up for Balance Buddy")

    # Signup Form
    with st.form(key='signup_form'):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        submit_button = st.form_submit_button(label="Sign Up")

    # Handle signup logic (this is a placeholder, you can add actual validation later)
    if submit_button:
        if password == confirm_password and username and email:
            st.session_state.page = "login"  # After successful signup, go to login page
            st.success("Account created successfully! Please log in.")
            st.experimental_rerun()
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.error("Please fill in all fields.")

    # Link to the login page
    if st.button('Already have an account? Log In'):
        st.session_state.page = "login"  # Set the page to 'login'
        st.experimental_rerun()

# Function for the Dashboard Page (after login)
def dashboard_page():
    # Set the page configuration
    st.set_page_config(page_title="Dashboard | Balance Buddy", page_icon="📊")

    # Page title
    st.title("Welcome to Your Dashboard")

    # Display content for logged-in users
    st.write("This is where the magic happens! Your personalized dashboard for health and work-life balance.")

    # Logout button
    if st.button("Log Out"):
        st.session_state.page = "welcome"  # Return to the welcome page
        st.experimental_rerun()

# Main logic to control which page is shown
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "welcome"  # Default page is the welcome page

    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()
    elif st.session_state.page == "dashboard":
        dashboard_page()

if __name__ == "__main__":
    main()


