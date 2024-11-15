import streamlit as st

def main():
    st.title("Healthy Living Goals Survey")
    
    # Section 1: Prioritization
    st.header("1. Prioritize Your Goals")
    st.write("Rank your priorities for healthy living from 1 (most important) to 5 (least important).")
    
    priorities = {
        "Sleep Hygiene": st.slider("Sleep Hygiene", 1, 5, 3),
        "Fitness": st.slider("Fitness", 1, 5, 3),
        "Work": st.slider("Work", 1, 5, 3),
        "Academics": st.slider("Academics", 1, 5, 3),
        "Other Healthy Living Goals": st.slider("Other Goals", 1, 5, 3)
    }
    
    st.write("### Your Priorities:")
    sorted_priorities = sorted(priorities.items(), key=lambda x: x[1])
    for goal, rank in sorted_priorities:
        st.write(f"{goal}: {rank}")
    
    # Section 2: Current Schedule Satisfaction
    st.header("2. How Do You Feel About Your Current Schedule?")
    current_schedule = st.radio(
        "Select one that best describes your current schedule:",
        ("I feel it's balanced", "It's manageable but needs improvement", "I'm overwhelmed and need changes")
    )
    
    st.write(f"**Your response:** {current_schedule}")
    
    # Section 3: Stress Levels
    st.header("3. How Stressed Are You About Your Daily Routine?")
    stress_level = st.slider("Stress Level (0 = No Stress, 10 = Extremely Stressed)", 0, 10, 5)
    st.write(f"**Your stress level:** {stress_level}")
    
    # Section 4: Additional Comments
    st.header("4. Any Additional Comments or Goals?")
    additional_comments = st.text_area("Let us know about any specific goals, challenges, or feedback:")
    
    # Display Summary
    if st.button("Submit"):
        st.subheader("Survey Summary")
        st.write("### Prioritization:")
        for goal, rank in sorted_priorities:
            st.write(f"{goal}: {rank}")
        
        st.write("### Current Schedule:")
        st.write(current_schedule)
        
        st.write("### Stress Level:")
        st.write(stress_level)
        
        if additional_comments:
            st.write("### Additional Comments:")
            st.write(additional_comments)
        else:
            st.write("No additional comments provided.")
        
        st.success("Thank you for completing the survey!")

if __name__ == "__main__":
    main()
