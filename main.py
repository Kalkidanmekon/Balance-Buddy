import streamlit as st

# Title
st.title("New Recurring Event")

# Event Type
st.subheader("Type")
event_type = st.selectbox("Select Type", ["Work", "Family", "Social", "Triathlon", "Study"], index=4)

# Hours per Week
st.subheader("Hours/Week")
hours_per_week = st.number_input("Enter hours per week", min_value=1, max_value=40, value=20, step=1)

# Day Selector
st.subheader("Day")
selected_days = st.multiselect("Select Day(s)", ["Su", "M", "Tu", "W", "Th", "F", "Sa"])

# Time of Day
st.subheader("Time of Day")
time_of_day = st.radio(
    "Choose Time of Day",
    ["Morning", "Afternoon", "Evening"],
    horizontal=True,
)

if time_of_day == "Morning":
    time_period = st.radio("Select Time", ["Early", "Late"], horizontal=True, key="morning")
elif time_of_day == "Afternoon":
    time_period = st.radio("Select Time", ["Early", "Late"], horizontal=True, key="afternoon")
else:
    time_period = st.radio("Select Time", ["Early", "Late"], horizontal=True, key="evening")

# Summary
st.write("---")
st.write("### Summary of Event")
st.write(f"**Type**: {event_type}")
st.write(f"**Hours/Week**: {hours_per_week}")
st.write(f"**Days**: {', '.join(selected_days)}")
st.write(f"**Time of Day**: {time_of_day} ({time_period})")
