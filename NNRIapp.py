
import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #2e6259;
            color: white;
        }
        h1, h2, h3, h4, h5, h6, p, div {
            color: white !important;
        }
        .css-1d391kg, .css-ffhzg2, .css-1v3fvcr {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Logo ---
st.image("logo.jpeg", width=150)

# --- Header ---
st.title("NeuroNur Research Initiative NNRI")
st.subheader("Advancing neuroscience research through global collaboration 🌍")
# --- Mission ---
st.markdown("### 🌿 Mission")
st.write(
    "Advancing neuroscience research through global collaboration and open data. "
    "NeuroNur is a volunteer-based initiative empowering Saudi scientists to lead innovative neuroscience research "
    "by connecting with global collaborators, designing impactful studies, and fostering a culture of data sharing and transparency."
)

# --- Vision ---
st.markdown("### 🌌 Vision")
st.write(
    "To build a globally connected neuroscience community where Saudi researchers lead and contribute "
    "to cutting-edge discoveries, foster open science, and inspire the next generation of innovators dedicated "
    "to understanding the brain and improving lives."
)

# --- Join Us ---
st.markdown("### ✨ Join Us")
st.write(
    "We're building a team of researchers, students, and volunteers! If you're interested in collaborating "
    "on neuroscience, data analysis, or outreach, [click here to apply](https://forms.gle/your-google-form-link)."
)

# --- Projects ---
st.markdown("### 🔬 Our First Project")
st.info(
    "Launching June 2025 – Topic: Neural biomarkers for early Alzheimer's detection (details coming soon!)"
)

# --- Footer ---
st.markdown("---")
st.caption("© 2025 NeuroNur | Built with 💚 by volunteers worldwide")
