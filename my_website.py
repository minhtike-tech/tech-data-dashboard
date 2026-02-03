import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration (ခေါင်းစဉ်နဲ့ Icon)
st.set_page_config(
    page_title="Min Min Htike's Portfolio", 
    page_icon="📊",
    layout="wide"
)

# 2. Sidebar (ဘေးက အကွက်)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.header("Contact Info")
st.sidebar.info("📍 Irumashi, Saitama ken, Japan")
st.sidebar.text("📧 mht.minhtike@gmail.com") # မင်းအီးမေးလ် အမှန်ထည့်ပါ
st.sidebar.text("📱 070-8940-4565")

# 3. Main Title (အဓိက ခေါင်းစဉ်)
st.title("👨‍💻 Data Analyst Portfolio")
st.subheader("Min Min Htike")
st.write("""
မင်္ဂလာပါ! ကျွန်တော်ကတော့ Japan မှာ နေထိုင်ပြီး Data Analysis ကို လေ့လာနေသူ တစ်ဦးဖြစ်ပါတယ်။ 
Python, Data Visualization နဲ့ Business Insights တွေကို စိတ်ဝင်စားပါတယ်။
""")

st.markdown("---") # မျဉ်းတစ်ကြောင်းတားမယ်

# 4. Education & Certifications (ပညာရေးနှင့် သင်တန်းများ)
st.header("🎓 Education & Qualifications (ပညာအရည်အချင်း)")

# Column ၂ ခု ခွဲလိုက်မယ် (ကြည့်လို့ ပိုလှအောင်)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏫 University Degrees")
    st.write("👉 **B.Sc (သို့) သက်ဆိုင်ရာဘွဲ့** - [တက္ကသိုလ်အမည်]")
    st.write("👉 **Diploma in Network Engineering** - [ကျောင်းအမည်]")

with col2:
    st.subheader("📜 Certifications")
    st.write("👉 **JLPT N2** (Japanese Language Proficiency Test)")
    st.write("👉 **Network Course:** CCNA / Network+ (ပြီးခဲ့သည့် သင်တန်းများ)")
    st.write("👉 **Python for Data Analysis:** Self-Study Project (2025-Present)")

st.markdown("---")

# 5. Skills (ကျွမ်းကျင်မှုများ)
st.header("🛠 Professional Skills")

st.write("##### 💻 Programming & Tech")
st.progress(80) # Progress Bar လေးနဲ့ ပြမယ်
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

# 6. Sample Projects (လက်တွေ့ ပရောဂျက်များ)
st.header("📈 Sample Data Visualization")
st.write("ဒါကတော့ Python သုံးပြီး Random Data တွေကို ချက်ချင်း ပုံဖော်ထားတာ ဖြစ်ပါတယ်။")

# Chart Data အစစ်ဆောက်မယ်
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Sales', 'Income', 'Expenses']
)

# Area Chart နဲ့ ပြရင် ပိုလှတယ်
st.area_chart(chart_data)

# 7. Footer
st.markdown("---")
st.markdown("© 2026 Min Min Htike. All Rights Reserved.")