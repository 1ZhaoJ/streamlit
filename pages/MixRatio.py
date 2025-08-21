import streamlit as st
import sympy

# Define a dictionary to store the values you want to update based on the selectbox value
params = {
    "W_B_Max": "",
    "W_B_Max_str": " ",
    "other_parameter_1": "",
    "other_parameter_2": "",
    "aggregate_type": "碎石",
    "concrete_design_strength": "",
    "Cement_strength": "",
    "fly_ash_content": "",
    "slag_content": "",
    "addition_of_admixtures": "",
    "water_reducing_rate": "",
    "sand_rate": "",
    "cementitious_materials_min": "",
    "m_w0": "",
    "m_cp": "",
    "gamma_ceg": "",  #水泥强度富余系数
    
    "c_28d_cs": "",  #水泥28d胶砂抗压强度
    "cm_28d_cs": "",  #胶凝材料28d胶砂抗压强度
    "gamma_f": "",  #粉煤灰影响系数
    "gamma_s": "",  #粒化高炉矿渣粉影响系数
    "design_strength": "",  #设计强度
    "theta": "",  #混凝土强度标准差（MPa）
    "Alpha_a": "",  #回归系数a
    "Alpha_b": "",  #回归系数b
    "W_B": " ",  #水胶比
    

    

}
if "aggregate_type" not in params:  
    params["aggregate_type"] = "碎石"  

col1, col2 = st.columns(2)
with col1:
   concrete_design_strength = st.selectbox(
      "混凝土设计强度",
      ("C15", "C20", "C25", "C30", "C35", "C40", "C45", "C50", "C55", "C60"),
      index=3,
      placeholder="Select contact method...",
   )
   params["concrete_design_strength"] = concrete_design_strength
   st.write("You selected:", concrete_design_strength)
with col2:
   Cement_strength = st.selectbox(
      "水泥强度（MPa）",
      ("32.5", "42.5", "52.5"),
      index=0,
      placeholder="Select contact method...",
   )
   params["Cement_strength"] = Cement_strength
   st.write("You selected:", Cement_strength)
   
if params["Cement_strength"] == "32.5"  :
    params["gamma_ceg"] = "1.12"
    gamma_ceg=1.12
elif params["Cement_strength"] == "42.5":
    params["gamma_ceg"] = "1.16"
    gamma_ceg=1.16
else:
    if params["Cement_strength"] == "52.5":
        params["gamma_ceg"] = "1.10"
        gamma_ceg=1.10
print(f"gamma_ceg: {gamma_ceg}")

col1, col2 = st.columns(2)
with col1:
    aggregate_type = st.selectbox("集料类型", ("碎石", "鹅卵石"),
                                  index=0, key="aggregate_type_selectbox")
    params["aggregate_type"] = aggregate_type
    st.write("Selected Aggregate Type:", params["aggregate_type"])

with col2:
    W_B_Max = st.selectbox("最大水胶比", ("0.60", "0.55", "0.50", "0.45"),
                                          index=0, key="max_water_binder_ratio_selectbox")
    params["W_B_Max"] = W_B_Max
    st.write("Selected Max Water Binder Ratio:", params["W_B_Max"])

