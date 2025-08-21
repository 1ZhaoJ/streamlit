# streamlit run c:\Software\project\pyserial_mysql_streamlit\实时显示数据\streamlit_app.py
#  streamlit run c:\Software\project\pyserial_mysql_streamlit\实时显示数据\streamlit_app.py --server.address 192.168.4.114 --server.port 8501
import streamlit as st
import mysql.connector
import pandas as pd
import time
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
import os
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
# 启用跨域访问
st._config.set_option('server.enableCORS', True)
st._config.set_option('server.enableXsrfProtection', False)



# 共享MySQL配置
DB_CONFIG = {
    'host': 'localhost',
    'port': "3306",
    'user': 'streamlit',
    'password': 'dudu018027',
    'database': 'streamlit'
}

TABLE_NAME = 'vehicle_data'

def get_data(limit=100):
    """从数据库获取最新数据"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        query = f"""
        SELECT timestamp, x, y, z, temperature, humidity 
        FROM {TABLE_NAME} 
        ORDER BY timestamp DESC 
        LIMIT {limit}
        """
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"数据库错误: {e}")
        return pd.DataFrame()
    finally:
        if conn.is_connected():
            conn.close()

def get_cloud_data(limit=1000):
    """获取3D云图数据"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        query = f"SELECT x, y, z, temperature FROM {TABLE_NAME} ORDER BY timestamp DESC LIMIT {limit}"
        return pd.read_sql(query, conn)
    except Exception as e:
        st.error(f"数据库错误: {e}")
        return pd.DataFrame()
    finally:
        if conn.is_connected():
            conn.close()

def create_3d_cloud(df):
    """创建3D云图"""
    if df.empty:
        return go.Figure()
    
    latest = df.iloc[0]
    latest_x, latest_y, latest_z = latest['x'], latest['y'], latest['z']
    
    fig = go.Figure(data=[
        go.Scatter3d(
            x=df['x'],
            y=df['y'],
            z=df['z'],
            mode='markers',
            marker=dict(
                size=5,
                color=df['temperature'],  # 颜色映射温度值
                colorscale='Viridis',
                opacity=0.8,
                colorbar=dict(title='温度')
            )
        )
    ])
    
    # 添加台车模型（简单立方体表示）
    fig.add_trace(go.Mesh3d(
        x=[latest_x-0.5, latest_x+0.5, latest_x+0.5, latest_x-0.5, 
           latest_x-0.5, latest_x+0.5, latest_x+0.5, latest_x-0.5],
        y=[latest_y-0.2, latest_y-0.2, latest_y+0.2, latest_y+0.2,
           latest_y-0.2, latest_y-0.2, latest_y+0.2, latest_y+0.2],
        z=[latest_z, latest_z, latest_z, latest_z,
           latest_z+0.3, latest_z+0.3, latest_z+0.3, latest_z+0.3],
        i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k=[0, 7, 2, 3, 6, 7, 1, 7, 5, 5, 7, 6],
        color='blue',
        opacity=0.6
    ))
    
    fig.update_layout(
        scene=dict(
            xaxis_title='X 坐标',
            yaxis_title='Y 坐标',
            zaxis_title='Z 高度',
            aspectmode='cube'
        ),
        height=800,
        margin=dict(l=0, r=0, b=0, t=30)
    )
    return fig

# 页面设置
st.set_page_config(page_title="传感器实时监控", layout="wide")
st.title("传感器数据实时仪表板")

# 初始化占位符
metric_placeholder = st.empty()
tabs_placeholder = st.empty()
cloud_placeholder = st.empty()

# 自动刷新设置
refresh_rate = st.slider("刷新频率（秒）", 1, 10, 2, key="refresh_rate")

# 主刷新循环
last_refresh = time.time()
stop_refresh = False

while not stop_refresh:
    # 获取数据
    df = get_data(100)
    cloud_df = get_cloud_data(1000)
    
    with metric_placeholder.container():
        # 创建5列用于显示实时数值
        col1, col2, col3, col4, col5 = st.columns(5)
        
        if not df.empty:
            # 格式化时间戳
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # 获取最新数据
            latest = df.iloc[0]
            
            # 显示实时数值
            with col1:
                st.metric("X方向位移", f"{latest['x']:.2f}g")
            with col2:
                st.metric("Y方向位移", f"{latest['y']:.2f}g")
            with col3:
                st.metric("Z方向位移", f"{latest['z']:.2f}g")
            with col4:
                st.metric("温度", f"{latest['temperature']:.1f}°C")
            with col5:
                st.metric("湿度", f"{latest['humidity']:.1f}%")
        else:
            st.warning("等待传感器数据...")
    
    with tabs_placeholder.container():
        if not df.empty:
            # 反转数据顺序（最新数据在最后）
            df = df.sort_values('timestamp', ascending=True)
            
            # 创建传感器图表
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "X方向位移", "Y方向位移", "Z方向位移", "温度", "湿度"
            ])
            
            with tab1:
                fig_x = px.line(
                    df, x='timestamp', y='x',
                    title='X 方向实时位移',
                    labels={'x': '位移 (m)', 'timestamp': '时间'}
                )
                st.plotly_chart(fig_x, use_container_width=True)
            
            with tab2:
                fig_y = px.line(
                    df, x='timestamp', y='y',
                    title='Y 方向实时位移',
                    labels={'y': '位移 (m)', 'timestamp': '时间'}
                )
                st.plotly_chart(fig_y, use_container_width=True)
            
            with tab3:
                fig_z = px.line(
                    df, x='timestamp', y='z',
                    title='Z 方向实时位移',
                    labels={'z': '位移 (m)', 'timestamp': '时间'}
                )
                st.plotly_chart(fig_z, use_container_width=True)
            
            with tab4:
                fig_temp = px.line(
                    df, x='timestamp', y='temperature',
                    title='温度实时趋势',
                    labels={'temperature': '温度 (°C)', 'timestamp': '时间'}
                )
                st.plotly_chart(fig_temp, use_container_width=True)
            
            with tab5:
                fig_humd = px.line(
                    df, x='timestamp', y='humidity',
                    title='湿度实时趋势',
                    labels={'humidity': '湿度 (%)', 'timestamp': '时间'}
                )
                st.plotly_chart(fig_humd, use_container_width=True)
    
    with cloud_placeholder.container():
        st.header("3D 位移云图")
        fig_3d = create_3d_cloud(cloud_df)
        st.plotly_chart(fig_3d, use_container_width=True)
    
    # 添加控制按钮
    if st.button('停止刷新'):
        stop_refresh = True
    
    # 显示刷新时间
    current_time = datetime.now().strftime("%H:%M:%S")
    st.caption(f"最后刷新: {current_time} | 下次刷新: {refresh_rate}秒后")
    
    # 等待设定的时间
    time.sleep(refresh_rate)
    st.experimental_rerun()