import streamlit as st

def main():
    # Set the page configuration (optional)
    st.set_page_config(page_title="Balance Buddy", page_icon="⚖️")

    # Page title (Balance Buddy)
    st.title("Balance Buddy")

    # Logo (using HTML and CSS)
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <div style="font-size: 50px; font-weight: bold; color: #4A90E2;">
                Balance Buddy
            </div>
            <p style="font-size: 24px; color: #4A90E2;">Achieve harmony in health and work — Balance Buddy helps you take control of your life!</p>
        </div>
        <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
            <div style="width: 70px; height: 15px; background-color: #4A90E2; margin-bottom: 10px; border-radius: 5px;"></div>
            <div style="width: 90px; height: 15px; background-color: #4A90E2; margin-bottom: 10px; border-radius: 5px;"></div>
            <div style="width: 110px; height: 15px; background-color: #4A90E2; margin-bottom: 10px; border-radius: 5px;"></div>
        </div>
        """, unsafe_allow_html=True
    )

    # "Get Started" button
    if st.button('Get Started'):
        st.write("Welcome to Balance Buddy! Let’s get started on your journey to better health and work-life balance.")
        # Add your next step here (e.g., navigate to another page or show more content)

if __name__ == "__main__":
    main()



