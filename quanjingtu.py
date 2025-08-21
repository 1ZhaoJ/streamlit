
import os  
  
# 假设全景图文件在当前脚本所在的目录中的 'images' 文件夹内  
image_path = os.path.join('images', 'panorama.jpg')  
  
# 获取当前脚本的目录路径  
script_dir = os.path.dirname(os.path.abspath(__file__))  
  
# 构建全景图的URL（这里假设服务器在本地运行，端口为8000）  
url = f'http://localhost:8000/{os.path.relpath(image_path, script_dir)}'  
  
print(url)  # 输出全景图的URL
