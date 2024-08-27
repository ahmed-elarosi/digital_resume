from pathlib import Path

import streamlit as st
from PIL import Image
from googletrans import Translator  # For translation

current_dir =Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ahmed_Elarosi_Softwareentwickler_Bewerbung.pdf"
profile_pic = current_dir / "assets" / "hamdi.jpg"
translator = Translator()  # Create a translator instance


#--settings--#
PAGE_TITLE = "Digital resume | Ahmed Elarosi"
PAGE_ICON = "🦉"
NAME = "Ahmed Elarosi"
DESCRIPTION = """
Junior Software Developer | DDD Enthusiast | Web App & API Development | Python/JS

Business and finance background with over 10 years of experience
"""
EMAIL ="ahmed_elarosi@proton.me"
PHONE = "+49 1729851066"
HOME = "Rosenheim, Germany"
SOCIAL_MEDIA = {
"LinkedIn": "https://www.linkedin.com/in/ahmed-elarosi/",
"GitHub": " https://github.com/Ahmed-Elarosi",
"Xing": "https://www.xing.com/profile/Ahmed_Elarosi/cv",


}

def translate_text(text, target_language="en"):
    """Translates text to the specified language."""
    if target_language == "en":  # No translation needed if English
        return text
    return translator.translate(text, dest=target_language).text

def load_content(language="en"):
    """Loads content dynamically based on the chosen language."""
    #st.title(translate_text(HOME, language))
    # st.markdown(translate_text(DESCRIPTION, language))

Projects = {
"🏆 Automation File Management sorts files into folders based on their type using :blue[Python]":"https://github.com/Ahmed-Elarosi/file_management",
"🏆 Personal portfolio website using :blue[Next.js, a React framework]": "https://ahmed-elarosi.vercel.app/",
"🏆 Imageboard, a simple social media app, Full Stack :blue[MERN (Mongo,Express,React,Node)]": "https://imageboard.vercel.app/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Language Selection ---
st.sidebar.subheader("Language")
language = st.sidebar.selectbox(
    "Choose a language",
    ("English", "Arabic", "German")  # Add more languages as needed
)

#--styles--#
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)
load_content(language)

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
    st.write(f"📱 {PHONE}")
    st.write(f"🏠 {translate_text(HOME, language)}")

#-- SOCIAL MEDIA --#

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (name, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[index]:
        st.markdown(f"[{translate_text(name, language)}]({link})")

# -- experience --#
st.write("#")
st.subheader(":blue[Experience & Qualifications]", divider='rainbow')
st.write("""

- ✔️ 3 years of experience in software development
- ✔️ 10 years of experience in business and finance
- ✔️ strong hands on experience in web app and API development
- ✔️ Strong knowledge in Python and JavaScript
- ✔️ Excellent team player, self-motivated and displaying strong sense of initiative on tasks
- ✔️ Strong analytical and problem-solving skills
- ✔️ Strong communication and interpersonal skills
""")

# --skills--#
st.write("#")
st.subheader(":blue[Skills]",divider='rainbow')
st.write(
    """

- 👨🏻‍💻 ***Programming Languages:*** Python, JavaScript, TypeScript
- 📚 ***Web Frameworks & Libraries:*** React, Streamlit, Flask
- 🌐 ***Web Technologies:*** Web Components
- 🤖 ***DevOps Tools:*** Jenkins, Docker, Kafka, Kubernetes, Microservices, Mogodb
- 🌩️ ***Cloud Platforms:*** AWS  (S3, EC2, API Gateway)
- 🚀 ***Version Control:*** Git
- 📊 ***Agile Development & Project Management Tools:*** Jira, Trello, YouTrack

""")

# -- work experience --#

st.write("#")
st.subheader(":blue[Work History]",divider='rainbow')

# -- 1st job --#
st.write("🚧", "**Software developer | StickX Textilveredelung**" )
st.write("10/2022 - 04/2024")
st.write("""
- ➡️ Designing and implementing company-internal REST-API-
based web applications in close collaboration with users,
using the Domain Driven Design approach
- ➡️ Writing unit and integration tests to ensure the quality
and reliability of the code
- ➡️ Developing and maintaining the company's website
- ➡️ Developing algorithms to solve business problems,
improving efficiency and productivity
- ➡️ Conceptualizing and implementing database applications
to store and manage data effectively
- ➡️ Integrating external interfaces into the software
architecture (using API or FTP) to expand functionality
and connectivity
- ➡️ Developing internal libraries to parse supplier emails and
PDF files, automating data extraction and processing
- ➡️ Creating comprehensive documentation for software
components and user guides for easy understanding and
usage
""")

# -- 2nd job --#
st.write("🚧", "**Arabic outreach program manager | Wikimedia Deutschland**" )
st.write("20/2019 - 01/2020")
st.write("""
- ➡️ Working with the Arabic language communities, country
by country (or affiliate by affiliate) to audit their needs
for documentation, partnership, outreach, awareness,
and education
- ➡️ Overseeing a project with Arabic volunteers to
prepare/translate appropriate materials based on these
needs related to major Wikimedia initiatives
""")

# -- 3rd job --#
st.write("🚧", "**Medical laboratory assistant | Quick lab**" )
st.write("08/2016 - 10/2018")
st.write("""
- ➡️ Collecting blood samples from patients.
- ➡️ Deciphering the best method for drawing blood for every
individual patient.
- ➡️ Initiating the centrifuging of blood samples, depending
on if this is allowed in the state you are working in
""")

#-- 4th job --#
st.write("🚧", "**Chief accountant | Shorakaa for real estate**" )
st.write("02/2011 - 07/2018")
st.write("""
- ➡️ Processing with banks, cashing checks, and making
transfers.
- ➡️ Preparing monthly profit and loss statements, and
resolving accounting discrepancies and irregularities
""")

#-- 5th job --#
st.write("🚧", "**Senior accountant and auditor | Consulting group (MFA)**" )
st.write("07/2010 - 01/2011")
st.write("""
- ➡️ Assisting in the design and preparation of feasibility
study for many companies and projects
- ➡️ Performing monthly balance sheet, income statement
and changes in financial position/budget variance
analyses
- ➡️ Preparing bank reconciliation statements and performing
other administrative work
""")

#-- 6th job --#
st.write("🚧", "**Senior accountant | Diving ocean new project**" )
st.write("09/2008 - 06/2010")
st.write("""
- ➡️ Establishing, maintaining, and coordinating the
implementation of accounting procedures
- ➡️ Reconciling accounting inconsistencies
- ➡️ Identifying accounting system (NAUTILUS) discrepancies
""")

# -- Projects and Accomplishments --#
st.write("#")
st.subheader(":blue[Projects and Accomplishments]",divider='rainbow')
for name, link in Projects.items():
    st.markdown(f"[{name}]({link})")


# -- Education --#
st.write("#")
st.subheader(":blue[Education]",divider='rainbow')


## -- Volunteering --#
st.write("#")
st.subheader(":blue[Volunteering]",divider='rainbow')
st.write("""
- ✅ Wikimedia Movement
- ✅ Member of Wikimania 2018 program team - Cape Town.
- ✅ Member of Wikiindaba 2017 program team - Accra.
- ✅ Chief organizer of WikiArabia 2017 - Cairo.
- ✅ Editor at Arabic Wikipedia.

    """)