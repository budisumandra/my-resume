from pathlib import Path
import streamlit as st
from PIL import Image

# ---- PATH SETTINGS ----
current_dir = Path(__name__).parent if '__file__' in locals() else Path.cwd() 
css_file = current_dir/ "styles" / "main.css"
cv_file = current_dir/ "assets" / "myCV.pdf"
my_profile = current_dir/ "assets" / "Image1.jpeg"

# ---- GENERAL SETTINGS ----
PAGE_TITLE = "DIGITAL CV | SETIA BUDI SUMANDRA"
PAGE_ICON = ':smiley:'
NAME = "SETIA BUDI SUMANDRA S.Si"
DESCRIPTION = "Junior Data Scientist, build descriptive and predictive analysis to support decision-making"
EMAIL = 'budisumandra325@gmail.com'
SOCIAL_MEDIA = {
    "Medium": "https://medium.com/@budisumandra",
    "LinkedIn": "https://www.linkedin.com/in/setia-budi-sumandra-42b992213/",
    "GitHub": "https://github.com/budisumandra",
    "Instagram": "https://www.instagram.com/budisumandra/"
}
PROJECTS = {
    "🏆 Car Price Prediction" : "https://budisumandra-car-price-prediction-app-dcl6dw.streamlit.app/",
    "🏆 Deploy Water Potability with Flask" : "https://github.com/budisumandra/PotabilityDeploy_Flask",
    "🏆 Handwritten Digit Prediction with GaussianNB Algorihtm" : "https://github.com/budisumandra/handwritten_GaussianNB",
    "🏆 Water Potability Prediction with Tress|XGBoost Algorithm" : "https://github.com/budisumandra/water_potability_Trees-XGBoost",
    "🏆 Water Potability Prediction": "https://budisumandra-water-potability-prediction-app-625p0w.streamlit.app/",
    "🏆 Visual Analysis of Airbnb New York Dataset":"https://medium.com/@budisumandra/performed-visual-analysis-to-airbnb-new-york-dataset-using-barplot-pie-chart-catplot-and-map-406390afaa88",
    "🏆 Array/Ndarrays with Numpy":"https://medium.com/@budisumandra/numpy-multiple-options-for-creating-array-ndarrays-tensors-with-numpy-b6cedc76fd9b",
    "🏆 EDA Water Potability Analysis":"https://medium.com/@budisumandra/performing-exploratory-data-analysis-eda-through-visualization-techniques-to-analyze-water-203feaa04a19",
    "🏆 Mall Customers Segmentation with K-Means":"https://medium.com/@budisumandra/mall-customers-segmentation-with-k-means-clustering-algorithm-in-python-55ba10e4bbe3",
    "🏆 Tokyo 2020 Olympic Athlete Analysis":"https://medium.com/@budisumandra/tokyo-2020-olympic-athlete-dataset-visualization-and-analysis-a-case-study-of-using-matplotlib-and-fd4e79850811"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# ---- LOAD CSS, PDF, AND PROFILE PICT ----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(cv_file, 'rb') as cv:
    PDFbyte = cv.read()
profile_pic = Image.open(my_profile)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=cv_file.name,
        mime="application/octet-stream",
        )
    st.write("📫", EMAIL)

# ---- SOCIAL MEDIA SECTION ----
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[i].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader('Experience and Qualifications')
st.write("---")
st.write(
        """
    - ✔️ Has 6 months internship experience in the field of Data Science at PT Solusi 247 (NLP Project Field)
    - ✔️ Medium level on experience and knowledge in Python and RDBMS (SQL & MySQL)
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Easy to adapt to new things and can work under pressure
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
        """
    - 👩‍💻 Programming: Python (Scikit-learn, Keras & Tensorflow, Pandas, Streamlit, Matplotlib, Seaborn), Shell Script, Java Script, HTML & CSS, Bootstrap & JQUERY\n
    - 📚 Modeling: Linear regression, Logistic Regression, Decision Trees, SVM, K-Means, Deep Learning\n
    - 🗄️ Databases: SQL, MySQL
    """
    )


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Support Developer | PT Solusi 247**")
st.write("09/2021 - Present")
st.write(
        """
    - ► Used Shell Script and SQL/MySQL
    - ► Provide and Pivot data with MS.Excel from SQL/MySQL Database and sometimes it dumps the data via a server using a shell script to the Telegram Bot
    """
)

# --- SKILLS ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.markdown(
        """
        2016 - 2020\n
    - 📚 **Bachelor Degree**: Physics Department | FMIPA Gadjah Mada University (UGM)
    """
    )

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
