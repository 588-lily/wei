import streamlit as st
import pandas as pd
st.title("🥢南宁美食攻略🍚")
st.text(' 探索南宁最受好评的美食地点！选择你感兴趣的餐厅，查看评分和位置。')
st.header("🎊南宁美食地图")
map_data={
    'latitude':[22.812081,22.768678,22.816239,22.821253,22.868554],
    'longitude':[108.393248,108.433240,108.318796,108.315196,108.292531]

    }
st.map(pd.DataFrame(map_data))

import streamlit as st
import pandas as pd


# 定义数据,以便创建数据框
data = {
    '月份':['中餐', '快餐', '小吃'],
    '均价':[80,40,15],
    
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("💰不同餐厅价格")


# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)

# 通过y参数筛选只显示2、3号门店的数据
st.line_chart(df, y=['均价'])



st.header("🔥餐厅评分")
import streamlit as st
import pandas as pd
data = {
    '餐厅':['麦当劳', '蛙小侠', '越雅鸡肉粉','杨国福麻辣烫','三品王'],
    '评分':[4.7,4.5,3.9,4.3,4.0], 
    }
df = pd.DataFrame(data)
index = pd.Series([1,2,3,4,5], name='餐厅评分')
st.subheader("餐厅评分")
st.bar_chart(df, x='餐厅')
df.set_index('餐厅',inplace=True)





st.header("📍各餐厅12月价格走势图")

import streamlit as st
import pandas as pd

# 定义数据,以便创建数据框
data = {
    '月份':['01月', '02月', '03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
    '麦当劳':[45,50,51,48,60,58,70,68,66,75,69,52],
    '蛙小侠':[79,88,92,87,98,120,110,99,120,128,138,112],
    '越雅鸡肉粉':[12, 14, 15,11,16,13,17,13,19,16,11,12],
    '杨国福麻辣烫':[20,23,26,27,21,29,34,36,28,37,35,37],
    '三品王':[13,17,16,20,22,23,17,18,19,25,27,29]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
# 将新索引应用到数据框上
df.index = index
st.header("折线图")
st.subheader("门店月销售额走势对比")
st.line_chart(df, x='月份')
df.set_index('月份', inplace=True)





st.header("📍用餐高峰时段")
import streamlit as st
import pandas as pd
data = {
    '时段':['11', '12', '13','14','15','16','17','18','19'],
    '麦当劳':[40, 80, 120,110,90,70,89,100,110],
    '蛙小侠':[50, 79,70,80,85,98,120,140,160],
    '越雅鸡肉粉':[29, 40, 60,55,40,30,55,51,45],
    '杨国福麻辣烫':[60,80,75,65,66,85,90,100,110],
    '三品王':[35,50,45,38,30,20,30,32,34]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3,4,5,6,7,8,9], name='序号')
# 将新索引应用到数据框上
df.index = index

st.header("用餐高峰时段")
st.area_chart(df, x='时段')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('时段', inplace=True)

st.header("🍽餐厅详情")






