import streamlit as st
st.set_page_config(page_title='视频网站',page_icon='🔊')
st.title('视频播放器💗')
video_url=[{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/58/57/30023615758/30023615758-1-192.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761301849&mid=0&oi=771356656&nbs=1&gen=playurlv3&uipk=5&platform=html5&trid=c28ad0efd882432c96997c9c5ac7668h&os=cosovbv&og=hw&upsig=35296743fbd2506700255d5bc2a43cf1&uparams=e,deadline,mid,oi,nbs,gen,uipk,platform,trid,os,og&bvc=vod&nettype=0&bw=841919&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
    'title':'甜心格格 第一季',
    'episode':'第一集 剪纸不见了'
    },{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/52/93/30023749352/30023749352-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=d487dd2e2b16499bb314fcf534abeaah&mid=0&platform=html5&os=cosovbv&og=hw&deadline=1761302607&nbs=1&oi=771356656&gen=playurlv3&uipk=5&upsig=dbc8f8c49d9fbac42c39e4646a9a31f7&uparams=e,trid,mid,platform,os,og,deadline,nbs,oi,gen,uipk&bvc=vod&nettype=0&bw=807976&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'甜心格格 第一季',
    'episode':'第二集 下不来的气球'
        },{
    'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/58/57/30023615758/30023615758-1-192.mp4?e=ig8euxZM2rNcNbRV7WdVhwdlhWdBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=b478770c8ff746a1af3528094c7036eh&mid=0&uipk=5&oi=771356656&deadline=1761302812&platform=html5&os=cosovbv&og=hw&nbs=1&gen=playurlv3&upsig=4057c527b8de66bd2220766c930e2089&uparams=e,trid,mid,uipk,oi,deadline,platform,os,og,nbs,gen&bvc=vod&nettype=0&bw=841919&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
    'title':'甜心格格 第一季',
    'episode':'第三集 新科武状元'}]
if 'ind' not in st.session_state:
    st.session_state['ind']=0
    
st.header(video_url[st.session_state['ind']]['title'])
st.subheader(video_url[st.session_state['ind']]['episode'])

st.video(video_url[st.session_state['ind']]['url'])

   

c1,c2,c3=st.columns(3)

def play(arg):
    st.session_state['ind']=int(arg)

for i in range(len(video_url)):
    st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))





