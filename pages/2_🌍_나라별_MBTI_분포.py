import streamlit as st

st.set_page_config(page_title="나라별 MBTI 분포", page_icon="🌍", layout="centered")

st.title("🌍 나라별 MBTI 분포 비교")
st.write("나라마다 문화와 가치관이 다르기 때문에 MBTI 유형의 분포도 조금씩 달라요. 궁금한 나라를 선택해보세요! 🧳")

# 나라별 상위 MBTI 유형 예시 데이터 (%) - 여러 자료를 참고해 재구성한 예시 데이터
country_data = {
    "🇰🇷 한국": {
        "ISTJ": 15.0, "ESTJ": 12.4, "ENFP": 9.7, "ISFJ": 8.3, "ESFJ": 8.2,
    },
    "🇺🇸 미국": {
        "ISFJ": 13.8, "ESFJ": 12.3, "ISTJ": 11.6, "ISFP": 8.8, "ESTJ": 8.7,
    },
    "🇯🇵 일본": {
        "ISFJ": 14.0, "ISTJ": 12.5, "ISFP": 10.0, "INFP": 8.5, "ESFJ": 8.0,
    },
    "🇨🇳 중국": {
        "ISTJ": 13.0, "ISFJ": 11.5, "ESTJ": 10.5, "ISTP": 9.0, "ENFP": 7.5,
    },
    "🇧🇷 브라질": {
        "ESFJ": 12.5, "ESFP": 11.0, "ENFP": 10.0, "ISFJ": 9.5, "ESTJ": 8.5,
    },
    "🇩🇪 독일": {
        "ISTJ": 12.0, "INTJ": 9.5, "ISFJ": 9.0, "ESTJ": 8.5, "INTP": 7.5,
    },
}

selected_country = st.selectbox("👉 나라를 선택해주세요", list(country_data.keys()))

st.subheader(f"{selected_country}의 상위 MBTI 유형 Top 5")
st.bar_chart(country_data[selected_country])

st.divider()
st.write("### 🗺️ 전체 나라 한눈에 비교하기")
top_type_by_country = {c: list(d.items())[0] for c, d in country_data.items()}
for country, (mbti, pct) in top_type_by_country.items():
    st.write(f"- {country} → 가장 많은 유형: **{mbti}** (약 {pct}%)")

st.info(
    "💡 위 데이터는 여러 공개 자료를 참고해 재구성한 **예시 데이터**예요. "
    "실제 정밀 통계는 조사 기관, 표본, 시기에 따라 달라질 수 있으니 흥미 위주로 참고해주세요 😊"
)