st.image(r'images\W_Bmax.png', caption='图1 ', use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    fly_ash_content = st.number_input("粉煤灰掺量（%）", min_value=0.0, max_value=50.0, step=0.01,
                                       format="%.2f")
    params["fly_ash_content"] = float(fly_ash_content)
    st.write("the current number is ", "%.2f" % fly_ash_content)

with col2:
    slag_content = st.number_input("粒化高炉矿渣粉掺量（%）", min_value=0.0, max_value=50.0, step=0.01, format="%.2f")
    params["slag_content"] = float(slag_content)
    st.write("the current number is ", "%.2f" % slag_content)

st.image(r'images\Snipaste_2024-07-20_10-40-19.jpg', caption='图2 ', use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    gamma_f = st.number_input("粉煤灰影响系数", min_value=0.55, max_value=1.0,
                             help="请输入粉煤灰影响系数（0.55-1.00）,参考图2", step=0.01, format="%.2f")
    params["gamma_f"] = float(gamma_f)
    st.write("the current number is ", "%.2f" % gamma_f)

with col2:
    gamma_s = st.number_input("粒化高炉矿渣粉影响系数", min_value=0.7, max_value=1.0, 
                              help="请输入粒化高炉矿渣粉影响系数（0.70-1.00）,参考图2",step=0.01, format="%.2f")
    params["gamma_s"] = float(gamma_s)
    st.write("the current number is ", "%.2f" % gamma_s)

col1, col2 = st.columns(2)
with col1:
    addition_of_admixtures = st.number_input("外加剂掺量（%）", min_value=1.0, max_value=1.2, step=0.01, format="%.2f")
    params["addition_of_admixtures"] = float(addition_of_admixtures)
    st.write("the current number is ", "%.2f" % addition_of_admixtures)

with col2:
    water_reducing_rate = st.number_input("减水剂减水率（%）", min_value=8.0, max_value=100.0, step=0.01, format="%.2f")
    params["water_reducing_rate"] = float(water_reducing_rate)
    st.write("the current number is ", "%.2f" % water_reducing_rate)




image_path = r'images\Sand_rate.png'  

# 显示帮助图片
st.image(r'images\Sand_rate.png', caption='图3 ', use_column_width=True)

st.image(r'images\cementitious_materials_min.png', caption='图4 ', use_column_width=True)

col1, col2 = st.columns(2)
with col1:
    sand_rate = st.number_input("砂率（%）",min_value =0,max_value =100,
                             help="参考图3")
    params["sand_rate"] = sand_rate
    st.write("The current number is ", sand_rate)
with col2:
    cementitious_materials_min = st.number_input("最小胶凝材料用量（kg/m³）",help="参考图4")
    params["cementitious_materials_min"] = cementitious_materials_min
    st.write("The current number is ", cementitious_materials_min)

st.image(r'images\Snipaste_2024-07-20_10-24-19.jpg', caption='图5 ', use_column_width=True)
col1, col2 = st.columns(2)
with col1:
    m_w0 = st.number_input("加减水剂前的需水量（kg/m³）",help="参考图5")
    params["m_w0"] = m_w0
    st.write("The current number is ", m_w0)
with col2:
    m_cp = st.number_input("混凝土拌合物的假定质量（kg）", value=2350, placeholder="2350~2450",
                             min_value =2350,max_value =2450)
    params["m_cp"] = m_cp
    st.write("The current number is ", m_cp)

# 将 widget 的初始值存储在会话状态下
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)
with col1:
    st.checkbox("水泥28d胶砂抗压强度（MPa）是否有实测值，若有则输入", key="disabled")
with col2:
    c_28d_cs = st.number_input("水泥28d胶砂抗压强度（MPa）",min_value =0,
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,)
    params["c_28d_cs"] = c_28d_cs
    st.write("The current number is ", c_28d_cs)
if params["c_28d_cs"]>0:
    params["c_28d_cs"] = c_28d_cs
else: 
    gamma_ceg = float(params["gamma_ceg"])  
    cement_strength = float(params["Cement_strength"])  
    # 执行赋值操作  
    c_28d_cs = round(gamma_ceg * cement_strength, 2)


# 将 widget 的初始值存储在会话状态下
if "visibility_section2" not in st.session_state:  
    st.session_state.visibility_section2 = "visible"  
    st.session_state.disabled_cm = False  # 更改键名以保持一致性  
  
col1, col2 = st.columns(2)  
  
with col1:  
    st.checkbox("胶凝材料28d胶砂抗压强度（MPa）是否有实测值，若有则输入", key="disabled_cm")  # 更改key以与会话状态中的键名匹配  
  
with col2:  
    cm_28d_cs = st.number_input("胶凝材料28d胶砂抗压强度（mpa）", min_value=0,  
                                label_visibility=st.session_state.visibility_section2,  
                                disabled=st.session_state.disabled_cm) 
    params["cm_28d_cs"] = cm_28d_cs
    st.write("The current number is ", cm_28d_cs)

#表示设计强度
# 假设 params["concrete_design_strength"] 是 'C20'  
design_strength_str = params["concrete_design_strength"]  
# 检查字符串是否以 'C' 开头，并尝试提取后面的数字部分  
if design_strength_str.startswith('C'):  
    design_strength_num = design_strength_str[1:]  # 移除开头的 'C'  
    try:  
        concrete_design_strength = float(design_strength_num)  
    except ValueError:  
        # 如果提取后的字符串不是有效的数字，则抛出错误  
        raise ValueError(f"Invalid design strength format: {design_strength_str}")  
else:  
    # 如果字符串不是以 'C' 开头，也抛出错误  
    raise ValueError(f"Unexpected design strength format: {design_strength_str}")  
  
# 现在 concrete_design_strength 应该是一个浮点数，值为 20.0
theta = params["theta"]

if theta:  # Check if theta is not an empty string
    try:
        theta = float(theta)
    except ValueError:
        raise ValueError(f"Error converting theta to float: {params['theta']}")
#计算配制强度f_cu0
f_cuk = concrete_design_strength
if concrete_design_strength in [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]:
    if concrete_design_strength < 60:
        if theta != "":
            theta = float(theta)
        else:
            if concrete_design_strength <= 20:
                theta = 4.0
            elif 25 <= concrete_design_strength <= 45:
                theta = 5.0
            elif 50 <= concrete_design_strength <= 55:
                theta = 6.0
        f_cu0 = f_cuk + 1.6450 * theta
        f_cu0 = round(f_cu0, 1)
    elif concrete_design_strength >= 60:
        f_cu0 = 1.15 * f_cuk
        f_cu0 = round(f_cu0, 1)
print(f"Calculated f_cu0: {f_cu0}")


if params["cm_28d_cs"]>0:
    params["cm_28d_cs"] = round(cm_28d_cs, 2)
else: 
    gamma_f = float(params["gamma_f"])  
    gamma_s = float(params["gamma_s"])   
    params["c_28d_cs"] = float(params["c_28d_cs"])
    # 执行赋值操作  
    cm_28d_cs = round(gamma_f * gamma_s * c_28d_cs, 2)
    params["cm_28d_cs"] = round(cm_28d_cs, 2)
print(f"c_28d_cs: {c_28d_cs}")
print(f"cm_28d_cs: {cm_28d_cs}")
# 回归系数a_a和a_a
Alpha_a = None    
Alpha_b = None   
  
# 处理 Alpha_a  
if Alpha_a is not None:  
    if isinstance(Alpha_a, str):  
        if Alpha_a.replace('.', '', 1).isdigit():  
            Alpha_a = float(Alpha_a)  
        else:  
            raise ValueError(f"Error converting alpha_a to float: {Alpha_a}")  
    elif isinstance(Alpha_a, (int, float)):    
        pass  
    else:   
        raise TypeError(f"Unsupported type for alpha_a: {type(Alpha_a)}")  
else:    
    if aggregate_type == "碎石":  
        Alpha_a = 0.53  
    elif aggregate_type == "鹅卵石":  
        Alpha_a = 0.49  
  
# 处理 Alpha_b  
if Alpha_b is not None:  
    if isinstance(Alpha_b, str):  
        if Alpha_b.replace('.', '', 1).isdigit():  
            Alpha_b = float(Alpha_b)  
        else:  
            raise ValueError(f"Error converting alpha_b to float: {Alpha_b}")  
    elif isinstance(Alpha_b, (int, float)):  
        # 如果已经是整数或浮点数，则无需转换  
        pass  
    else:  
        # 如果不是字符串、整数或浮点数，则抛出错误（这里可以根据需要处理）  
        raise TypeError(f"Unsupported type for alpha_b: {type(Alpha_b)}")  
else:  
    # 如果 Alpha_b 是 None，则根据 aggregate_type 设置默认值  
    if aggregate_type == "碎石":  
        Alpha_b = 0.20  
    elif aggregate_type == "鹅卵石":  
        Alpha_b = 0.12  
print(f"Alpha_a: {Alpha_a}")
print(f"Alpha_b: {Alpha_b}")  
#计算水胶比
W_B = Alpha_a * f_cu0 / (f_cu0 + Alpha_a * Alpha_b * f_cu0)
W_B = round(W_B, 2)
#查表确定最大水胶比W_Bmax
# W_B_Max = float(W_B_Max)
# if W_B <= W_B_Max:
#     W_B = W_B
# elif W_B > W_B_Max:
#     W_B = W_B_Max
# print(f"W_B: {W_B}")
#计算胶凝材料用量m_b0
m_w0 = round(m_w0, 2)
m_w0 = float(m_w0)
water_reducing_rate = float(water_reducing_rate)
m_w0 = m_w0 * (1 - water_reducing_rate/100)
m_b0 = m_w0 / W_B
m_w0 = round(m_w0, 2)
m_b0 = int(m_b0)
cementitious_materials_min = int(cementitious_materials_min)
if m_b0 <= cementitious_materials_min:
    m_b0 = cementitious_materials_min
else:
    m_b0 = m_b0
m_b0 = round(m_b0, 2)
print(f"m_b0: {m_b0}")
m_fly_ash = m_b0 * fly_ash_content / 100
m_slag = m_b0 * slag_content / 100
m_cement = m_b0 - m_fly_ash - m_slag
m_fly_ash = round(m_fly_ash, 2)

#计算外加剂用量m_a0
addition_of_admixtures = float(addition_of_admixtures)
m_a0 = m_b0 * addition_of_admixtures / 100
m_a0 = round(m_a0, 2)
print(f"m_a0: {m_a0}")
#查表得到砂率Sand rate
sand_rate = int(sand_rate)

#计算砂石用量sand_rate
# m_f0 + m_c0 + m_g0 + m_s0 + m_w0 = m_cp
# sand_rate = m_s0 / (m_g0 + m_s0)
m_cp = int(m_cp)
x, y = sympy.symbols('m_g0 , m_s0')
eq1 = sympy.Eq(m_b0 + m_w0 + x + y, m_cp)
eq2 = sympy.Eq(y / (x + y), sand_rate / 100)
sol = sympy.solve((eq1, eq2), (x, y))
m_g0 = int(sol[x])
m_s0 = int(sol[y])
print("计算配合比每立方米混凝土拌合物的粗骨料用量m_g0=" , m_g0 , "kg/m3")
print("计算配合比每立方米混凝土拌合物的细骨料用量m_s0=" , m_s0 , "kg/m3")
st.write("混凝土设计强度design_strength", "=", concrete_design_strength, "MPa")
st.write("混凝土配制强度f_cu0", "=", f_cu0, "MPa")
st.write("水泥28d抗压强度c_28d_cs", "=", c_28d_cs, "MPa")
st.write("胶凝材料28d抗压强度cm_28d_cs", "=", cm_28d_cs, "MPa")
st.write("混凝土水胶比W/B", "=", W_B)
st.write("砂率sand_rate", "=", sand_rate, "%")
st.write("计算配合比每立方米混凝土拌合物的水泥用量m_cement=", m_cement, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的粉煤灰用量m_fly_ash=", m_fly_ash, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的矿渣粉用量m_slag=", m_slag, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的水用量m_w0=", m_w0, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的细骨料用量（砂石）m_s0=", m_s0, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的粗骨料用量（碎石或鹅卵石）m_g0=", m_g0, "kg/m3")
st.write("计算配合比每立方米混凝土拌合物的外加剂用量m_a0=", m_a0, "kg/m3")
if m_cement== 0:
    m_cement=1.0
ratio_m_cement = round(m_cement / m_cement, 2)
ratio_fly_ash = round(m_fly_ash / m_cement, 2)
ratio_slag = round(m_slag / m_cement, 2)
ratio_w0 = round(m_w0 / m_cement, 2)
ratio_s0 = round(m_s0 / m_cement, 2)
ratio_g0 = round(m_g0 / m_cement, 2)
ratio_a0 = round(m_a0 / m_cement, 2)
st.write("配合比m_cement:m_fly_ash:m_slag:m_w0:m_s0:m_a0=", ratio_m_cement, ":",ratio_fly_ash,":",ratio_slag,":",ratio_w0,":",ratio_s0,":",ratio_g0,":",ratio_a0,)


