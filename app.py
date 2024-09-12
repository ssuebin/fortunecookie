import streamlit as st
import os

def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # 현재 스크립트의 디렉토리 경로 설정
    current_dir = os.path.dirname(__file__)
    
    # 파일 경로 설정
    html_file = os.path.join(current_dir, 'index.html')
    css_file = os.path.join(current_dir, 'styles.css')
    js_file = os.path.join(current_dir, 'script.js')
    
    # HTML, CSS, JS 파일 읽고 삽입
    st.markdown(load_file(css_file), unsafe_allow_html=True)
    st.markdown(load_file(html_file), unsafe_allow_html=True)
    st.markdown(f"<script>{load_file(js_file)}</script>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
