elif menu == "Track Resources":

    st.header("💻 Campus Resource Tracker")

    resource_data = pd.DataFrame({

        "Resource": [
            "Computer Lab 1",
            "Computer Lab 2",
            "Library Hall",
            "Study Room A",
            "Projector Room"
        ],

        "Status": [
            "Available",
            "Occupied",
            "Available",
            "Occupied",
            "Available"
        ]
    })

    st.table(resource_data)
