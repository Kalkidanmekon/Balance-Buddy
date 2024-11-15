import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- App Title ---
st.set_page_config(page_title="Equilibrium", layout="wide")
st.title("Welcome to Equilibrium")
st.subheader("Your AI-driven wellness scheduler for balance in work, health, and life.")

# --- Health Tip of the Day ---
health_tips = [
    "Remember to take breaks to stretch and hydrate.",
    "Meditation can help you stay grounded during busy days.",
    "A balanced diet improves productivity and mood.",
    "Exercise regularly to reduce stress and boost energy."
]

# Random tip of the day (simulated)
import random
tip_of_the_day = random.choice(health_tips)

st.markdown(f"**Tip of the Day**: {tip_of_the_day}")

# Button to proceed to next step
if st.button('Next: Start Organizing'):
    st.write("Great! Let's get started with organizing your schedule.")

    # --- User Task Input ---
    st.header("Step 1: Enter Your Tasks")

    # Create an empty DataFrame to store user inputs
    task_data = []

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for day in days_of_week:
        st.subheader(f"Enter tasks for {day}")

        # Task Name
        task_name = st.text_input(f"Task for {day}", key=f"task_{day}")
        if task_name:
            # Category: Work, Health, etc.
            category = st.selectbox("Category", ["Work", "Health", "Social", "Personal Development", "Other"], key=f"category_{day}")

            # Flexible/Non-Flexible
            is_flexible = st.radio("Is this task flexible?", ['Yes', 'No'], key=f"flexible_{day}")
            
            # Flexible tasks: preferred time of day
            if is_flexible == 'Yes':
                preferred_time = st.selectbox(f"Preferred time for {task_name}", ["Morning", "Afternoon", "Evening"], key=f"preferred_time_{day}")
            else:
                preferred_time = "Fixed Time"
            
            # Deadline for homework-like tasks (only if flexible)
            if 'homework' in task_name.lower():
                deadline_date = st.date_input(f"Deadline for {task_name}", key=f"deadline_{day}")
            else:
                deadline_date = None
            
            # Collect task details
            task_data.append({
                "Task": task_name,
                "Category": category,
                "Day": day,
                "Flexible": is_flexible,
                "Preferred Time": preferred_time,
                "Deadline": deadline_date
            })

        st.write("\n")
    
    # Button to submit tasks and generate the schedule
    if st.button('Generate Your Schedule'):
        if task_data:
            st.write("**Your Proposed Schedule**:")

            # --- Generate Proposed Schedule ---
            schedule_df = pd.DataFrame(task_data)

            # Display the proposed schedule
            st.dataframe(schedule_df)

            st.write("This is your proposed schedule. Remember, flexible tasks can be moved around.")

            # --- Task Progress Tracking (Simulated) ---
            st.header("Step 2: Track Your Progress")
            st.write("At the end of each task, we'll track whether you were able to complete it.")

            task_status = []
            for _, row in schedule_df.iterrows():
                task_completion = st.selectbox(f"Did you complete {row['Task']}?", ['Yes', 'No'], key=f"completion_{row['Task']}")
                task_status.append(task_completion)
            
            # Show task completion status
            st.write("**Your Progress:**")
            task_status_df = schedule_df.copy()
            task_status_df['Completion'] = task_status

            st.dataframe(task_status_df)

            st.write("Great job! Keep going!")

            # --- Weekly Analytics (Simulated) ---
            if st.button('Finish Week'):
                st.write("**Weekly Analytics:**")

                completed_tasks = task_status.count('Yes')
                total_tasks = len(task_status)
                completion_rate = (completed_tasks / total_tasks) * 100

                st.write(f"You completed {completed_tasks} out of {total_tasks} tasks this week.")
                st.write(f"Your task completion rate is {completion_rate}%.")

                # Feelings Survey
                st.write("How do you feel about this week's progress?")
                feelings = st.radio("Select how you feel:", ["Great", "Okay", "Could Improve"], key="feelings")

                # Future Recommendations
                if feelings == "Could Improve":
                    st.write("We recommend incorporating more health activities into your schedule next week!")
                elif feelings == "Okay":
                    st.write("Nice job! Let's aim for a better balance next week!")
                else:
                    st.write("Fantastic work! Keep it up!")

                st.write("We'll adjust your schedule based on your feedback for next week.")

            st.write("\n")
        
        else:
            st.error("Please enter at least one task to generate a schedule.")


# Run the app
if __name__ == "__main__":
    main()
