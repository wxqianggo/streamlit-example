import openai
import streamlit as st

openai.api_key = "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"

# Define the function to generate responses using GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message.strip()


# Homepage
def homepage():
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
    # Define the contact page
    st.title("Contact Us")
    st.write("Please fill out the form below or ask us a question using the chatbot.")
    
    # Add a form for users to submit their contact information
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.button("Submit")
    
    # Add the GPT-3 chatbot
    st.sidebar.title("Chat with a Specialist")
    prompt = st.sidebar.text_input("Ask a question")
    if prompt:
        response = generate_response(prompt)
        st.sidebar.write(response)
    
    # Add a confirmation message after the form is submitted
    if submit:
        st.write("Thank you for contacting us! We will get back to you soon.")
 
   
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
