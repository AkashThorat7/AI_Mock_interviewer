import streamlit as st
from graph import build_interview_graph
import os


st.set_page_config(page_title="🎤 Virtual AI Interview", layout="centered")


st.markdown("""
    <style>
        .main-container { background-color: #f7f9fc; padding: 2rem; border-radius: 15px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);}
        .question-card { background-color: #ffffff; padding: 1.5rem; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0px 3px 12px rgba(0,0,0,0.1);}
        .feedback-box { background-color: #eaf4ff; border-left: 5px solid #007bff; padding: 1rem; border-radius: 10px; margin-top: 1rem;}
        .record-btn { background-color: #ff4b4b; color: white; border: none; padding: 10px 25px; border-radius: 25px; font-size: 16px; cursor: pointer;}
        .record-btn:hover { background-color: #e63e3e;}
        .stop-btn { background-color: #007bff; color: white; border: none; padding: 10px 25px; border-radius: 25px; font-size: 16px; cursor: pointer;}
        .stop-btn:hover { background-color: #005dc1;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Virtual AI Interviewer")
st.caption("A realistic mock interview powered by **Groq + LangGraph + Streamlit**")


if "app" not in st.session_state: st.session_state.app = None
if "state" not in st.session_state: st.session_state.state = None
if "started" not in st.session_state: st.session_state.started = False
if "current_question" not in st.session_state: st.session_state.current_question = ""
if "feedback" not in st.session_state: st.session_state.feedback = ""
if "done" not in st.session_state: st.session_state.done = False
if "asked_question" not in st.session_state: st.session_state.asked_question = False

# Sidebar Setup

st.sidebar.header("🎯 Interview Setup")
role = st.sidebar.text_input("Role (e.g., Data Scientist)")
round_type = st.sidebar.text_input("Round Type (e.g., Technical)")
duration = st.sidebar.slider("Recording Duration (seconds)", 10, 45, 20)
start_btn = st.sidebar.button("🚀 Start Interview")

if start_btn:
    if not role or not round_type:
        st.sidebar.warning("⚠️ Please fill in both Role and Round Type.")
    else:
        st.session_state.app = build_interview_graph()
        # Initialize state with role, round_type, empty history, question index
        st.session_state.state = {
            "role": role,
            "round_type": round_type,
            "questions": [],
            "current_q": 0,
            "interview_history": {},
            "final_feedback": ""
        }
        st.session_state.started = True
        st.session_state.done = False
        st.session_state.asked_question = False
        st.session_state.feedback = ""
        st.sidebar.success("✅ Interview setup complete! Click below to begin.")
        st.balloons()

# Interview Section

if st.session_state.started and not st.session_state.done:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("## 🎙️ Virtual Interview Session")

    # Button to ask/generate next question
    if st.button("🗣️ AI Ask Question") or st.session_state.asked_question:
        if not st.session_state.asked_question:
            st.session_state.asked_question = True
            app = st.session_state.app
            state = st.session_state.state

            # Invoke agent to generate next question
            result = app.invoke(state)
            st.session_state.state = result

            # Get current question
            current_index = result.get("current_q", 0)
            print(current_index)
            questions = result.get("questions", [])
            print(f" streamlit Questions: {questions}")
            st.session_state.current_question = questions[current_index] if current_index < len(questions) else "No more questions."

    # Display current question
    if st.session_state.current_question:
        st.markdown(f"""
        <div class="question-card">
            <h3>💬 Question:</h3>
            <p style="font-size:18px;">{st.session_state.current_question}</p>
        </div>
        """, unsafe_allow_html=True)

   
    if st.session_state.current_question == "No more questions.":
        st.session_state.done = True
        st.session_state.feedback = st.session_state.state.get("final_feedback", "No feedback generated.")
        st.balloons()

# Final Feedback Section

if st.session_state.done:
    st.markdown("---")
    st.subheader("🧾 Final Feedback Report")
    feedback = st.session_state.feedback

    st.markdown(f"""
    <div class="feedback-box">
        <b>⭐ Overall Evaluation:</b><br>
        <p style="font-size:16px; line-height:1.6;">{feedback}</p>
    </div>
    """, unsafe_allow_html=True)

    st.download_button(
        label="📥 Download Feedback Report",
        data=feedback.encode("utf-8"),
        file_name=f"{role}_{round_type}_feedback.txt",
        mime="text/plain"
    )

    st.subheader("🗂️ Interview Summary")
    for q, a in st.session_state.state.get("interview_history", {}).items():
        with st.expander(f"💬 {q}"):
            st.write(f"**Answer:** {a}")

st.markdown("---")
st.caption("🎧 *Tip: Use headphones and a quiet environment for the best results.*")

