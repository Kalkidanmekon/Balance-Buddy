import streamlit as st
import datetime

# Function for Welcome Page
def welcome_page():
    st.title("Welcome to Balance Buddy!")
    st.write("""
    Welcome to **Balance Buddy**, your ultimate companion to help you balance work, health, and life. 
    We help you organize your tasks, set your priorities, and achieve a healthy routine. 
    Let's get started and make your life more balanced!
    """)
    
    # "Get Started" button to move to the next page
    if st.button("Get Started"):
        st.session_state.page = "login"  # After clicking 'Get Started', navigate to the login page

# Function for Task Input
def enter_task_page():
    st.title("Enter Your Task")
    
    # Input for Task Name
    task_name = st.text_input("Task Name (e.g., Econ, Reading)")
    
    if task_name:
        # Category Selection
        category = st.selectbox("Category", ["Work", "Health", "Study", "Personal"])
        
        # Flexibility Selection
        flexibility = st.radio("Is this task flexible?", ["Yes", "No"])
        
        if flexibility == "No":
            # If task is not flexible, ask if it's recurring
            is_recurring = st.radio("Is this task recurring?", ["Yes", "No"])
            
            if is_recurring == "Yes":
                # Recurring Task - ask for weekly timeslots
                st.write("Select the recurring timeslots within the week.")
                days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
                recurring_days = st.multiselect("Choose days for recurring task", days_of_week)
                
                st.write("Recurring task on the following days:", recurring_days)
                
                # Now the task will block the other recurring times
                st.write("The selected times for this task are blocked for the rest of the week.")
            
        elif flexibility == "Yes":
            # If task is flexible, ask for the preferred time of day and hours
            part_of_day = st.selectbox("Preferred part of the day", ["Morning", "Afternoon", "Evening"])
            hours = st.slider("Number of hours for this task", 1, 8, 1)
            
            # Display the task's selected time part and hours
            st.write(f"Your task is set for {part_of_day} for {hours} hours.")
            
            # If Evening part of the day, ask for bedtime and wake-up time
            if part_of_day == "Evening":
                bedtime = st.time_input("What time will you go to bed?", datetime.time(22, 0))
                wakeup_time = st.time_input("What time will you wake up?", datetime.time(6, 0))
                
                # Calculate sleep duration (difference between bedtime and wakeup time)
                bedtime_dt = datetime.datetime.combine(datetime.date.today(), bedtime)
                wakeup_dt = datetime.datetime.combine(datetime.date.today(), wakeup_time)
                
                if wakeup_dt < bedtime_dt:
                    # If wakeup time is earlier than bedtime (i.e., after midnight)
                    wakeup_dt += datetime.timedelta(days=1)  # Add one day to wakeup time
                
                sleep_duration = (wakeup_dt - bedtime_dt).seconds / 3600  # Sleep duration in hours
                
                # Check if sleep duration is less than 7 hours and show warning if so
                if sleep_duration < 7:
                    st.warning("Warning: You should aim for at least 7 hours of sleep for your health.")
                else:
                    st.success(f"Your sleep duration will be {sleep_duration:.1f} hours.")
        
        # Display the task once all options are filled
        st.write(f"Task: {task_name}")
        st.write(f"Category: {category}")
        st.write(f"Flexibility: {flexibility}")
        
        if flexibility == "No" and is_recurring == "Yes":
            st.write(f"Recurring on: {', '.join(recurring_days)}")
        
        elif flexibility == "Yes" and part_of_day == "Evening":
            st.write(f"Task will be done at {bedtime} and wake up at {wakeup_time}.")
        else:
            st.write(f"Task will be done in the {part_of_day} for {hours} hours.")

# Function for Tasks with Deadline (monthly)
def tasks_with_deadline_page():
    st.title("Tasks with Deadline")

    task_name = st.text_input("Task Name with Deadline (e.g., Submit Report, Complete Assignment)")
    
    if task_name:
        # Deadline Date Selection
        deadline = st.date_input("Select deadline", min_value=datetime.date.today())
        
        # Task Category
        category = st.selectbox("Category", ["Work", "Health", "Study", "Personal"])
        
        # Display task details
        st.write(f"Task: {task_name}")
        st.write(f"Category: {category}")
        st.write(f"Deadline: {deadline}")

        # Here, you can add logic to break down tasks into smaller sub-tasks
        # For now, we will just display it
        st.write("You can break this task into smaller sub-tasks to help plan your work.")
        # In future, this can be a form where users input sub-tasks for the main task.

# Main function to control navigation between pages
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "welcome"  # Default to the welcome page

    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "signup":
        signup_page()
    elif st.session_state.page == "dashboard":
        dashboard_page()
    elif st.session_state.page == "enter_task":
        enter_task_page()
    elif st.session_state.page == "tasks_with_deadline":
        tasks_with_deadline_page()

if __name__ == "__main__":
    main()
