import streamlit as st
c1,c2=st.columns([1,2])
with c1:
    st.set_page_config(page_title="个人简历生成器", page_icon="🎨", layout="wide")
    st.title('个人简历生成器🎨')
    st.text('使用Streamlit创建您的个性化简历')
    st.subheader('个人信息表单')

    name = st.text_input('姓名', autocomplete='name')
    career = st.text_input('职业', autocomplete='career')
    phone = st.text_input('电话', autocomplete='phone')
    email = st.text_input('邮箱', autocomplete='email')
    dob = st.text_input('出生日期', autocomplete='dob')

    st.write('性别👨‍💼👩‍💼')
    gender = st.radio(
    '你的性别是',
    ['男', '女', '其他'],
    horizontal=True,
    label_visibility='hidden'
    )

    import streamlit as st
    def my_format_func(option):
        return f'{option}'
    degrees = st.selectbox('学历：', ['高中','本科','专科','硕士','博士'], format_func=my_format_func, index=2)

    # 自定义format_func函数
    def my_format_func(option):
        return f'{option}'

    language_options = st.multiselect(
       '语言能力',
      ['中文', '英文', '日语', '西班牙语', '俄语', '法语'],
       format_func=my_format_func,
     )

    skill_options = st.multiselect(
       '技能（可多选）',
       ['Python', 'SQL', 'Java', '数据分析', 'HTML/CSS'],
       format_func=my_format_func,
       )
    
    import streamlit as st
    from datetime import datetime, time
    work = st.slider('工作经验（年）', 0, 30)
    pay = st.slider(
      '期望薪资范围（元）',
      5000, 50000,(10000,30000))

    import streamlit as st
    introduce=st.text_area(
        label='个人简介',
        placeholder='请简要介绍您的专业背景、职业目标和个人特点...'
        )



    import streamlit as st
    from datetime import datetime, time
    w1 = st.time_input("最佳联系时间")

    import streamlit as st
    import pandas as pd
    from io import StringIO

    photo=st.file_uploader('上传个人照片')
    if photo is not None:
        bytes_data=photo.getvalue()
        


    
    





with c2:
    st.title('简历实时浏览')
    a1,a2=st.columns(2)
    with a1:
        if photo:
            st.image(photo,width=300)
        st.write('',name)
        st.write('职位：',career)
        st.write('电话：',phone)
        st.write('邮箱：',email)
        st.write('出生日期：',dob)
        st.write('性别：',gender)
    with a2:
        st.write('学历：',degrees)
        s=''
        for yuyan in language_options:
            s=s+yuyan
        
        st.write('语言能力：',s)
        st.write('工作经验：',work)
        st.write('期望薪资：',pay)
        st.write('最佳联系时间：',w1)     
    st.title('个人简介')
    st.write('',introduce)


    st.title('专业技能')
    w=''
    for i in skill_options:
        w=w+i
         
    st.write('技能：',w)

