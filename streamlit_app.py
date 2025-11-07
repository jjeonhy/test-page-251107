import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# ...existing code...
import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# ...existing code...
# 변경된 코드: 주사위 굴리기 앱 추가
import random
from datetime import datetime
import pandas as pd

st.title("🎲 간단한 주사위 굴리기 앱")

# 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("설정")
    count = st.slider("주사위 개수", 1, 10, 2)
    sides_option = st.selectbox("면 수", [4, 6, 8, 10, 12, 20, 100, "사용자 지정"])
    if sides_option == "사용자 지정":
        sides = st.number_input("사용자 지정 면 수", min_value=2, max_value=1000, value=6)
    else:
        sides = int(sides_option)
    seed = st.text_input("시드 (선택, 같은 문자열이면 동일한 결과)")
    roll_btn = st.button("굴리기")

if roll_btn:
    if seed:
        random.seed(seed)
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.history.insert(0, {"time": timestamp, "count": count, "sides": sides, "rolls": rolls, "total": total})

# 결과 표시
if st.session_state.history:
    latest = st.session_state.history[0]
    st.subheader("최근 결과")
    st.write(f"시간: {latest['time']}")
    st.write(f"{latest['count']}개 d{latest['sides']} 주사위 결과: {latest['rolls']}")
    st.metric("합계", latest["total"])
    # 간단한 막대그래프
    df = pd.DataFrame({"roll": latest["rolls"], "index": range(1, len(latest["rolls"]) + 1)})
    st.bar_chart(df.set_index("index"))

# 히스토리 보기
with st.expander("주사위 굴린 기록 보기"):
    if not st.session_state.history:
        st.write("아직 기록이 없습니다.")
    else:
        for i, entry in enumerate(st.session_state.history):
            st.write(f"{i+1}. [{entry['time']}] {entry['count']} x d{entry['sides']} → {entry['rolls']} (합: {entry['total']})")
        