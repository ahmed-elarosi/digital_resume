from pathlib import Path

import streamlit as st
from PIL import Image


current_dir =Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ahmed_Elarosi.pdf"
profile_pic = current_dir / "assets" / "pfp.jpg"


#--settings--#
PAGE_TITLE = "Digital resume | Ahmed Elarosi"
PAGE_ICON = "random"
NAME = "Ahmed Elarosi"
DESCRIPTION = """
Junior Software Dev | DDD Enthusiast | Web App & API Development | Python/JS
"""
EMAIL ="ahmed_elarosi@proton.me"



