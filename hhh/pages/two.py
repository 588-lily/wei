import streamlit as st
st.set_page_config(page_title='狗狗',page_icon='🐕')

images = [
    {
      'url':'https://image.petmd.com/files/styles/863x625/public/CANS_dogsmiling_379727605.jpg?w=1920&q=75',
      'parm':'金毛'
    },
    {
      'url':'https://breedingbusiness.com/wp-content/uploads/2021/07/cutest-small-white-dog-breeds.jpg',
      'parm':'萨摩耶'
    },
    {
      'url': 'https://www.dictionary.com/e/wp-content/uploads/2017/02/catOrDogPerson_1000x700.jpg',
      'parm':'金毛'

     },
    {
      'url':'https://cdn.wallpapersafari.com/50/62/T5eaoX.jpg',
      'parm':'金毛'
    },
    {
     'url':'https://www.dogster.com/wp-content/uploads/2024/10/Bluey.jpg',
     'parm':'动漫狗'

    }
    
]

if 'ind'not in st.session_state:
    st.session_state['ind'] = 0

def nextImg():
   st.session_state['ind'] = (st.session_state['ind'] + 1)%len(images)
def lastImg():
   st.session_state['ind'] = (st.session_state['ind'] - 1)%len(images)

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])

c1,c2=st.columns(2)
with c1:
    st.button('下一张',on_click=nextImg)  
  
with c2:
    st.button('上一张',on_click=lastImg)

