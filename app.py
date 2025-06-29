import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="Simple Portfolio", page_icon="👩‍💻")

# Load your profile image
# Replace 'profile.jpg' with your image file path or URL
image = Image.open("profile.jpg")

# Display the image
st.image(image, width=200)  # Adjust width as needed

# Title
st.title("👩‍💻 Your Name")

# About Me
st.header("About Me")
st.write("""
Write a short introduction about yourself here.  
You can include your background, interests, and what you do.
""")

# Skills
st.header("Skills")
st.write("""
- Skill 1  
- Skill 2  
- Skill 3  
- Skill 4  
""")

# Projects
st.header("Projects")

st.markdown("""
### Project One
A short description of project one.  
[GitHub Repo](https://github.com/yourgithub/project-one)

### Project Two
A short description of project two.  
[GitHub Repo](https://github.com/yourgithub/project-two)
""")

# Contact
st.header("Contact")
st.markdown("[LinkedIn](https://www.linkedin.com/in/yourlinkedin)")
st.markdown("[GitHub](https://github.com/yourgithub)")
st.markdown("[Email](mailto:youremail@example.com)")
