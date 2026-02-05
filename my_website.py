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
col_link1, col_link2 = st.sidebar.columns(2)

with col_link1:
    st.link_button("🔗 GitHub", "https://github.com/minhtike-tech")
    
with col_link2:
    st.link_button("👔 LinkedIn", "https://www.linkedin.com/in/minminhtike-data")
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

        st.write("🎓 **Foundation Diploma in Business & IT**")
        st.caption("Myanmar Management Institute, Yangon")

    with col2:
        st.subheader("📜 Professional Certifications")
        st.write("🇯🇵 NAT-TEST N3 Certified (N2 Level Proficiency)")

        st.markdown("---")

        st.write("**💻 IT & Networking**")
        st.write("✅ **Network Engineering**") 
        st.write("✅ **Advanced A+** (Hardware & System)")
        st.write("✅ **Practical A+** (Hands-on Training)")

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
    st.subheader("🧠 Soft Skills")
    st.write("✅ **Problem Solving** (Logical thinking & Troubleshooting)")
    st.write("✅ **Teamwork** (Experience working in diverse teams)")
    st.write("✅ **Adaptability** (Fast learner of new technologies)")

    st.write("---")

    st.subheader("🗣️ Language Proficiency")

    lang1, lang2, lang3 = st.columns(3)

    with lang1:
        st.info("🇲🇲 **Burmese** (Native)")

    with lang2:
        st.success("🇯🇵 **Japanese** (Business Level)")

    with lang3:
        st.warning("🇬🇧 **English** (Intermediate)")

with tab3:
    st.subheader("📂 My Projects")
    
    with st.expander("📊 Sales Dashboard (Streamlit & Python)"):
        st.write("**Technologies:** Python, Pandas, Streamlit, Plotly")
        st.write("**Description:**")
        st.write("""
        - Created an interactive dashboard to visualize sales data.
        - Analyzed monthly trends and top-selling products.
        - Helped business owners make data-driven decisions.
        """)
        #st.link_button("👉 View Code on GitHub", "https://github.com/minhtike-tech") # Link မရှိရင် ခဏဖြုတ်ထားလို့ရ

    with st.expander("🤖 Automation Tool (Python & Selenium)"):
        st.write("**Technologies:** Python, Selenium, ChromeDriver")
        st.write("**Description:**")
        st.write("""
        - Automated repetitive tasks such as filling forms and downloading reports.
        - Reduced manual work time by 40%.
        """)

    with st.expander("🧹 Data Cleaning Project"):
        st.info("🚧 Currently working on this project...")
        st.write("---")
    
st.markdown("---")
st.markdown("© 2026 Min Min Htike. All Rights Reserved.")