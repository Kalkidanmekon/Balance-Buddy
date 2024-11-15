import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Initialize session state variables
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "calendar_generated" not in st.session_state:
    st.session_state.calendar_generated = False

# Function to display the welcome page
def welcome_page():
    st.title("Balance Buddy")
    st.subheader("Achieve control over your life by balancing health and work!")
    if st.button("Get Started"):
        st.session_state.page = "smart_calendar"

# Function to add a new task
def add_task():
    task_name = st.text_input("Enter Task Name (e.g., 'Econ', 'Reading')")
    if task_name:
        category = st.selectbox("Category", ["Work", "Self-Care", "Class", "Social Life"])
        flexible = st.radio("Is it flexible?", ["Yes", "No"])

        if flexible == "No":
            start_time = st.time_input("Start Time")
            duration = st.number_input("Duration (hours)", min_value=1, max_value=12)
            recurring = st.radio("Is it recurring?", ["Yes", "No"])
            if recurring == "Yes":
                days = st.multiselect("Select Days for Recurrence", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
            else:
                days = [datetime.now().strftime("%a")]
        else:
            time_of_day = st.radio("Preferred Time of Day", ["Morning", "Afternoon", "Evening"])
            duration = st.number_input("Duration (hours)", min_value=1, max_value=12)
            days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

        deadline = st.date_input("Deadline (if applicable)", value=datetime.today())

        # Add task to session state
        if st.button("Add Task"):
            st.session_state.tasks.append({
                "name": task_name,
                "category": category,
                "flexible": flexible,
                "start_time": start_time if flexible == "No" else None,
                "duration": duration,
                "recurring": recurring if flexible == "No" else None,
                "days": days,
                "time_of_day": time_of_day if flexible == "Yes" else None,
                "deadline": deadline
            })
            st.success("Task added!")

# Function to create a weekly calendar with color-coded tasks
def generate_calendar():
    st.title("This Week's Calendar")

    # Create a DataFrame for the week with time slots
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    time_slots = ["Morning", "Afternoon", "Evening"]
    calendar_df = pd.DataFrame(index=days, columns=time_slots)
    calendar_df = calendar_df.fillna("")  # Initialize empty slots

    # Assign colors based on category or flexibility
    color_map = {
        "Work": "#FF6F61",
        "Self-Care": "#6B5B95",
        "Class": "#88B04B",
        "Social Life": "#F7CAC9",
        "Flexible": "#FFD700",
        "Non-Flexible": "#FF4500"
    }

    # Populate calendar slots with tasks
    for task in st.session_state.tasks:
        for day in task["days"]:
            slot = task["time_of_day"] if task["flexible"] == "Yes" else "Flexible"
            cell_color = color_map[task["category"] if task["flexible"] == "Yes" else "Non-Flexible"]

            if calendar_df.loc[day, slot] == "":  # If slot is empty
                calendar_df.loc[day, slot] = f"{task['name']} ({task['duration']}h)"
            else:
                # Adjust flexible tasks to make room for non-flexible ones if needed
                if task["flexible"] == "No":
                    # Redistribute the flexible tasks if a conflict occurs
                    other_slots = [s for s in time_slots if calendar_df.loc[day, s] == ""]
                    if other_slots:
                        new_slot = other_slots[0]
                        calendar_df.loc[day, new_slot] = calendar_df.loc[day, slot]
                        calendar_df.loc[day, slot] = f"{task['name']} ({task['duration']}h)"
                    else:
                        calendar_df.loc[day, slot] += f", {task['name']} ({task['duration']}h)"

    # Display the calendar with color-coded cells
    for day in days:
        st.write(f"### {day}")
        for slot in time_slots:
            task_text = calendar_df.loc[day, slot]
            if task_text:
                color = color_map["Flexible" if "Flexible" in task_text else task["category"]]
                st.markdown(f'<div style="background-color:{color};padding:10px;border-radius:5px">{slot}: {task_text}</div>', unsafe_allow_html=True)

    st.session_state.calendar_generated = True

# Main function to control page navigation
def main():
    st.sidebar.title("Navigation")
    st.sidebar.radio("Go to", ["Smart Calendar", "Progress", "Resources", "Health Tips"], key="nav")

    # Initialize session state if not already set
    if "page" not in st.session_state:
        st.session_state.page = "welcome"

    # Display appropriate page based on session state
    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "smart_calendar":
        st.title("Smart Calendar")
        add_task()
        if st.button("Generate Calendar"):
            generate_calendar()
            st.session_state.page = "generated_calendar"
    elif st.session_state.page == "generated_calendar":
        if not st.session_state.calendar_generated:
            generate_calendar()
        if st.button("Add More Tasks"):
            st.session_state.page = "smart_calendar"
            st.session_state.calendar_generated = False  # Reset to allow more tasks to be added

# Run the app
if __name__ == "__main__":
    main()
