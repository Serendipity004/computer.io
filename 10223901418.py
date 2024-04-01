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
    txt = st.text_area('曾发表过文案',value="",type="default") #type为缺省
    
#一个表单提交按钮form_submit_button
    submit_button = st.form_submit_button('数据上传')
    
    
#读取csv数据以dataframe显示
url_data = "https://EcnuGISChaser.github.io/gis_development/data/csj_pm25.csv"
df = pd.read_csv(url_data,encoding="utf8")

#创建expander容器
with st.expander("显示原始数据"):
    st.dataframe(df)
