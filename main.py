import streamlit as st

# Function to create Home Page
def home():
    st.title("Home Page")
    st.write("Welcome to our website!")
    st.write("Navigate to other pages using the sidebar.")

# Function to create Team Page
def team():
    st.title("Team Page")
    st.write("Meet our team members here.")

# Function to create Predict Page
def predict():
    st.title("Predict Page")
    st.write("Make predictions using our tool.")
    st.write("To access the main application, click [here](http://localhost:8502).")

# Function to create Contact Us Page
def contact_us():
    st.title("Contact Us Page")
    st.write("Feel free to contact us for any queries or feedback.")

# Main function to handle page navigation
def main():
    # Apply custom CSS styles
    st.markdown(
        """
        <style>
            
            .sidebar .sidebar-content {
                background-color: #00000;
            }
            .css-1vqcepb {
                color: #333333;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 12px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Home", "Team", "Predict", "Contact Us"))

    if page == "Home":
        home()
    elif page == "Team":
        team()
    elif page == "Predict":
        predict()
    elif page == "Contact Us":
        contact_us()

if __name__ == "__main__":
    main()
