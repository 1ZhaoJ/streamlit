import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sizes = [30, 40, 20, 10]
label_names = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()
ax.pie(sizes, labels=label_names, autopct='%1.1f%%')
ax.axis('equal')

st.pyplot(fig)

uploaded_file = st.file_uploader("上传 CSV 文件", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("上传文件成功！")
else:
    st.stop()

x_var = st.selectbox(
    label="选择横坐标的属性",
    options=['bill_length_mm', 'bill_depth_mm','flipper_length_mm','body_mass_g',]
)
y_var = st.selectbox(
    label="选择纵坐标的属性",
    options=['bill_length_mm', 'bill_depth_mm','flipper_length_mm','body_mass_g',]
)

sns.set_style("darkgrid")
markers={'Adelie':'s',
         'Gentoo':'x',
         'Chinstrap':'o'
         }
fig,ax=plt.subplots()
ax=sns.scatterplot(data=df,
                   x=x_var,
                   y=y_var,
                   hue='species',
                   style='species')
plt.xlabel(x_var)
plt.xlabel(y_var)
plt.title('Plot')
st.pyplot(fig)