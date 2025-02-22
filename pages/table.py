import streamlit as st

st.set_page_config(page_title="Styled Table with Cards", page_icon="📊", layout="wide")

def card():
    # Custom CSS for Styling
    st.markdown(
        """
        <style>
        .card {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .btn {
            background-color: black;
            color: white;
            padding: 8px 15px;
            margin: 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .btn:hover {
            background-color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Example Data (Each Row)
    data = [
        {
            "buttons": ["Reassign Job", "Agent Cancel", "Client Cancel", "Make Note"],
            "amount": "$180",
            "client_name": "Ava DeSena",
            "client_email": "adsena88@gmail.com",
            "client_phone": "643 345 4456",
            "status": "WAS CANCELLED BY ORIGINAL PRO",
            "agent_email": "jillianocasio@me.com",
            "appointment_time": "Feb 21, 2025 - 8:30 AM",
            "location": "1 Grand Cypress Blvd, Orlando, FL 32836",
        },
        # Add more rows as needed
    ]

    # Create a Table-Like Structure
    for row in data:
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 2])

        # Column 1 - Action Buttons
        with col1:
            for btn in row["buttons"]:
                st.markdown(f'<button class="btn">{btn}</button>', unsafe_allow_html=True)

        # Column 2 - Pricing & Client Info
        with col2:
            st.markdown(f'<div class="card"> Svcs: {row["amount"]} </div>', unsafe_allow_html=True)
            st.markdown(f'<div class="card"> {row["client_name"]} <br> {row["client_phone"]} <br> {row["client_email"]} </div>', unsafe_allow_html=True)
            st.markdown('<button class="btn">Credit Client</button>', unsafe_allow_html=True)
        
        # Column 3 - Agent Info
        with col3:
            st.markdown(f'<div class="card"> {row["agent_email"]} <br> {row["status"]} </div>', unsafe_allow_html=True)
            st.markdown('<button class="btn">Press En Route</button>', unsafe_allow_html=True)

        # Column 4 - Appointment Time
        with col4:
            st.markdown(f'<div class="card"> {row["appointment_time"]} </div>', unsafe_allow_html=True)
            st.selectbox("Change Day:", ["Feb 21, 2025", "Feb 22, 2025"])
            st.selectbox("Change Time:", ["8:30 AM", "10:00 AM"])
            st.button("Get Available Times")

        # Column 5 - Location & More Actions
        with col5:
            st.markdown(f'<div class="card"> {row["location"]} </div>', unsafe_allow_html=True)
            st.markdown('<button class="btn">Change Addr</button>', unsafe_allow_html=True)
            st.markdown('<button class="btn">Block User</button>', unsafe_allow_html=True)

        st.divider()  # Adds a separator between rows

# card()
# card()