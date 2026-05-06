import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="오늘 뭐 입지?",
    page_icon="👕",
    layout="wide"
)

st.title("👕 오늘 뭐 입지?")
st.write("날씨와 스타일에 따라 코디를 추천해주는 앱")

gender = st.selectbox(
    "성별 선택",
    ["남성", "여성"]
)

style = st.selectbox(
    "스타일 선택",
    ["캐주얼", "스트릿", "미니멀", "스포티"]
)

weather = st.slider(
    "오늘 기온",
    min_value=-10,
    max_value=35,
    value=20
)

if st.button("코디 추천 받기"):
    st.success(f"{gender} / {style} 스타일 추천 완료!")
    
    if weather >= 25:
        st.write("반팔 + 반바지 추천 ☀️")
    elif weather >= 15:
        st.write("후드집업 + 청바지 추천 🍃")
    else:
        st.write("코트 + 니트 추천 ❄️")
