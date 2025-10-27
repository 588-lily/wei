import streamlit as st
st.title("🎶简易音乐播放器")
st.markdown('##### 使用Streamlit制作的简易音乐播放器，支持切歌和基本播放控制')
st.set_page_config(page_title='音乐库',page_icon='🎶')
music=[
    {'url':'https://music.163.com/song/media/outer/url?id=2071452224.mp3',
          'parm':'专辑封面',
          'photo':'https://p2.music.126.net/q_ZSJmVQ_NlLXq7UNAYK3g==/109951168826077552.jpg?param=180y180',
          'name':'Take my hand',
          'author':'DAISHI DANCE / Cécile Corbel',
          'time':'4:19'
     },
         {'url':'https://music.163.com/song/media/outer/url?id=1456890009.mp3',
          'parm':'专辑封面',
          'photo':'https://p1.music.126.net/yN1ke1xYMJ718FiHaDWtYQ==/109951165076380471.jpg?param=180y180',
          'name':'罗生门',
          'author':'梨冻紧 / Wiz_H张子豪',
          'time':'4:03'
          },
         {'url':'https://music.163.com/song/media/outer/url?id=30352891.mp3',
          'parm':'专辑封面',
          'photo':'https://p2.music.126.net/Nd86SOcyCxU5Qu7jdZn_MQ==/7725168696876736.jpg?param=180y180',
          'name':'牵丝戏',
          'author':'银临 / Aki阿杰',
          'time':'3:59'}
]

import streamlit as st

if 'ind' not in st.session_state:
    st.session_state['ind']=0
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1) % len(music)
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1) % len(music)



a1,a2=st.columns([1,2])
with a1:
    st.image(music[st.session_state['ind']]['photo'],caption=music[st.session_state['ind']]['parm'])
with a2:
    st.header(music[st.session_state['ind']]['name'])
    st.subheader(f"歌手:{music[st.session_state['ind']]['author']}")
    st.caption(f"时长:{music[st.session_state['ind']]['time']}")
    col1,col2=st.columns(2)   
with col2:
   st.button('⏩下一首',on_click=nextImg,use_container_width=True)
with col1:
   st.button('⏪上一首',on_click=lastImg,use_container_width=True)
st.audio(music[st.session_state['ind']]['url'])



import streamlit as st
# 设置页面标题
st.title("音乐播放器 - 使用说明")
# 1. 创建下拉选择框（选项对应不同说明模块）
option = st.selectbox(
    "选择要查看的说明内容：",
    ("功能说明", "课堂练习任务", "扩展练习（可选）"))
# 2. 根据选择的选项，显示对应的内容
if option == "功能说明":
   st.subheader("音乐播放器功能说明：")
   st.write("1. 播放/暂停：点击中间的播放/暂停按钮控制音乐播放")
   st.write("2. 切换功能：使用左右箭头按钮切换上一首/下一首")
   st.write("3. 歌曲列表：从列表中选择任意歌曲播放")
elif option == "课堂练习任务":
    st.subheader("课堂练习任务：")
    st.write("1. 实现基本的播放控制功能")
    st.write("2. 添加专辑封面显示")
    st.write("3. 实现切换功能（上一首/下一首）")
    st.write("4. 显示歌曲基本信息（标题、歌手、时长）")
elif option == "扩展练习（可选）":
    st.subheader("扩展练习（可选）：")
    st.write("• 添加随机播放功能")
    st.write("• 实现音量控制")
    st.write("• 添加播放进度显示")

'---------------------------------------------------'
st.text('Streamlit音乐播放器|课堂练习示例|使用python、streamlit构建')





