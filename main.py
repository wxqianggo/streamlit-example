import streamlit as st

# Homepage
def homepage():
    st.title("Welcome to our new startup!")
    st.write("We specialize in talking with specialists by GPT.")
    st.write("Check out our About and Contact pages to learn more!")

# About page
def about():
    st.title("About Us")
    st.write("Our startup was founded in 2021 with the goal of revolutionizing the way specialists communicate with GPT.")
    st.write("We believe that our technology has the potential to transform the industry and improve the lives of millions of people.")

# Contact page
def contact():
    st.title("Contact Us")
    st.write("If you have any questions or would like to learn more about our startup, please contact us at:")
    st.write("- Email: info@ourstartup.com")
    st.write("- Phone: 555-1234")

# Page Navigation
pages = {
    "Homepage": homepage,
    "About": about,
    "Contact": contact
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))
page = pages[selection]
page()
