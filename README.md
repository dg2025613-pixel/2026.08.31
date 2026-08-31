# 🧭 청소년 진로 상담소

고등학생을 위한 MBTI 기반 직업 추천 웹앱입니다.
자신의 MBTI 유형을 선택하면, 그 유형에 어울리는 직업 3가지를 이모지와 함께 추천해줍니다 ✨

## 📌 소개

- 대상: 진로를 고민하는 고등학생
- 방식: MBTI 16개 유형 중 하나를 선택 → 맞춤 직업 3가지와 설명 제공
- 별도 라이브러리 설치 없이 Streamlit 기본 기능만으로 구현
- 페이지 이동 없이 메인 화면 하나로 모든 기능 제공

## 🛠️ 사용 기술

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## 🚀 실행 방법

### 1. 저장소 클론
```bash
git clone <이 저장소의 URL>
cd <저장소 폴더>
```

### 2. 필요한 패키지 설치
```bash
pip install streamlit
```

### 3. 앱 실행
```bash
streamlit run main.py
```

실행 후 브라우저에서 `http://localhost:8501` 로 접속하면 앱을 확인할 수 있어요.

## ☁️ Streamlit Cloud로 배포하기

1. 이 저장소를 본인의 GitHub 계정으로 fork 하거나 push 합니다.
2. [Streamlit Community Cloud](https://streamlit.io/cloud)에 로그인합니다.
3. `New app`을 클릭하고 저장소, 브랜치, Main file path(`main.py`)를 지정합니다.
4. `Deploy` 버튼을 누르면 몇 분 안에 배포가 완료됩니다.

## 📁 파일 구성

```
.
├── main.py         # Streamlit 앱 메인 코드
└── README.md        # 프로젝트 설명 파일
```

## 💡 참고 사항

이 앱에서 제공하는 직업 추천은 MBTI 성격 유형의 일반적인 경향을 참고한 것으로, 재미와 진로 탐색의 출발점으로 활용하시길 권장해요. 실제 진로 선택은 개인의 흥미, 적성, 가치관을 종합적으로 고려해 천천히 찾아가는 것이 좋습니다 🌱

---

🌈 Made with ❤️ for 고등학생 여러분의 꿈을 응원합니다!
