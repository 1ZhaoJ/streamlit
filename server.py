import http.server
import streamlit
import socketserver
import os  

PORT = 5500

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()


# 假设全景图文件在当前脚本所在的目录中的 'images' 文件夹内  
image_path = os.path.join( '微信图片_20240630102920 全景.jpg')  
  
# 获取当前脚本的目录路径  
script_dir = os.path.dirname(os.path.abspath(__file__))  
  
# 构建全景图的URL
url = f'http://localhost:5500/{os.path.relpath(image_path, script_dir)}'  
  
print(url)  # 输出全景图的URL

# 假设全景图文件在项目的static文件夹中  
panorama_image = '微信图片_20240630102920 全景.jpg'  
  
# 使用st.image()函数显示全景图  
st.image(panorama_image)