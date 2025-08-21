import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(
    page_title="浇筑",
    page_icon=":pencil:",
    layout="wide",
)

st.write("## 浇筑台车监控")





# 创建三维数据
data = np.random.rand(3, 100)

# 创建一个新的 matplotlib 图表
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制三维散点图
ax.scatter(data[0], data[1], data[2])

# 显示图表
st.write(fig)



# 2. st.line_chart()
st.write("2. st.line_chart()")
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['含水率','质量','体积']
)
st.line_chart(chart_data)

