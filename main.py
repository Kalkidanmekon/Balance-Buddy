import streamlit as st
import pandas as pd
import datetime

# Function for Smart Calendar
def smart_calendar_page():
    st.title("📅 Smart Calendar")
    st.write("Organize your tasks effectively and achieve balance in your schedule.")

    task_name = st.text_input("Enter Task Name")
    if task_name:
        task_date = st.date_input("Select Task Date", datetime.date.today())
        start_time = st.time_input("Start Time")
        end_time = st.time_input("End Time")
        
        if start_time >= end_time:
            st.error("End time must be later than start time.")
        else:
            st.success(f"Task '{task_name}' scheduled on {task_date} from {start_time} to {end_time}.")
            
        # Placeholder for future integration with dynamic calendar
        st.info("Future updates will include a dynamic drag-and-drop calendar view.")

# Function for Progress Analytics
def progress_page():
    st.title("📊 Progress Tracker")
    st.write("Visualize how you're progressing by following the calendar.")
    
    # Simulated Data
    progress_data = {
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Tasks Completed": [5, 8, 7, 10],
        "Planned Hours": [15, 20, 18, 22],
        "Achieved Hours": [13, 19, 16, 21],
    }
    df = pd.DataFrame(progress_data)
    
    st.subheader("Weekly Progress Overview")
    st.dataframe(df)
    
    # Visualization
    st.line_chart(df.set_index("Week"))

# Function for Resources
def resources_page():
    st.title("📚 Resources")
    st.write("Explore helpful resources to support your productivity and well-being.")
    
    resources = [
        {"Resource": "10 Tips for Better Time Management", "Link": "https://www.example.com/tips"},
        {"Resource": "Healthy Eating on a Budget", "Link": "https://www.example.com/healthy-eating"},
        {"Resource": "Mindfulness for Stress Relief", "Link": "https://www.example.com/mindfulness"},
    ]
    df_resources = pd.DataFrame(resources)
    
    for _, row in df_resources.iterrows():
        st.write(f"- [{row['Resource']}]({row['Link']})")

# Function for Health Tips
def health_tips_page():
    st.title("💡 Health Tips")
    st.write("Stay motivated and healthy with these practical tips.")
    
    health_tips = [
        "Drink at least 8 glasses of water daily.",
        "Take a 10-minute walk after every hour of sitting.",
        "Incorporate at least 30 minutes of physical activity into your day.",
        "Get 7-9 hours of quality sleep each night.",
        "Eat a balanced diet rich in fruits, vegetables, and lean proteins."
    ]
    
    for tip in health_tips:
        st.info(tip)

# Main Function
def main():
    st.sidebar.title("Dashboard Navigation")
    option = st.sidebar.radio("Go to", ["Smart Calendar", "Progress", "Resources", "Health Tips"])
    
    # Routing based on user choice
    if option == "Smart Calendar":
        smart_calendar_page()
    elif option == "Progress":
        progress_page()
    elif option == "Resources":
        resources_page()
    elif option == "Health Tips":
        health_tips_page()

# Entry point
if __name__ == "__main__":
    main()
