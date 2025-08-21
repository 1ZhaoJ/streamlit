import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager  # 添加这一行以导入 font_manager
from matplotlib.font_manager import FontProperties
import plotly.express as px

# # 使用 CSS 自定义上传组件的大小
# st.markdown("""
#     <style>
#     .stFileUploader {
#         width: 100px;  /* 设置宽度 */
#         height: 500px;  /* 设置高度 */
#         border-radius: 5px;  /* 可选：设置圆角 */
#         padding: 10px;  /* 可选：设置内边距 */
#         text-align: center;  /* 可选：文本居中对齐 */
#         background-color: #f0f0f0;  /* 可选：背景颜色 */
#     }
#     </style>
# """, unsafe_allow_html=True)

# # 使用 CSS 调整列的边距和间距
# st.markdown("""
#     <style>
#     .stAPP {
#         margin: 10px;  /* 设置列和页面边缘的间距 */
#     }
#     </style>
# """, unsafe_allow_html=True)

# 指定中文字体
font_path = 'C:\Windows\Fonts\STSONG.ttf'  # 替换为你的中文字体路径
font_prop = font_manager.FontProperties(fname=font_path)
# 使用容器来包装列
with st.container():
    st.markdown("<br>", unsafe_allow_html=True)  # 添加一些额外的空间
    # 创建两个列
    col1, spacer, col2 = st.columns([3, 0.5, 3,])

    # 第一列：上传 CSV 用于饼图
    with col1:
        # 上传 csv 文件
        uploaded_file1 = st.file_uploader("上传饼图：生产品种分布 csv 文件", type=['csv'])

        # 确保文件被上传
        if uploaded_file1 is not None:
            try:
                # 读取 csv 文件
                data1 = pd.read_csv(uploaded_file1)

                # 移除列名中的多余空格
                data1.columns = data1.columns.str.strip()
                # 确保 dataframe 中有需要的列
                if 'values' in data1.columns and 'labels' in data1.columns:
                    # 创建饼图
                    fig1, ax1 = plt.subplots(figsize=(8, 5))
                    ax1.pie(data1['values'], labels=data1['labels'], autopct='%1.1f%%', startangle=90)
                    ax1.axis('equal')  # 保证饼图是圆形
                    # 在饼图中央显示一段文字
                    plt.title("今日总产量为185吨（t）", fontproperties=font_prop, fontsize=12, fontweight='bold')
                    # 显示饼图
                    st.pyplot(fig1)

                else:
                    st.warning("csv 文件中需要包含 'values' 和 'labels' 列。可用列为：" + ", ".join(data1.columns))

            except Exception as e:
                st.error(f"读取文件时发生错误: {e}")
    with col2:
        uploaded_file = st.file_uploader("上传折线图：每小时生产方量CSV文件", type=['csv'])

        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file, encoding='utf-8')
        else:
            st.stop()
        # 假设数据中有 '时间' 列和不同生产线的列
        if '时间' in data.columns and '1号生产线' in data.columns and '2号生产线' in data.columns:
            font_prop = FontProperties(fname='C:\Windows\Fonts\STSONG.ttf')
            # 绘制折线图
            plt.figure(figsize=(8, 5))

            # 绘制生产线1
            plt.plot(data['时间'], data['1号生产线'], marker='s', label='Production Line No.1')

            # 绘制生产线2
            plt.plot(data['时间'], data['2号生产线'], marker='o', label='Production Line No.2')
            plt.title('每小时生产方量',fontproperties=font_prop, fontsize=12, fontweight='bold')
            plt.xlabel('时间',fontproperties=font_prop, fontsize=12, fontweight='bold')
            plt.ylabel('生产方量',fontproperties=font_prop, fontsize=12, fontweight='bold')
            plt.xticks(rotation=0)  # 旋转x轴标签以便于阅读
            plt.legend()  # 添加图例
            plt.grid()

            # 显示图形
            st.pyplot(plt)
        else:
            st.error("数据中应包含 '时间' 列以及以 '生产线' 开头的列。")

    # with col3:
    #     uploaded_file = st.file_uploader("上传折线图CSV文件", type=['csv'])

    #     if uploaded_file is not None:
    #         df = pd.read_csv(uploaded_file, encoding='utf-8')
    #     else:
    #         st.stop()

    #     x_var = 'data'
    #     y_var = 'strength'
    #     sns.set_style("darkgrid")
    #     markers = {'c15': 's', 'c30': 'o'}

    #     fig, ax = plt.subplots(figsize=(3, 3))
    #     ax = sns.lineplot(data=df, x=x_var, y=y_var, hue='design_strength', style='design_strength')
    #     plt.xlabel(x_var)
    #     plt.ylabel(y_var)
    #     plt.title('The strength of concrete test block')
    #     st.pyplot(fig)

uploaded_file = st.file_uploader("上传折线图：混凝土试块抗压强度csv文件", type=['csv'])
# 确保文件被上传
if uploaded_file is not None:
    # 读取 CSV 文件
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    # 检查数据至少有两列
    if df.shape[1] > 1:  # 至少需要两列
        # 假设第一列是 x 值，其他列是 y 值
        y = df.iloc[:, 1:]  # y 轴数据（多个列）
        # 将 x 列设置为索引
        plot_data = df.set_index(df.columns[0])  # 使用第一列作为索引

        # 使用 Plotly 绘制折线图
        fig = px.line(plot_data, title='混凝土试块抗压强度折线图')
        fig.update_layout(
            xaxis_title=df.columns[0],  # x 轴标题
            yaxis_title='抗压强度(MPa)',  # y 轴标题
            xaxis_tickangle=0  # 旋转 x 轴标签
        )
        st.plotly_chart(fig)  # 展示 Plotly 图表

    else:
        st.warning("数据中需要至少两列，以便绘制折线图。")

