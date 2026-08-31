import streamlit as st

st.set_page_config(page_title="한국 MBTI 비율", page_icon="🇰🇷", layout="centered")

st.title("🇰🇷 우리나라 MBTI 유형 비율")
st.write("국내 여러 조사 자료를 참고해 정리한 한국인의 MBTI 유형별 대략적인 비율이에요 📊")

# 국내 MBTI 유형별 대략적인 비율 (%)
korea_mbti_ratio = {
    "ISTJ": 15.0,
    "ESTJ": 12.4,
    "ENFP": 9.7,
    "ISFJ": 8.3,
    "ESFJ": 8.2,
    "ISTP": 7.0,
    "ISFP": 5.0,
    "ESFP": 5.0,
    "ESTP": 4.0,
    "ENTP": 4.0,
    "INFP": 4.0,
    "ENTJ": 3.5,
    "ENFJ": 3.3,
    "INTJ": 3.3,
    "INTP": 3.2,
    "INFJ": 2.9,
}

st.bar_chart(korea_mbti_ratio)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.metric("🥇 가장 많은 유형", "ISTJ", "약 15%")
with col2:
    st.metric("🌱 가장 희귀한 유형", "INFJ", "약 2.9%")

st.info(
    "💡 위 수치는 국내 MBTI 관련 조사 자료들을 참고해 재구성한 **추정치**예요. "
    "조사 기관과 시기에 따라 실제 비율은 다를 수 있으니 재미로 참고해주세요! 반올림으로 인해 합계가 정확히 100%가 아닐 수 있어요."
)

st.caption("🔍 참고: ISTJ·ESTJ 등 SJ 계열이 상대적으로 많고, INFJ·INTP 등 N 계열은 비교적 드문 편이에요.")
