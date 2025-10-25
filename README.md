# AI Interview Coach

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

<img width="1348" height="782" alt="Screenshot 2025-08-03 at 1 25 39 PM" src="https://github.com/user-attachments/assets/2d3ea4e3-e870-4df4-9384-ffd82d6649c1" />
<img width="1349" height="783" alt="Screenshot 2025-08-03 at 1 26 19 PM" src="https://github.com/user-attachments/assets/ba189d24-ecb9-4b04-bea6-cab5c7bdb98e" />
<img width="1350" height="783" alt="Screenshot 2025-08-03 at 1 26 50 PM" src="https://github.com/user-attachments/assets/332c8184-045c-4df5-ab8c-4bd2092bd190" />
<img width="1343" height="785" alt="Screenshot 2025-08-03 at 1 27 32 PM" src="https://github.com/user-attachments/assets/74797b75-46da-43c4-b7d3-4b3114f7c35d" />
<img width="1353" height="784" alt="Screenshot 2025-08-03 at 1 28 34 PM" src="https://github.com/user-attachments/assets/d806d806-d76c-4dc6-8da7-b4600df69fc6" />

---

## 🛠 Tech Stack

| Component        | Tech Used                |
|------------------|--------------------------|
| Frontend UI      | Streamlit                |
| Voice Input      | Streamlit audio input + Whisper    |
| Speech Output    | gTTS                     |
| AI Engine        | Gemini API               |
| Core Logic       | Python                   |
| Deployment       | Streamlit Cloud          |

---

## 🧠 Key Learnings

- **Voice Integration in Web Apps**: Learned to integrate real-time voice recording using `sounddevice` (changed to streamlit audio input), and send the audio to OpenAI’s **Whisper** for seamless transcription.

- **Prompt Engineering for Dual Roles & Difficulty Scaling**: Refined prompt structures for two key tasks: generating interview questions and evaluating user responses. Also learned to dynamically scale difficulty using prompt tweaks.

- **Streamlit UI Implementation**: Built a clean, voice-first interface using **Streamlit**, ensuring smooth interaction across devices.

- **Gemini API Integration**: Successfully integrated **Google Gemini** to generate questions and evaluate responses. Learned to handle token limits, structure prompts effectively, and parse replies into actionable feedback.

---

## 📈 Future Scope

- Store user history, show progress graphs
- Add emotion analysis or confidence rating
- Export transcripts + feedback as PDF
- Replace gTTS with more natural TTS like ElevenLabs

---
**Created By: Chhavi Dhankhar**
