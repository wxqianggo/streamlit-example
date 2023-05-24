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
    
def app():
    st.title("Welcome to our Startup!")
    st.write("We are a team of specialists who can help you with anything you need.")
    st.write("Our goal is to provide you with the best possible service and make sure you are satisfied with our work.")
    st.write("Please click the button below to get in touch with us and learn more about our services.")
    if st.button("Contact Us"):
        st.write("You can reach us at info@startup.com")
 
    st.markdown(
        """
        <div style='background-color: #f5f5f5; padding: 5rem 0;'>
            <h1 style='text-align: center; font-size: 4rem; margin-bottom: 2rem;'>Welcome to our Startup!</h1>
            <p style='text-align: center; font-size: 2rem; margin-bottom: 2rem;'>We are a team of specialists who can help you with anything you need.</p>
            <p style='text-align: center; font-size: 2rem; margin-bottom: 2rem;'>Our goal is to provide you with the best possible service and make sure you are satisfied with our work.</p>
            <div style='text-align: center;'>
                <a href='/contact' style='background-color: #0072c6; color: white; font-size: 2rem; padding: 1rem 2rem; border-radius: 1rem; text-decoration: none;'>Contact Us</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
if __name__ == '__main__':
    app()

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
