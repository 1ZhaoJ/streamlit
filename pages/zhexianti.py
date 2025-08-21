import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("上传CSV文件", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    st.write(df)
    st.success("上传文件成功！")
else:
    st.stop()

x_var = st.selectbox(
    label="选择横坐标的属性",
    options=['DATA', 'STRENGTH']
)
y_var = st.selectbox(
    label="选择纵坐标的属性",
    options=['DATA', 'STRENGTH']
)

sns.set_style("darkgrid")
markers = {'c15': 's', 'c30': 'o'}

fig, ax = plt.subplots()
ax = sns.lineplot(data=df, x=x_var, y=y_var, hue='design_strength', style='design_strength')
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('混凝土试块强度')
st.pyplot(fig)