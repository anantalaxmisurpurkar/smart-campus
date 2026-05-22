elif menu == "Report Issue":

    st.header("📢 Report Campus Issue")

    student_name = st.text_input("Student Name")

    location = st.text_input("Location")

    issue_type = st.selectbox(
        "Issue Type",
        [
            "WiFi Problem",
            "Projector Issue",
            "Broken Chair",
            "Computer Not Working",
            "Electricity Problem"
        ]
    )

    description = st.text_area("Issue Description")

    if st.button("Submit Issue"):

        issue = {
            "Student Name": student_name,
            "Location": location,
            "Issue Type": issue_type,
            "Description": description,
            "Status": "Pending"
        }

        st.session_state.issues.append(issue)

        st.success("Issue Submitted Successfully!")
