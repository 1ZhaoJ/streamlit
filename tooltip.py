import streamlit as st  
  
# 带有tooltip的HTML内容  
html_content = """  
<style>  
.tooltip {  
    position: relative;  
    display: inline-block;  
    border-bottom: 1px dotted black;  
}  
  
.tooltip .tooltiptext {  
    visibility: hidden;  
    width: 120px;  
    background-color: #555;  
    color: #fff;  
    text-align: center;  
    border-radius: 6px;  
    padding: 5px 0;  
    position: absolute;  
    z-index: 1;  
    bottom: 100%;   
    left: 50%;   
    margin-left: -60px;  
    opacity: 0;  
    transition: opacity 0.3s;  
}  
  
.tooltip:hover .tooltiptext {  
    visibility: visible;  
    opacity: 1;  
}  
</style>  
  
<div class="tooltip">Hover over me  
  <span class="tooltiptext">This is a tooltip text</span>  
</div>  
"""  
  
# 在Streamlit中嵌入HTML内容  
st.markdown(html_content, unsafe_allow_html=True)