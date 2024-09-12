import streamlit as st

def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

def main():
    # HTML 파일 불러오기
    html_file = 'index.html'
    html_content = load_html(html_file)
    
    # HTML 삽입
    st.markdown(html_content, unsafe_allow_html=True)
    
    # 필요시 JS나 CSS 파일도 따로 삽입 가능
    st.markdown("""
        <style>
        /* 여기에 CSS 코드 추가 가능 */
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
