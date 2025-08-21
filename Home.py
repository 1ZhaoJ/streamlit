#  streamlit run c:\Software\project\pyserial_mysql_streamlit\pythonProject6\Home.py [ARGUMENTS]
import pandas as pd
import numpy as np

import streamlit as st
import datetime
import time
import matplotlib.pyplot as plt
import matplotlib

st.set_page_config(
    page_title="混凝土全过程质量监控",
    page_icon=":world_map:️",
    layout="wide",
)



# 显示静态内容
st.write("## 欢迎使用混凝土全过程质量监控应用程序！")
st.write("这里可以放一些文本、图表或其他内容")


txt = st.text_area('Text to analyze', '''
     I(...)
     ''', height=200)
st.write('Sentiment:')

matplotlib.rc("font", family='AR PL UMing CN')


time_container = st.sidebar.empty()


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x

while True:
    current_time = datetime.datetime.now()
    time_container.write("当前时间是: {}".format(current_time.strftime("%H:%M:%S")))
    time.sleep(1)









