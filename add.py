import streamlit as st
import pandas as pd
from datetime import datetime

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Smart Campus Tracker",
    layout="wide"
)

# ---------------- TITLE ----------------

st.title("🏫 Smart Campus: Live Resource & Issue Tracker")

st.markdown("---")

# ---------------- SESSION STORAGE ----------------

if "issues" not in st.session_state:
    st.session_state.issues = []

# ---------------- SIDEBAR ----------------

menu = st.sidebar.selectbox(
    "Select Menu",
    [
        "Home",
        "Report Issue",
        "Track Resources",
        "View Issues",
        "Analytics Dashboard",
        "Feedback",
        "Emergency Contacts"
    ]
)

# ---------------- HOME ----------------

if menu == "Home":

    st.header("🏫 Welcome to Smart Campus System")

    st.write("""
    This Smart Campus System helps students and staff to:
    
    ✅ Report campus problems  
    ✅ Track campus resources  
    ✅ Monitor issue status  
    ✅ View analytics dashboard  
    ✅ Submit feedback  
    ✅ Access emergency contacts  
    """)

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=250
    )

# ---------------- REPORT ISSUE ----------------

elif menu == "Report Issue":

    st.header("📢 Report Campus Issue")

    student_name = st.text_input("Student Name")

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "Mechanical", "Civil"]
    )

    location = st.text_input("Location")

    issue_type = st.selectbox(
        "Issue Type",
        [
            "WiFi Problem",
            "Projector Issue",
            "Broken Chair",
            "Computer Not Working",
            "Electricity Problem",
            "Water Leakage",
            "Fan Not Working"
        ]
    )

    priority = st.selectbox(
        "Priority Level",
        ["Low", "Medium", "High"]
    )

    description = st.text_area("Issue Description")

    if st.button("Submit Issue"):

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        issue = {
            "Student Name": student_name,
            "Department": department,
            "Location": location,
            "Issue Type": issue_type,
            "Priority": priority,
            "Description": description,
            "Status": "Pending",
            "Time": current_time
        }

        st.session_state.issues.append(issue)

        st.success("✅ Issue Submitted Successfully!")

# ---------------- TRACK RESOURCES ----------------

elif menu == "Track Resources":

    st.header("💻 Campus Resource Tracker")

    resource_data = pd.DataFrame({

        "Resource": [
            "Computer Lab 1",
            "Computer Lab 2",
            "Library Hall",
            "Study Room A",
            "Projector Room",
            "Seminar Hall"
        ],

        "Status": [
            "Available",
            "Occupied",
            "Available",
            "Occupied",
            "Available",
            "Available"
        ],

        "Capacity": [
            60,
            45,
            120,
            20,
            100,
            200
        ]
    })

    st.table(resource_data)

# ---------------- VIEW ISSUES ----------------

elif menu == "View Issues":

    st.header("📋 Reported Issues")

    if len(st.session_state.issues) == 0:

        st.warning("No Issues Reported Yet")

    else:

        df = pd.DataFrame(st.session_state.issues)

        st.dataframe(df)

        st.subheader("🔍 Search Issues")

        search = st.text_input("Search by Location or Issue Type")

        if search:

            filtered_df = df[
                df.astype(str).apply(
                    lambda row: row.str.contains(search, case=False).any(),
                    axis=1
                )
            ]

            st.dataframe(filtered_df)

        st.subheader("✅ Resolve Issue")

        issue_index = st.number_input(
            "Enter Issue Index",
            min_value=0,
            max_value=len(st.session_state.issues)-1,
            step=1
        )

        if st.button("Mark as Resolved"):

            st.session_state.issues[issue_index]["Status"] = "Resolved"

            st.success("Issue Resolved Successfully!")

# ---------------- ANALYTICS DASHBOARD ----------------

elif menu == "Analytics Dashboard":

    st.header("📊 Campus Analytics Dashboard")

    total_issues = len(st.session_state.issues)

    resolved = 0
    pending = 0

    for issue in st.session_state.issues:

        if issue["Status"] == "Resolved":
            resolved += 1
        else:
            pending += 1

    st.metric("Total Issues", total_issues)
    st.metric("Resolved Issues", resolved)
    st.metric("Pending Issues", pending)

    if total_issues > 0:

        chart_data = pd.DataFrame({
            "Status": ["Resolved", "Pending"],
            "Count": [resolved, pending]
        })

        st.bar_chart(chart_data.set_index("Status"))

# ---------------- FEEDBACK ----------------

elif menu == "Feedback":

    st.header("📝 Student Feedback")

    feedback = st.text_area("Write Your Feedback")

    rating = st.slider(
        "Rate Campus Services",
        1,
        5
    )

    if st.button("Submit Feedback"):

        st.success("✅ Feedback Submitted Successfully!")

        st.write("⭐ Rating:", rating)

# ---------------- EMERGENCY CONTACTS ----------------

elif menu == "Emergency Contacts":

    st.header("🚨 Emergency Contacts")

    contacts = pd.DataFrame({

        "Department": [
            "Campus Security",
            "Medical Room",
            "Fire Safety",
            "Electrical Maintenance",
            "Hostel Office"
        ],

        "Contact Number": [
            "9876543210",
            "9876501234",
            "9123456780",
            "9988776655",
            "9012345678"
        ]
    })

    st.table(contacts)

    st.success("📞 Emergency Help Available 24/7")
