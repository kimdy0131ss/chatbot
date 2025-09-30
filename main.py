import streamlit as st
import requests

API_URL = "https://api.upstage.ai/v1/chat/completions"
API_KEY = "up_k0KqmdLq53BmsKWzLoAwKpZzgQoE0"


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role":"system", "content":"넌 간단한 질문들, 말에 대답해주는 말동무같은 존재야. '솔라'라는 키워드는 절대 사용 불가야."}
    ]


st.title("예제")
user_input = st.chat_input("여기에 메시지를 입력하시오")

if user_input:
    st.session_state.messages.append({"role":"user", "content":user_input})
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "solar-pro",
        "messages": st.session_state.messages
    }

    with st.spinner("🤖 챗봇이 생각 중입니다..."):
        response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role":"assistant", "content":reply})
    else:
        reply = "오류 발생"
    
    st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    elif msg["role"] == "user":
        st.markdown(f"**👤 사용자:** {msg['content']}")
    else:
        st.markdown(f"**🤖 챗봇:** {msg['content']}")