col1, col2 = st.columns([3, 3])
with col1:
        uploaded_file = st.file_uploader("上传表格文件", type=['csv'])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file, encoding='utf-8')
            st.dataframe(df, width=700, height=300)  # 您可以根据需要调整宽度和高度
        else:
            st.stop()
        # 上传文件的组件
with col2:
    # 上传文件的组件
    uploaded_file = st.file_uploader("上传柱状图:材料数据 csv 文件", type=['csv'], key="uploader_1")
    # 确保文件被上传
    if uploaded_file is not None:
        # 读取 csv 文件
        df = pd.read_csv(uploaded_file, encoding='utf-8')

        # 检查数据至少有两列
        if df.shape[1] > 1:
            x = df.iloc[:, 0]  # x 轴数据
            y = df.iloc[:, 1:]  # y 轴数据

            # 确保 y 数据是数值类型
            y = y.apply(pd.to_numeric, errors='coerce')  # 转换为数值，无法转换的设置为 nan

            # 将 x 和 y 结合
            plot_data = pd.DataFrame(data=y.values, index=x.values, columns=y.columns)

            # 使用 Plotly 绘制柱状图
            fig = px.bar(plot_data, x=plot_data.index, y=plot_data.columns, 
                        title='材料进耗存统计',  
                        width=700,  # 设置宽度
                        height=350)  # 设置高度
            fig.update_layout(xaxis_tickangle=0,# 旋转 x 轴标签
            xaxis_title='',  # 取消横坐标标题
            yaxis_title='单位（t）',  # 将纵坐标标题设置为 't'
            ) 
            st.plotly_chart(fig)  # 确保在这里调用 st.plotly_chart()
        else:
            st.warning("数据中需要至少两列，以便绘制图表。")
    
uploaded_file = st.file_uploader("上传折线图：温度csv文件", type=['csv'], key="uploader_9")
# 确保文件被上传
if uploaded_file is not None:
    # 读取 CSV 文件
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    if df.shape[1] > 1:  # 至少需要两列
        # 假设第一列是 x 值，其他列是 y 值
        y = df.iloc[:, 1:]  # y 轴数据（多个列）
        # 将 x 列设置为索引
        plot_data = df.set_index(df.columns[0])  # 使用第一列作为索引
        # 使用 Plotly 绘制折线图
        fig = px.line(plot_data, title='温度')
        fig.update_layout(
                xaxis_title=df.columns[0],  # x 轴标题
                yaxis_title='温度变化',  # y 轴标题
                xaxis_tickangle=0  # 旋转 x 轴标签
            )
        st.plotly_chart(fig)  # 展示 Plotly 图表
    else:
        st.warning("数据中需要至少两列，以便绘制折线图。")


# col1, spacer, col2 = st.columns([3, 0.5, 3])
# with col1:
#     uploaded_file = st.file_uploader("上传CSV文件", type=['csv'], key="uploader_2")

#     # 确保文件被上传
#     if uploaded_file is not None:
#         # 读取 CSV 文件
#         df = pd.read_csv(uploaded_file, encoding='utf-8')
#         # 确保 DataFrame 中有数值的列以便绘制折线图
#         # 这里假设第一列是 x 轴，其他列是 y 轴
#         if df.shape[1] > 1:  # 至少需要两列
#             # 假设第一列是 x 值，其他列是 y 值
#             x = df.iloc[:, 0]  # x 轴数据
#             y = df.iloc[:, 1:]  # y 轴数据（多个列）
#             df.set_index(df.columns[0], inplace=True)
#             # 使用 st.line_chart 绘制折线图
#             st.line_chart(y)

#         else:
#             st.warning("数据中需要至少两列，以便绘制折线图。")

# with col2:
#     # 上传文件的组件
#     uploaded_file = st.file_uploader("上传区域图csv文件", type=['csv'], key="uploader_3")
#     # 确保文件被上传
#     if uploaded_file is not None:
#         # 读取 CSV 文件
#         df = pd.read_csv(uploaded_file, encoding='utf-8')
#         # 这里假设第一列是 x 轴，其他列是 y 轴
#         if df.shape[1] > 1:  # 至少需要两列
#             # 假设第一列是 x 值，其他列是 y 值
#             x = df.iloc[:, 0]  # x 轴数据
#             y = df.iloc[:, 1:]  # y 轴数据（多个列）

#             # 使用 st.line_chart 绘制折线图
#             st.area_chart(y)

#         else:
#             st.warning("数据中需要至少两列，以便绘制折线图。")




# 上传文件的组件
uploaded_file = st.file_uploader("上传柱状图 csv 文件", type=['csv'], key="uploader_7")

# 确保文件被上传
if uploaded_file is not None:
    # 读取 csv 文件
    df = pd.read_csv(uploaded_file, encoding='utf-8')

    # 检查数据至少有两列
    if df.shape[1] > 1:
        # 假设第一列是 x 轴，其他列是 y 轴
        x = df.iloc[:, 0]  # x 轴数据
        y = df.iloc[:, 1:]  # y 轴数据（多个列）
        # 确保 y 数据是数值类型
        y = y.apply(pd.to_numeric, errors='coerce')  # 转换为数值，无法转换的设置为 NaN
        # 将 x 和 y 组合成一个新的 DataFrame
        plot_data = pd.DataFrame(data=y.values, index=x.values, columns=y.columns)
        # 使用 st.area_chart 绘制区域图
        st.area_chart(plot_data)
    else:
        st.warning("数据中需要至少两列，以便绘制图表。")
else:
    st.info("请上传一个 csv 文件。")