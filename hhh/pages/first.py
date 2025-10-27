import streamlit as st

st.title("我的第一个Streamlit应用")
st.text('这也是一个普通文本展示元素，带有工具提示🤑',help='带有工具提示')
st.text('''读者们，\n你们好\t！欢迎学习Streamlit😁''')
st.text("Hello World!")



st.title("代码")
str='''a=1
b=2
print(a+b)
'''

st.code(str,language=None)
st.caption('这是python代码')
st.code(str,language="python",line_numbers=True)


st.markdown('***')
st.markdown('# 一级标题')
st.markdown('## 二级标题')
st.markdown('*斜体文本*')
st.markdown(':red[斜体]')
st.markdown('**粗体文本**')

import pandas as pd  
import streamlit as st
st.markdown('# 🐕 动物 小狗- 数字档案')
st.image("https://img95.699pic.com/photo/60027/3385.jpg_wh860.jpg")
st.markdown('## 🟡基础信息')
st.text('''动物ID：emo:1314-520''')
st.text('动物出生时间:2023-10-20 11:04|精神状态:✅良好')
st.text('当前位置:家|安全等级：绝密')


import streamlit as st  # 导入Streamlit并用st代表它


st.subheader('🐾动物技能')



# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="坐下", value="32", delta="+1.5")
c2.metric(label="上厕所", value="76", delta="6")
c3.metric(label="握手", value="80", delta="10")

import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '任务':['小狗学坐下', '学会上厕所', '学会握手' ],
    '状态':['✅完成', '⭕进行中', '❌未完成' ],
    '难度':['🔴🔴🔴◯◯', '🔴🔴◯◯◯', '🔴◯◯◯◯' ],
}
# 定义数据框所用的索引
index = pd.Series(['2025-9-23', '2025-9-28', '2025-9-35', ], name='日期')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('动物技能')
st.table(df)



st.title("🐕最新代码成果")
str='''a=1
b=2
print(a+b)
'''


st.code(str,language="python",line_numbers=True)

st.markdown('*********************************')

st.markdown(':green[>>>SYSTEH MESSAGE:]下一个任务目标')
st.markdown(':green[>>>TAGET:]训练系统')
st.markdown(':green[>>>COUNTDOWN:]2025-10-25')
st.markdown('系统状态：在线 连接状态：已加密')


