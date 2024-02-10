from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | FELIPE IGNACIO MUNHOZ TOLEDO"
PAGE_ICON = ":love:"
NAME = "Felipe Ignacio Muñoz Toledo"
DESCRIPTION = """
Chemical Engineer with an MSc. in Computational Mechanics, offering specialized consultancy services in modeling, simulation, and process optimization. With expertise in utilizing computational tools. 
"""


EMAIL = "felipe.toledo@coc.ufrj.br"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/felipemunoztoledo",
    "GitHub": "https://github.com/felipe77-CH",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="centered",initial_sidebar_state="auto")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Experience in project management and technical consulting in various industrial sectors (4 years)
- ✔️ Preparation of technical documentation for executive projects.
- ✔️ Good understanding of innovation principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Leadership of multidisciplinary teams in finding holistic solutions to complex problems
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, Matlab
- 📊 Data Visulization: PowerBi, MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
- ⌨️ Tools: Git, Jupyter
- ⌨️ Process modeling: HYSYS, DWSYM 
- ⌨️ Fluid dynamic simulations: OpenFoam, Ansys (CFX E Fluent)

"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Technical Consultant | Project Engineers**")
st.write("09/2022 - Present")
st.write(
    """
- ► Preparation of flow diagrams, P&ID and calculation bases related to the implementation of treatment station (ET) projects.
- ► Energy efficiency studies applied to drying processes in copper leachate mining, contemplating energy baselines.
- ► Implementation of modular systems for the treatment of waste from the paper industry.
- ► Analysis of time series and evaluation of control systems in chemical plants.
- ► Implementation of computational intelligence models to improve the production of biogas from sugar industry waste.
"""
) 

# --- JOB 2
st.write('\n')
st.write("🚧", "**Development | Research Engineer**")
st.write("10/2021 - 02/2022")
st.write(
    """
- ► Process control according to regulations, reporting KPIs aligned with corporate requirements.
- ► Calculation and best operating cost lines of a high pressure boiler system.
- ► Implementation of cleaning operating curves for heat exchangers.
- ► Modeling of gas scrubber towers.

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Internship | Project Engineers**")
st.write("01/2021 - 04/2021")
st.write(
    """
- ► Modeling of a biomass boiler and evaluating energy cogeneration alternatives.
- ► Improvement in combustion quality to reduce atmospheric emissions.
- ► Preparation of flow charts of the various production stages to implement the TPM pillar.
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "**Assistant professor | Investigator**")
st.write("03/2018 - 03/2022")
st.write(
    """
- ► University teaching at the University of Santiago de Chile (USACH).
- ► Preparation of theoretical and didactic material for the disciplines of Environmental Engineering and Linear Algebra.
- ► Preparation of a joint project with students, focusing on industrial applications of sanitary engineering.
"""
)
