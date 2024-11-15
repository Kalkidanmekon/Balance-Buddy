import streamlit as st
from datetime import datetime, timedelta

# Function to display the welcome page
def welcome_page():
    st.title("Balance Buddy")
    st.subheader("Achieve control over your life by incorporating health and work!")
    if st.button("Get Started"):
        st.session_state.page = "smart_calendar"

# Function to add a new task
def add_task():
    task_name = st.text_input("Enter Task Name (e.g., 'Econ', 'Reading')", key=f"task_{len(st.session_state.tasks)}")
    if task_name:
        category = st.selectbox("Category", ["Work", "Self-Care", "Class", "Social Life"], key=f"category_{task_name}")
        flexible = st.radio("Is it flexible?", ["Yes", "No"], key=f"flexible_{task_name}")

        if flexible == "No":
            start_time = st.time_input("Start Time", key=f"start_time_{task_name}")
            duration = st.number_input("Duration (hours)", min_value=1, max_value=12, key=f"duration_{task_name}")
            recurring = st.radio("Is it recurring?", ["Yes", "No"], key=f"recurring_{task_name}")
            if recurring == "Yes":
                days = st.multiselect("Select Days for Recurrence", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], key=f"days_{task_name}")
        else:
            time_of_day = st.radio("Preferred Time of Day", ["Morning", "Afternoon", "Evening"], key=f"timeofday_{task_name}")
            duration = st.number_input("Duration (hours)", min_value=1, max_value=12, key=f"flexible_duration_{task_name}")

        deadline = st.date_input("Deadline (if applicable)", key=f"deadline_{task_name}", value=datetime.today())

        # Add task to session state
        if st.button("Add Task"):
            st.session_state.tasks.append({
                "name": task_name,
                "category": category,
                "flexible": flexible,
                "start_time": start_time if flexible == "No" else None,
                "duration": duration,
                "recurring": recurring if flexible == "No" else None,
                "days": days if flexible == "No" and recurring == "Yes" else None,
                "time_of_day": time_of_day if flexible == "Yes" else None,
                "deadline": deadline
            })
            st.success("Task added!")

# Function to generate a basic calendar view
def generate_calendar():
    st.title("Generated Calendar")
    st.write("Here is your organized weekly schedule based on the tasks entered:")
    for task in st.session_state.tasks:
        st.write(f"**{task['name']}**")
        st.write(f"- Category: {task['category']}")
        if task["flexible"] == "No":
            st.write(f"- Start Time: {task['start_time']}")
            st.write(f"- Duration: {task['duration']} hours")
            if task["recurring"] == "Yes":
                st.write(f"- Recurs on: {', '.join(task['days'])}")
        else:
            st.write(f"- Preferred Time of Day: {task['time_of_day']}")
            st.write(f"- Duration: {task['duration']} hours")
        st.write(f"- Deadline: {task['deadline']}")
        st.write("---")

# Main function to control page navigation
def main():
    st.sidebar.title("Navigation")
    st.sidebar.radio("Go to", ["Smart Calendar", "Progress", "Resources", "Health Tips"], key="nav")

    # Initialize session state if not already set
    if "page" not in st.session_state:
        st.session_state.page = "welcome"
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Display appropriate page based on session state
    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "smart_calendar":
        st.title("Smart Calendar")
        add_task()
        if st.button("Generate Calendar"):
            st.session_state.page = "generated_calendar"
    elif st.session_state.page == "generated_calendar":
        generate_calendar()

# Run the app
if __name__ == "__main__":
    main()
