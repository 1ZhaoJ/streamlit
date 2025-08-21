import streamlit as st

def main():
    st.title("三维全景图展示")

    # 在这里替换为你的HTML文件路径
    html_file = "quanjing.html"

    # 读取HTML文件内容
    with open(html_file, 'r', encoding="utf-8") as f:
        html_content = f.read()

    # 在Streamlit应用中显示HTML内容
    st.components.v1.html(html_content, height=600)

if __name__ == "__main__":
    main()
