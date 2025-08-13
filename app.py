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
Chemical Engineer with an MSc in Computational Mechanics, offering specialized consultancy services in modeling, simulation, and process optimization. I have solid experience in environmental project management, process innovation, and advanced computational simulations. Currently, I lead environmental sanitation projects at Destra, managing teams, prioritizing tasks, and solving technical challenges, while developing process diagrams, technical documentation, and construction plans for industrial effluent treatment plants, including aerobic systems, dissolved air flotation (DAF), and membrane technologies. I have contributed to the successful implementation of leachate treatment plants and am developing patentable technologies aimed at nutrient recovery.
"""
SUBTITLE="Digital CV | FELIPE IGNACIO MUNHOZ TOLEDO"

EMAIL = "felipe.toledo@coc.ufrj.br"

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/felipemunoztoledo",
    "GitHub": "https://github.com/felipe77-CH",
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide",initial_sidebar_state="auto")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="small") 

with col1:
    st.image(profile_pic, width=300)


with col2:
    st.title(NAME)
    st.markdown("<h4 style='font-size:22px;'>MSc. Computational Mechanics | Process Modeling & Optimization | Data Scientist</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify;'>{DESCRIPTION}</p>", unsafe_allow_html=True)

    # Cuatro botones en la misma fila
    btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4) # gap pequeño para acercarlos

    with btn_col1:
        st.download_button(
            label="📄 Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )

    with btn_col2:
        st.markdown(
            """
            <a href='https://github.com/felipe77-CH' target='_blank'>
                <button style='padding:8px 16px; font-size:16px; border-radius:5px; border:none; background-color:#333333; color:white; cursor:pointer;'>🐙 GitHub</button>
            </a>
            """,
            unsafe_allow_html=True
        )

    with btn_col3:
        st.markdown(
            """
            <a href='https://www.linkedin.com/in/felipemunoztoledo' target='_blank'>
                <button style='padding:8px 16px; font-size:16px; border-radius:5px; border:none; background-color:#0077B5; color:white; cursor:pointer;'>💼 LinkedIn</button>
            </a>
            """,
            unsafe_allow_html=True
        )

    with btn_col4:
        st.markdown(
            """
            <a href='mailto:felipe.toledo@coc.ufrj.br'>
                <button style='padding:8px 16px; font-size:16px; border-radius:5px; border:none; background-color:#28A745; color:white; cursor:pointer;'>✉️ Email</button>
            </a>
            """,
            unsafe_allow_html=True
        )



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
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, NumPy, TensorFlow, PyTorch), C++, SQL, Matlab
- 📊 Data Visualization: Power BI, MS Excel, Matplotlib, Seaborn
- 📚 Machine Learning & AI: Logistic Regression, Linear Regression, Decision Trees, Random Forest, Neural Networks, Deep Learning
- 🗄️ Databases & Cloud: MySQL, PostgreSQL, AWS (S3, EC2, SageMaker)
- ⌨️ Tools & Platforms: Git, Jupyter, VS Code, Docker
- ⚙️ Process Modeling: HYSYS, DWSIM
- 🌊 Fluid Dynamics Simulations: OpenFOAM, Ansys (CFX & Fluent)
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- 🎓 **MSc. Computational Mechanics**, Federal University of Rio de Janeiro (UFRJ/COPPE)
- 🎓 **BSc. Chemical Engineering**, University of Santiago de Chile (USACH)
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
