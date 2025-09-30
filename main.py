import streamlit as st
import requests

API_URL = "https://api.upstage.ai/v1/chat/completions"
API_KEY = "up_k0KqmdLq53BmsKWzLoAwKpZzgQoE0"

with st.container():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role":"system", "content":"넌 간단한 질문들, 말에 대답해주는 말동무같은 존재야. '솔라'라는 키워드는 절대 사용 불가야."}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "system":
            continue
        elif msg["role"] == "user":
            st.markdown(f"**👤 사용자:** {msg['content']}")
        else:
            st.markdown(f"**🤖 챗봇:** {msg['content']}")

    st.title("예제")
    st.markdown("<div id='scroll-anchor'></div>", unsafe_allow_html=True)
    user_input = st.chat_input("여기에 메시지를 입력하시오")

    if user_input:
        st.session_state.messages.append({"role":"user", "content":user_input})

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "solar-1-mini-chat",
            "messages": st.session_state.messages
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role":"assistant", "content":reply})
        else:
            reply = "오류 발생"

    st.markdown("""
        <script>
            const anchor = document.getElementById("scroll-anchor");
            if (anchor) {
                anchor.scrollIntoView({ behavior: "smooth", block: "end" });
            }
        </script>
    """, unsafe_allow_html=True)
