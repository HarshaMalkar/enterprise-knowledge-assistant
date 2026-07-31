import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/query"

st.set_page_config(
    page_title="Smart AI Workspace",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.main-title{
    text-align:center;
    color:#4F46E5;
    font-size:42px;
    font-weight:bold;
}
.answer-box{
    padding:15px;
    border-radius:10px;
    background:#F3F4F6;
    color:black;
}
</style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.title("🚀 Smart AI Workspace")
st.sidebar.success("Backend Connected")

if st.sidebar.button("🗑 Clear History"):
    st.session_state.history = []
    st.rerun()

st.markdown(
    '<p class="main-title">🤖 Smart AI Workspace</p>',
    unsafe_allow_html=True
)

st.write("Ask questions from your Enterprise Knowledge Base")

question = st.text_area(
    "Question",
    placeholder="Enter your question...",
    height=120
)

if st.button("🔍 Ask Question", use_container_width=True):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        with st.spinner("Searching knowledge base..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=300
                )

                response.raise_for_status()

                data = response.json()

                st.session_state.history.append(data)

            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")

if st.session_state.history:

    st.subheader("💬 Conversation History")

    for item in reversed(st.session_state.history):

        with st.container(border=True):

            st.markdown(
                f"### ❓ {item.get('question','')}"
            )

            st.markdown(
                f"""
                <div class="answer-box">
                {item.get('answer','No Answer')}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.caption(
                f"⏰ {item.get('timestamp','')}"
            )

            citations = item.get("citations", [])

            if citations:

                with st.expander("📚 Sources"):

                    for source in citations:

                        st.json(source)