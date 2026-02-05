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
Hello! I am Min Min Htike. I am currently based in Saitama, Japan, and I am on a focused journey to become a professional Data Analyst. My goal is simple: To turn raw data into meaningful actions. Currently, I am actively building my technical skills in Python, Data Visualization, and Problem Solving.
This portfolio documents my progress as I turn my career ambitions into reality—one project at a time.
""")

st.write("---")
col1, col2, col3 = st.columns(3)
col1.metric("📍 Location", "Saitama, Japan")
col2.metric("🎓 Degree", "B.Sc")
col3.metric("💼 Status", "Open for Work")
tab1, tab2, tab3 = st.tabs(["🎓 Education", "🛠️ Skills", "📂 Projects"])

with tab1:
    st.subheader("Academic Background & Certifications")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏛️ University Degrees")
        st.write("📚 **B.Sc (Computer Science)**")
        st.caption("Yadanabon University, Mandalay")
        st.write("---")

        st.write("Foundation Diploma in Business and Information Technology")
        st.caption("Myanmar Management Institute, Yangon")
        st.write("---")

    with col2:
        st.subheader("📜 Professional Certifications")
        st.write("🇯🇵 NAT-TEST N3 Certified (N2 Level Proficiency)")
        st.caption("Advanced Business Level Proficiency")

        st.write("---")

        st.write("✅ **Pratical A+**")
        st.write("✅ **Advanced A+**") 
        st.write("✅ **Network Engineering**") 
        st.caption("PC repair and system maintenance, troubleshooting and computer errors")

with tab2:
    st.subheader("Technical Stack")
    col_a, col_b = st.columns(2)

    with col_a:
        st.write("**🐍 Python Analysis**")
        st.progress(85)
        st.caption("Pandas, NumPy, Matplotlib")
    
    with col_b:
        st.write("**📊 Data Visualization**")
        st.progress(80)
        st.caption("Streamlit, PowerBI, Tableau")

with tab3:
    st.info("🚧 More projects coming soon!")
    st.write("✅ **Sales Dashboard:** Built with Streamlit")
    st.write("✅ **Automation Scripts:** Python & Selenium")

st.markdown("---")
st.markdown("© 2026 Min Min Htike. All Rights Reserved.")