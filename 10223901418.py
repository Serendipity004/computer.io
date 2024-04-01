import pandas as pd
import streamlit as st

#添加标题
st.title('社交媒体情感分析平台')

#创建表单
with st.form("my_form"):
    st.header("基本信息收集表单")

#第一个“性别”
    gender = list(["男","女"])
    gender1 = st.selectbox('性别',gender)
    
#第二个“年龄”
    age1 = st.number_input('年龄',min_value=0,max_value=150,value=0,format="%d")
    
#一个Text_input昵称
    txt = st.text_input('输入用户名',value="",type="default") #type为缺省
    
#一个表单提交按钮form_submit_button
    submit_button = st.form_submit_button('提交')
    

with st.form("my_form2"):
    st.header("数据收集表单")
    
#一个Text_input昵称
    txt = st.text_input('曾发表过文案',value="",type="default") #type为缺省
    
#一个表单提交按钮form_submit_button
    submit_button = st.form_submit_button('数据上传')
    uploaded_file = st.file_uploader("上传文件", type=['txt', 'csv', 'xlsx'])
    # 处理上传的文件
    if uploaded_file is not None:
    # 读取文件内容
        file_contents = uploaded_file.read()
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
            df = pd.read_excel(uploaded_file)
    df.head()
