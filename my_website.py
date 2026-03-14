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
    st.link_button("👔 LinkedIn", "https://www.linkedin.com/in/minminhtike-tech")
st.title("Min Min Htike 👨‍💻")
st.subheader("🚀 Junior Data Analyst | Portfolio")
st.write("""
Hello! I am Min Min Htike. I am currently based in Saitama, Japan, and I am on a focused journey to become a professional Data Analyst. My goal is simple: To turn raw data into meaningful actions. Currently, I am actively building my technical skills in Python, Data Visualization, and Problem Solving.
This portfolio documents my progress as I turn my career ambitions into reality—one project at a time.
""")

st.write("---")
col1, col2, col3 = st.columns(3)
col1.metric("📍 Location", "Saitama, Japan")
col2.metric("🎓 Degree", "B.Sc(CS)")
col3.metric("💼 Status", "Open for Work")
tab1, tab2, tab3 = st.tabs(["🎓 Education", "🛠️ Skills", "📂 Projects"])

with tab1:
    st.subheader("Academic Background & Certifications")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏛️ University Degrees")
        st.write("📚 **B.Sc (Computer Science)**")
        st.caption("Yadanabon University, Mandalay, Myanmar")

        st.write("🎓 **Foundation Diploma in Business & IT**")
        st.caption("Myanmar Management Institute, Yangon, Myanmar")

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

        st.write("**🗄️ SQL (Database)**")
        st.progress(75)
        st.caption("MySQL, PostgreSQL, Query Optimization")
    
    with col_b:
        st.write("**📊 Data Visualization**")
        st.progress(80)
        st.caption("Streamlit, PowerBI, Tableau")

        st.write("**📗 Excel & Spreadsheets**")
        st.progress(90) 
        st.caption("Pivot Tables, VLOOKUP, Macros")
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
    
    with st.expander("🚢 Titanic Survival Analysis (Python)"):
        st.write("**Technologies:** Python, Pandas, Seaborn, Matplotlib")
        st.write("**Description:**")
        st.write("""
        My first Data Analysis project using Python to explore and understand survival patterns from the Titanic dataset.
        - Data Cleaning: Handled missing age data using Median Imputation to ensure analysis accuracy.
        - Survival Analysis: Discovered key insights on how age and gender influenced survival chances, noting that young adult males were the most impacted group.
        - Family Dynamics: Analyzed the relationship between family size and survival probability.
        - Visualizations: Created clear distribution plots and bar charts to communicate findings effectively.
        """)
        st.link_button("👉 View Code on GitHub", "https://github.com/minhtike-tech/titanic-data-analysis") 

    with st.expander("🎬 Netflix Content Trends Analysis (Python)"):
        st.write("**Technologies:** Python, Pandas, Matplotlib, Seaborn")
        st.write("**Description:**")
        st.write("""
        An Exploratory Data Analysis (EDA) project on the Netflix dataset to uncover content strategies and streaming trends.
        - **Content Ratio:** Discovered that Movies significantly outnumber TV Shows on the platform.
        - **Global Insights:** Identified the United States as the leading producer, followed by India and the UK.
        - **Movie Durations:** Analyzed that the average Netflix movie duration is approximately 99 minutes.
        - **Growth Trends:** Documented a massive surge in content production starting from 2014, peaking in 2018-2019.
        """)
        st.link_button("👉 View Code on GitHub", "https://github.com/minhtike-tech/Netflix-Data-Analysis")

    with st.expander("🗼 Tokyo Airbnb Data Analysis (Python, SQL, Power BI)"):
        st.write("**Technologies:** Python, Pandas, SQLite, Power BI")
        st.write("**Description:**")
        st.write("""
        An end-to-end data pipeline project uncovering popular neighborhoods, budget-friendly hotspots, and VIP guests in Tokyo.
        - **The Ultimate Hotspot:** Identified Shinjuku Ku as the undisputed most popular neighborhood by guest reviews.
        - **Hidden Gems:** Discovered Taito Ku and Sumida Ku as highly sought-after, budget-friendly areas for tourists.
        - **Customer Retention:** Extracted the "Top 10 Most Loyal Customers" using SQL aggregations for potential VIP targeting.
        """)
        st.link_button("👉 View Code on GitHub", "https://github.com/minhtike-tech/Tokyo-Airbnb-Data-Analysis")
    
st.markdown("---")
st.markdown("© 2026 Min Min Htike. All Rights Reserved.")
