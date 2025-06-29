import streamlit as st
from PIL import Image

# --- Page Configuration ---
st.set_page_config(page_title="Laura Ndoigo | Portfolio", page_icon="👩‍💻")

# --- Load and Display Profile Image ---
try:
    image = Image.open("profile.jpg")  # Make sure profile.jpg is in the same folder
    st.image(image, width=200)
except Exception as e:
    st.warning("⚠️ Could not load profile image. Make sure 'profile.jpg' exists.")

# --- Portfolio Header ---
st.title("👩🏾‍💻 Laura Ndoigo")

# --- About Me ---
st.header("About Me")
st.write("""
Hi there! I’m a Health Informatics trainee with a background in medical device engineering.I specialize in bridging clinical innovation and digital health, ensuring that emerging health technologies are safe, effective, and aligned with real-world patient care needs.
""")

# --- Contact Section ---
st.header("Contact")
st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/laura-ndoigo-383362132/)")
st.markdown("[🐙 GitHub](https://github.com/laurandoigo)")  # Replace with your GitHub username
st.markdown("[✉️ Email](mailto:bekyibeilaurandoigo@gmail.com)")   # Replace with your email
