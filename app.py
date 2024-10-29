import streamlit as st
import random

# 포춘 메시지 리스트
fortunes = [
    "오늘은 행운이 따를 것입니다.",
    "당신은 놀라운 기회를 얻을 것입니다.",
    "힘든 시기가 지나갈 것입니다.",
    "새로운 친구를 사귈 기회가 생길 것입니다.",
    "긍정적인 태도가 좋은 결과를 가져올 것입니다.",
    "당신의 노력은 결실을 맺을 것입니다.",
    "마음을 여는 것이 중요합니다.",
    "자신을 믿으세요.",
    "생각지도 못한 곳에서 답을 찾게 될 것입니다.",
    "당신의 목표는 곧 달성될 것입니다."
]

def main():
    # 상태 초기화
    if "show_fortune" not in st.session_state:
        st.session_state.show_fortune = False
        st.session_state.fortune_message = ""

    # 페이지 제목 (가운데 정렬 및 글씨 크기 조정)
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>포춘쿠키</h1>", unsafe_allow_html=True)

    # 버튼 클릭 시 상태 변경
    if st.button("포춘쿠키 열기"):
        st.session_state.show_fortune = True
        st.session_state.fortune_message = random.choice(fortunes)

    # 메시지 화면 표시
    if st.session_state.show_fortune:
        st.markdown("<h2 style='text-align: center; font-size: 24px;'>🍪 당신의 포춘 메시지:</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-size: 20px;'>{st.session_state.fortune_message}</h3>", unsafe_allow_html=True)
        if st.button("다시 열기"):
            st.session_state.show_fortune = False  # 초기 화면으로 돌아가기

if __name__ == "__main__":
    main()
