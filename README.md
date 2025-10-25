# AI Mock Interviewer Using AI Agent

[![Streamlit](https://img.shields.io/badge/Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io/) 
[![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue?logo=python&logoColor=white)](https://www.python.org/) 
[![Speech to Text - Whisper](https://img.shields.io/badge/Speech%20to%20Text-Whisper-blueviolet?logo=openai&logoColor=white)](https://github.com/openai/whisper) 
[![LangGraph](https://img.shields.io/badge/LangGraph-orange?logo=python&logoColor=white)](https://www.langchain.com/langgraph) 
[![Groq](https://img.shields.io/badge/Groq-ff69b4?logo=groq&logoColor=white)](https://www.groq.com/) 
[![AI Agent](https://img.shields.io/badge/AI%20Agent-lightgrey?logo=robot&logoColor=white)](https://en.wikipedia.org/wiki/Intelligent_agent)
[![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)]()

# AI Mock Interviewer using AI Agent

Your personal AI-powered mock interview assistant, designed to help you prepare confidently for real-world job interviews.

🔗 [[Demo Coming Soon]]

This app simulates an actual interview environment by asking role- and round-specific questions. You can speak your answers out loud, get real-time transcription, and receive AI-generated feedback to improve your structure, clarity, and confidence.

---

## ☕️ Project Goals

AI Mock Interviewer was built to address a common problem: students and candidates often skip mock interviews and struggle during real interviews due to lack of preparation. This app helps you:

* Practice in a private, AI-driven environment before real interviews
* Learn to tackle both technical and HR questions effectively
* Receive structured, repeatable feedback
* Build confidence by speaking answers aloud and iterating based on feedback

---

## 💬 Features

* **Role & Round Type–Driven Interviews**: Provide your role and interview round type (e.g., Technical, HR), and the app generates tailored questions using AI, including trending and relevant content.

* **Voice-First Experience**: Speak your answers aloud using your microphone. The app transcribes your speech in real-time using **Whisper** or a similar STT model and responds via audio using **gTTS** or another TTS model.

* **AI Feedback in Real Time**: After each answer, the LLM evaluates your response and gives feedback on clarity, relevance, structure, technical correctness, and overall delivery.

* **Difficulty Modes**: Select **Beginner**, **Intermediate**, or **Advanced** to adjust question complexity according to your preparation level.

* **Streamlit-Powered UI**: Mobile-friendly interface with minimal clicks, smooth interaction between voice input, transcription, and feedback display.

* **Future Enhancements**: Improve prompt generation for questions and feedback summaries, integrate real-time communication using WebRTC, add additional parameters like skills and seniority for personalized questions, and build an analytics dashboard to track progress.

---

This README provides an overview of the AI Mock Interviewer, its goals, features, and future plans for improving user experience and interactivity.

## 💻 UI Preview

<img width="1348" height="782" alt="Screenshot 2025-08-03 at 1 25 39 PM" src="https://github.com/AkashThorat7/AI_Mock_interviewer/blob/main/assets/first.jpg" />
<img width="1349" height="783" alt="Screenshot 2025-08-03 at 1 26 19 PM" src="https://github.com/AkashThorat7/AI_Mock_interviewer/blob/main/assets/second.jpg" />
<img width="1343" height="785" alt="Screenshot 2025-08-03 at 1 27 32 PM" src="https://github.com/AkashThorat7/AI_Mock_interviewer/blob/main/assets/third.jpg" />

---

## 🛠 Tech Stack

| Component        | Tech Used                |
|------------------|--------------------------|
| Frontend UI      | Streamlit                |
| Voice Input      | streamlit audio input + Whisper   |
| Speech Output    | gTTS                     |
| AI Agent         | Langgraph                |
| Core Logic       | Python                   |
| LLM              | Groq API                 |
| Deployment       | Streamlit Cloud          |


---

## Key Learnings

Voice Integration in Web Apps: Learned to capture real-time audio using Streamlit audio input, and process it with OpenAI Whisper for seamless transcription.

Prompt Engineering for Role & Round: Refined prompts to generate interview questions and evaluate answers effectively. Learned to dynamically adjust difficulty using prompt tweaks.

Streamlit UI Implementation: Built a clean, voice-first interface, ensuring smooth interaction across devices.

AI Feedback System Integration: Integrated Groq LLM to generate questions and evaluate responses. Learned to manage token limits, structure prompts efficiently, and parse replies into actionable feedback.

System Orchestration & Agent Graphs: Implemented a multi-step agent flow using LangGraph to manage question generation, TTS playback, recording, STT transcription, and evaluation.

Performance Optimization: Learned techniques to reduce latency, handle concurrency, and ensure real-time responsiveness in multi-component AI systems.
---



---
**Created By: Akash Thorat**
