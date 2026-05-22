elif menu == "View Issues":

    st.header("📋 Reported Issues")

    if len(st.session_state.issues) == 0:

        st.warning("No Issues Reported Yet")

    else:

        df = pd.DataFrame(st.session_state.issues)

        st.dataframe(df)

        st.subheader("Resolve Issue")

        issue_index = st.number_input(
            "Enter Issue Index",
            min_value=0,
            max_value=len(st.session_state.issues)-1,
            step=1
        )

        if st.button("Mark as Resolved"):

            st.session_state.issues[issue_index]["Status"] = "Resolved"

            st.success("Issue Resolved Successfully!")
