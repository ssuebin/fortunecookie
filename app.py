import streamlit as st
import random

# 포춘 메시지 리스트
fortunes = [
    "자신이 사는 곳을 떠나고자 하는 자는 행복하지 않은 사람이다.",
    "Muss es sein? Es muss sein! (그래야만 하는가? 그래야만 한다!)",
    "진중하게 내린 결정은 운명의 목소리와 결부되었다.",
    "인간을 위대하게 하는 것은, 아틀라스가 어깨에 하늘을 지고 있듯 인간도 자신의 운명을 짊어지고 있다는 점이다.",
    "자기 육체를 등한시하다간 쉽게 육체의 희생자가 되는 법이다.",
    "하나의 사랑이 잊히지 않는 사랑이 되기 위해서는 성 프란체스코의 어깨에 새들이 모여 앉듯 첫 순간부터 여러 우연이 합해져야만 한다.",
    "엄청나게 많은 우연의 일치를 우리는 대게 완전히 무심결에 지나쳐 버린다.",
    "인간의 삶은 마치 악보처럼 구성된다.",
    "인간은 가장 깊은 절망의 순간에서조차 무심결에 아름다움의 법칙에 따라 자신의 삶을 작곡한다.",
    "인간이 신비로운 우연의 만남을 보지 못하고 그의 삶에서 미적 차원을 배제한다면 비난받아 마땅하다.",
    "고민으로부터 그녀를 불쑥 구원하고 새로운 삶의 욕구를 그녀 가슴에 채워 준 것은 다름 아닌 아름다움의 의미였다.",
    "자신의 내밀성을 상실한 자는 모든 것을 잃은 사람이다.",
    "뇌 속에는 시적 기억이라 일컬을 수 있는 아주 특별한 지대가 존재해서 우리를 매료하고, 감동시키고, 우리의 삶에 아름다움을 주는 것이 기록된다.",
    "나는 쾌락을 찾는 것이 아니라 행복을 찾아. 행복없는 쾌락은 쾌락이 아니야.",
    "사랑은 은유로 시작된다.",
    "한 사람이 언어를 통해 우리의 시적 기억에 아로새겨지는 순간, 사랑은 시작되는 것이다.",
    "선악의 경계는 끔찍할 정도로 모호하다.",
    "내 소설의 인물들은 실현되지 않은 나 자신의 가능성들이다.",
    "소설은 작가의 고백이 아니라 함정으로 변한 이 세계에서 인간 삶을 찾아 탐사하는 것이다.",
    "키치는 인간 조건의 한 부분이다.",
    "인간의 참된 선의는 아무런 힘도 지니지 않은 사람들에 대해서만 순수하고 자유롭게 베풀어질 수 있다.",
    "이미 아는 것들 속에서 뱅뱅 도는 삶. 그 단조로움은 권태가 아니라 행복이다."

]

def main():
    # 상태 초기화
    if "show_fortune" not in st.session_state:
        st.session_state.show_fortune = False
        st.session_state.fortune_message = ""

    # 페이지 제목 (가운데 정렬 및 글씨 크기 조정)
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>밀란 쿤데라의 포춘쿠키</h1>", unsafe_allow_html=True)
    
    # 이미지 표시 (이미지 파일 경로를 'fortune_cookie.png'로 가정)
    st.image("fortune_cookie1.png", use_column_width=True)

    # 버튼 클릭 시 상태 변경
    if st.button("포춘쿠키 열기"):
        st.session_state.show_fortune = True
        st.session_state.fortune_message = random.choice(fortunes)

    # 메시지 화면 표시
    if st.session_state.show_fortune:
        st.markdown("<h2 style='text-align: center; font-size: 24px;'>🥠 오늘의 구절 🥠:</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-size: 20px;'>{st.session_state.fortune_message}</h3>", unsafe_allow_html=True)
        if st.button("다시 열기"):
            st.session_state.show_fortune = False  # 초기 화면으로 돌아가기

if __name__ == "__main__":
    main()
