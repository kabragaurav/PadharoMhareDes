import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Explore Gaurav Kabra's Portfolio",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for gradient background and button styling
st.markdown("""
    <style>
    /* Gradient background */
    body {
        background: linear-gradient(135deg, #1e1e2f, #343650, #4a4a6a, #616184, #79799f);
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }
    /* Center container */
    .main-content {
        text-align: center;
        margin-top: 100px;
    }
    /* Button style */
    .stButton button {
        background-color: #fb8500;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #ffb703;
    }
    </style>
""", unsafe_allow_html=True)

# Main content container
with st.container():
    st.markdown("<div class='main-content'>", unsafe_allow_html=True)
    
    # Heading and description
    st.title("Welcome to My World!")
    st.subheader("Explore my projects, skills, and more on my website.")
    
    # Button to open website
    if st.button("Visit My Website"):
        st.write("Redirecting to my website...")
        st.markdown("[Visit Gaurav Kabra's Website](https://gauravkabra.netlify.app/)")
    
    st.markdown("</div>", unsafe_allow_html=True)
