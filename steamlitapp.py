import streamlit as st 
import streamlit as st

# Sidebar Navigation
st.sidebar.title("Go Norquest 🚗")
page = st.sidebar.radio("Navigate", ["Overview", "About us", "Exploratory Data Analysis", "Machine learning"])

# Page: Overview
if page == "Overview":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Streamlit_logo.png/1200px-Streamlit_logo.png", width=150)
    st.title("Welcome to the Go Auto Sales Analysis Project!")
    st.write("""
    This project leverages a **dataset compiled by the Business Intelligence Team at Go Auto**, utilizing APIs
    from the **Canadian Black Book (CBB)**. The dataset includes:
    - **Vehicle Listings**: Active and sold vehicles across various dealerships in Edmonton within the last 30 days.
    - **Details**: Each listing provides rich details such as year, make, model, mileage, price, and dealership location.
    """)

    st.subheader("⚙️ Project Goal:")
    st.write("""
    The main goal of this project was to:
    - Apply **Exploratory Data Analysis (EDA)** techniques.
    - Develop a **Machine Learning Model** for clustering.
    - Use **Power BI Visualizations** to:
        - Analyze geographical clusters in Edmonton.
    """)

# Page: About us
elif page == "About us":
    st.title("About Us")
    st.write("""
    **Go Norquest** is a collaborative project to analyze vehicle sales and dealership performance in Edmonton. 
    We aim to empower dealerships with actionable insights using data and machine learning.
    """)

# Page: Exploratory Data Analysis
elif page == "Exploratory Data Analysis":
    st.title("Exploratory Data Analysis")
    st.write("""
    In this section, we explore the dataset, uncover trends, and visualize key statistics to better understand vehicle sales.
    """)

# Page: Machine Learning
elif page == "Machine learning":
    st.title("Machine Learning")
    st.write("""
    Here, we build machine learning models to predict sales patterns and optimize dealership operations.
    """)

# Footer
st.sidebar.markdown("### Contact Us")
st.sidebar.info("For questions, email us at: contact@norquest.com")
