from pathlib import Path

import streamlit as st
from PIL import Image


current_dir =Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ahmed_Elarosi.pdf"
profile_pic = current_dir / "assets" / "a.h.jpg"


#--settings--#
PAGE_TITLE = "Digital resume | Ahmed Elarosi"
PAGE_ICON = "random"
NAME = "Ahmed Elarosi"
DESCRIPTION = """
Junior Software Dev | DDD Enthusiast | Web App & API Development | Python/JS
"""
EMAIL ="ahmed_elarosi@proton.me"
SOCIAL_MEDIA = {
"LinkedIn": "https://www.linkedin.com/in/ahmed-elarosi/",
"GitHub": " https://github.com/Ahmed-Elarosi",
"xing": "https://www.xing.com/profile/Ahmed_Elarosi/cv",

}
Projects = {

"portfolio": "https://ahmed-elarosi.vercel.app/",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

#--styles--#
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

#-- HERO --#

col1, col2 = st.columns(2,gap="small")

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.markdown(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name="Ahmed_Elarosi.pdf",
        mime="application/pdf",
        )

    st.write(f"📧 {EMAIL}")
