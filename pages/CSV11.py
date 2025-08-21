import streamlit as st
import pandas as pd
import chardet
import matplotlib.pyplot as plt

st.title('CSV 文件上传和处理示例')

# 创建一个侧边栏部件，用于上传文件
uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

if uploaded_file is not None:
    rawdata = uploaded_file.getvalue()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    # 使用 pandas 读取上传的文件
    df = pd.read_csv(uploaded_file, encoding=encoding)

    st.success("上传文件成功！")

    x_var = st.selectbox(
        label="选择横坐标的属性",
        options=df.columns
    )
    y_var = st.selectbox(
        label="选择纵坐标的属性",
        options=df.columns
    )

    # 根据用户选择的属性创建图表数据
    chart_data = pd.DataFrame({x_var: df[x_var], y_var: df[y_var]})

    st.write("生成的图表数据:")
    st.write(chart_data)

    # 绘制折线图，每个'design_strength'种类对应不同颜色的线
    if 'design_strength' in df.columns:
        plt.figure(figsize=(10, 6))
        grouped_data = df.groupby('design_strength')
        for key, group in grouped_data:
            plt.plot(group[x_var], group[y_var], label=f"Category: {key}")
        plt.xlabel(x_var)
        plt.ylabel(y_var)
        plt.title("Line Chart with Different 'design_strength' Categories")
        plt.legend()
        st.pyplot(plt)
    else:
        st.warning("未找到'design_strength'列。请上传包含'design_strength'列的CSV文件。")