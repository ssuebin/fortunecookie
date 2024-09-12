import streamlit as st

# HTML 파일 불러오기
html_file = 'index.html'
st.markdown(open(html_file).read(), unsafe_allow_html=True)
