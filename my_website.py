import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Min Min Htike's Portfolio", 
    page_icon="📊",
    layout="wide"
)

with st.sidebar:
    st.image("my_photo.jpg", width=150)
    st.title("📬 Contact Info")
    st.write("📍 **Address**")
    st.caption("Irumashi, Saitama ken, Japan")
    st.markdown("---")
    st.write("📧 **Email**")
    st.markdown("[mht.minhtike@gmail.com](mailto:mht.minhtike@gmail.com)")
    st.write("📱 **Phone**")
    st.markdown("[070-8940-4565](tel:07089404565)")
    st.markdown("---")
    st.link_button("🔗 GitHub Profile", "https://github.com/minhtike-tech")
st.title("Min Min Htike 👨‍💻")
st.subheader("🚀 Aspiring Data Analyst | Portfolio")
st.write("""
Hello! I am Min Min Htike. I am currently based in Saitama, Japan, and I am on a focused journey to become a professional Data Analyst.  
My goal is simple: To turn raw data into meaningful actions. Currently, I am actively building my technical skills in Python, Data Visualization, and Problem Solving.
This portfolio documents my progress as I turn my career ambitions into reality—one project at a time.
""")

st.markdown("---") 

st.header("🎓 Education & Qualifications")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏫 University Degrees")
    st.write("👉 **B.Sc (Computer Science)** - [Yadanabon University]")
    st.write("👉 **Foundation Diploma in Business and Information Technology** - [Myanmar Management Institute]")

with col2:
    st.subheader("📜 Certifications")
    st.write("👉 **JLPT N2** (Japanese Language Proficiency Test)")
    st.write("👉 **Network Course:** Pratical A+ / Advanced A+ / Network Engineering")
    st.write("👉 **Python for Data Analysis:** Self-Study Project (2025-Present)")

st.markdown("---")

st.header("🛠 Professional Skills")

st.write("##### 💻 Programming & Tech")
st.progress(80) 
st.caption("Python (Pandas, NumPy, Matplotlib)")

st.write("##### 📊 Data Visualization")
st.progress(70)
st.caption("Streamlit, Excel, Charts")

st.write("##### 🌐 Networking")
st.progress(75)
st.caption("Network Infrastructure, Troubleshooting")

st.write("##### 🗣 Languages")
st.success("🇯🇵 Japanese (Business Level / N2)")
st.info("🇲🇲 Burmese (Native)")
st.warning("🇬🇧 English (Intermediate)")

st.markdown("---")

st.header("📈 Sample Data Visualization")
st.write("ဒါကတော့ Python သုံးပြီး Random Data တွေကို ချက်ချင်း ပုံဖော်ထားတာ ဖြစ်ပါတယ်။")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Sales', 'Income', 'Expenses']
)

st.area_chart(chart_data)

st.markdown("---")
st.markdown("© 2026 Min Min Htike. All Rights Reserved.")