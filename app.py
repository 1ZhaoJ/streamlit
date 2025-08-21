# streamlit run c:\Software\project\pyserial_mysql_streamlit\pythonProject6\app.py [ARGUMENTS]

import streamlit as st

# 创建侧边栏导航
page = st.sidebar.selectbox("Page", ["Home", "About", "Contact"])

# 根据所选页面显示不同内容
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page!")
elif page == "About":
    st.title("About Page")
    st.write("This is the about page.")
elif page == "Contact":
    st.title("Contact Page")
    st.write("Contact us at contact@example.com")