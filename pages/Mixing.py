import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from streamlit import components
from streamlit.components.v1 import html


st.set_page_config(
    page_title="搅拌",
    page_icon=":pencil:",
    layout="wide",
)

st.write("## 搅拌站监控")

st.write("1. 混凝土原材料组分（kg）")
st.write(pd.DataFrame({
    '细骨料-河砂': [1,2,3,4],
    '粗骨料-碎石': [10,20,30,40],
    '水泥': [100,200,300,400],
    '外加剂-减水剂': [10,20,30,40]}
))

# 创建一个自定义 Streamlit 组件显示全景图
st.markdown("### Interactive Panorama Viewer")

# 嵌入 HTML 和 JavaScript 代码以显示全景图
html_code = """
<iframe width="1000" height="500" allowfullscreen style="border:none;" src="https://realsee.cn/awWW9ObR"></iframe>
"""
st.markdown(html_code, unsafe_allow_html=True)




html_code = """
<iframe width="1000" height="500" allowfullscreen style="border:none;" src="http://127.0.0.1:5500/pythonProject6/quanjing.html"></iframe>
"""
st.markdown(html_code, unsafe_allow_html=True)




# 5.
st.write("5. image")
image = Image.open(r"C:\Users\ZhaoJ\Desktop\888\u=2910264715,818630913&fm=253&fmt=auto&app=138&f=JPEG.webp")
st.image(image, caption='混凝土搅拌站',
         use_column_width=True)