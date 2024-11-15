import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Define the main structure of the app
def main():
    st.title("Balance Buddy")
    st.sidebar.header("User Preferences")

    # Personalize the app introduction
    st.write("Welcome to Balance Buddy, your AI-powered scheduling assistant!")
    st.write("This app helps you balance your time between work, health, and personal life by creating a flexible yet structured schedule that adapts in real-time.")

    # User Input Section for Tasks
    st.header("Step 1: Enter Your Commitments")

    # Sample entries for commitments
    # Non-flexible tasks like work and classes
    non_flexible = st.sidebar.text_area("Non-flexible tasks (e.g., 'Work: 9 AM - 5 PM', 'Class: 11 AM - 12:30 PM')")
    
    # Flexible tasks like gym or homework
    flexible = st.sidebar.text_area("Flexible tasks (e.g., 'Gym: 1-hour, anytime between 5 PM - 8 PM')")

    # Categories of commitments
    st.write("Categories can include:")
    categories = st.multiselect("Select Categories", ["Work", "Health", "Social Life", "Education", "Other"])
    
    st.write("Here's an example of how you could enter your data:")
    st.code("""
    Non-flexible tasks:
    - Work: 9 AM - 5 PM, weekdays
    - Class: 11 AM - 12:30 PM, Tuesday and Thursday
    
    Flexible tasks:
    - Gym: 1 hour, anytime between 5 PM - 8 PM
    - Study: 2 hours, anytime in the evening
    """)

    # Initial Scheduling Based on User Input
    if st.button("Generate Initial Schedule"):
        generate_initial_schedule(non_flexible, flexible, categories)

    # Example Calendar Preview
    st.header("Calendar Preview")
    st.write("Here is a sample weekly schedule:")
    st.write("Monday - Friday: 9 AM - 5 PM: Work, 6 PM: Gym, 7 PM - 9 PM: Study")

    # Placeholder for advanced scheduling with notifications and adjustments
    st.write("Real-time scheduling adjustments will automatically manage tasks based on availability and priority.")

    # Weekly Check-in and Analytics
    st.header("Weekly Check-in")
    st.write("At the end of each week, track your progress here.")

    st.write("Here's an example of feedback and adjustment recommendations based on task completion:")
    st.code("""
    Tasks completed on time: 80%
    Adjustments suggested:
    - Prioritize social activities earlier in the week
    - Schedule 30-minute exercise blocks instead of 1 hour
    """)

    # Educational Section
    st.header("Did You Know?")
    st.write("Balance Buddy shares wellness tips based on your schedule.")
    st.write("For example: 'Getting at least 7 hours of sleep improves focus and reduces stress.'")

    # Future Expansion Placeholder: Integrate with fitness and health data
    st.header("Future Integrations")
    st.write("This app will soon support connections to fitness apps for personalized health insights and activity recommendations.")
    
    # Gamification with Streaks
    st.header("Gamification")
    st.write("Earn points for completing tasks on time and unlock rewards like gym discounts and wellness kits.")

    # Basic Settings
    st.sidebar.header("Settings")
    st.sidebar.write("Adjust app settings such as notification preferences, reminder frequency, and theme color.")
    theme = st.sidebar.selectbox("Theme Color", ["Light Blue", "Light Green", "White"])

# Function to generate a mock initial schedule
def generate_initial_schedule(non_flexible, flexible, categories):
    st.write("Based on your entries, here’s a draft schedule:")
    st.write("Non-flexible tasks:")
    st.write(non_flexible if non_flexible else "No non-flexible tasks entered.")

    st.write("Flexible tasks:")
    st.write(flexible if flexible else "No flexible tasks entered.")

    st.write("Task categories:")
    st.write(", ".join(categories) if categories else "No categories selected.")

    # Sample Schedule Preview
    st.subheader("Sample Schedule")
    sample_schedule = {
        "Monday": ["Work: 9 AM - 5 PM", "Gym: 6 PM", "Study: 7 PM - 9 PM"],
        "Tuesday": ["Work: 9 AM - 5 PM", "Class: 11 AM - 12:30 PM", "Gym: 6 PM"],
        "Wednesday": ["Work: 9 AM - 5 PM", "Gym: 6 PM", "Study: 7 PM - 9 PM"],
        "Thursday": ["Work: 9 AM - 5 PM", "Class: 11 AM - 12:30 PM", "Social activity: 6 PM"],
        "Friday": ["Work: 9 AM - 5 PM", "Gym: 6 PM"],
    }

    st.write(sample_schedule)

    st.success("Initial schedule generated! Check the calendar preview and adjust tasks as needed.")

# Run the app
if __name__ == "__main__":
    main()
