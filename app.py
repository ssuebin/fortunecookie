import streamlit as st
import os

# HTML 파일 로드
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# CSS 파일 로드
def load_css(css_file):
    with open(css_file, 'r', encoding='utf-8') as file:
        return f"<style>{file.read()}</style>"

# JS 파일 로드
def load_js(js_file):
    with open(js_file, 'r', encoding='utf-8') as file:
        return f"<script>{file.read()}</script>"

def main():
    # 경로 설정 (Streamlit Cloud에서 파일 경로 주의)
    current_dir = os.path.dirname(__file__)
    html_file = os.path.join(current_dir, 'index.html')
    css_file = os.path.join(current_dir, 'styles.css')
    js_file = os.path.join(current_dir, 'script.js')
    
    # HTML, CSS, JS 삽입
    st.markdown(load_html(html_file), unsafe_allow_html=True)
    st.markdown(load_css(css_file), unsafe_allow_html=True)
    st.markdown(load_js(js_file), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
