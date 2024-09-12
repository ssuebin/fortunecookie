import streamlit as st
import os

# 파일 로드 함수
def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # 파일 경로 설정
    html_file = 'index.html'
    css_file = 'styles.css'
    js_file = 'script.js'
    
    # CSS 삽입
    st.markdown(f"<style>{load_file(css_file)}</style>", unsafe_allow_html=True)
    
    # HTML 삽입
    st.markdown(load_file(html_file), unsafe_allow_html=True)
    
    # JS 삽입 (가능한 경우, 별도 JS 실행을 위한 처리)
    st.markdown(f"<script>{load_file(js_file)}</script>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
