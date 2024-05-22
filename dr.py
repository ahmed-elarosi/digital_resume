from pathlib import Path

import streamlit as st
from googletrans import Translator  # For translation
from PIL import Image

# -- Constants & Functions --
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ahmed_Elarosi.pdf"
profile_pic = current_dir / "assets" / "ahmed.jpg"
translator = Translator()  # Create a translator instance

PAGE_TITLE = "Digital Resume | Ahmed Elarosi"
PAGE_ICON = "🦉"

# ... (other constants like NAME, DESCRIPTION, SOCIAL_MEDIA, etc.)


def translate_text(text, target_language="en"):
    """Translates text to the specified language."""
    if target_language == "en":  # No translation needed if English
        return text
    return translator.translate(text, dest=target_language).text


def load_content(language="en"):
    """Loads content dynamically based on the chosen language."""
    st.title(translate_text(NAME, language))
    st.markdown(translate_text(DESCRIPTION, language))
    # ... (load other content elements dynamically, e.g., Skills, Experience)

    # --- SOCIAL MEDIA ---
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (name, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            st.markdown(f"[{translate_text(name, language)}]({link})")


# --- MAIN APP ---

# --- Theme Selection ---
st.sidebar.subheader("Theme")
theme = st.sidebar.selectbox(
    "Choose a theme",
    ("Light", "Dark")
)
if theme == "Dark":
    st.markdown(
        """
        <style>
        body {
            background-color: #111;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- Language Selection ---
st.sidebar.subheader("Language")
language = st.sidebar.selectbox(
    "Choose a language",
    ("English", "Arabic", "German")  # Add more languages as needed
)

# --- Main Content ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)
load_content(language)

# -- HERO --#
col1, col2 = st.columns(2, gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.download_button(
        label=translate_text("Download Resume", language),
        data=PDFbyte,
        file_name="Ahmed_Elarosi.pdf",
        mime="application/pdf",
    )
    st.write(f"📧 {EMAIL}")
    st.write(f"📱 {PHONE}")
    st.write(f"🏠 {HOME}")
