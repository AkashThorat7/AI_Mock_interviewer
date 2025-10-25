from langgraph.graph import StateGraph, END
from typing import TypedDict
from pathlib import Path
import time, pygame, numpy as np, sounddevice as sd
from scipy.io.wavfile import write
from prompt import groq_client, generate_interview_questions, summarize_interview_prompt

# ------------------------
# Define Interview State
# ------------------------
class InterviewState(TypedDict):
    role: str
    round_type: str
    questions: list
    current_q: int
    answers: list
    feedback: list
    interview_history: dict
    answer_file: str
    answer_text: str
    current_question: str
    final_feedback: str


# ------------------------
# Helper Functions
# ------------------------
def record_audio(filename: str, duration=10):
    fs = 44100
    print("🎙️ Recording started — speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    scaled = np.int16(audio / np.max(np.abs(audio)) * 32767)
    write(filename, fs, scaled)
    print(f"✅ Recording saved at: {filename}")

# ------------------------
# Graph Node Functions
# ------------------------
def generate_questions(state: InterviewState):
    questions = generate_interview_questions(state["role"], state["round_type"])
    print("\n✅ Generated Questions:\n", questions)
    return {
        "questions": questions,
        "current_q": 0,
        "answers": [],
        "interview_history": {}
    }


def ask_question_tts(state: InterviewState):
    q_index = state["current_q"]
    question = state["questions"][q_index]
    output_folder = Path(__file__).parent / "tts_audio"
    output_folder.mkdir(exist_ok=True)
    file_path = output_folder / f"question_{q_index+1}.wav"

    print(f"🗣️ Asking Question {q_index+1}: {question}")

    response = groq_client.audio.speech.create(
        model="playai-tts",
        voice="Aaliyah-PlayAI",
        response_format="wav",
        input=question,
    )
    response.write_to_file(file_path)

    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    return {"current_q": q_index, "current_question": question}


def record_answer(state: InterviewState):
    q_index = state["current_q"]

    # ✅ Create "answers" folder inside project
    answers_folder = Path(__file__).parent / "outputs"
    answers_folder.mkdir(exist_ok=True)

    # ✅ Save audio file inside "answers" folder
    audio_file = answers_folder / f"answer_{q_index+1}.wav"

    record_audio(filename=str(audio_file), duration=30)
    state["answer_file"] = str(audio_file)
    print(f"🎧 Recorded answer saved as: {audio_file}")

    if "interview_history" not in state:
        state["interview_history"] = {}

    question = state["questions"][q_index]
    state["interview_history"][question] = "[Audio recorded, not yet transcribed]"
    return state


def transcribe_answer(state: InterviewState):
    file_path = state.get("answer_file")
    if not file_path or not Path(file_path).exists():
        print("⚠️ No valid audio file found for this question.")
        return state

    question = state["questions"][state["current_q"]]
    with open(file_path, "rb") as f:
        transcription = groq_client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=f,
        )

    answer_text = transcription.text.strip()
    print(f"📝 Transcribed Answer: {answer_text}")
    state["interview_history"][question] = answer_text
    state["answer_text"] = answer_text
    return state


def evaluate_answer(state: InterviewState):
    q_index = state["current_q"]
    questions = state["questions"]
    ans = state.get("answer_text", "")
    state["answers"].append(ans)
    question = questions[q_index]
    state["interview_history"][question] = ans
    state["current_q"] += 1

    if state["current_q"] >= len(questions):
        print("\n🎯 All questions completed — generating feedback...\n")
        summary_text = summarize_interview_prompt(state["interview_history"], questions)
        state["final_feedback"] = summary_text
        return state
    return state


# ------------------------
# Build LangGraph
# ------------------------
def build_interview_graph():
    graph = StateGraph(InterviewState)

    graph.add_node("generate_questions", generate_questions)
    graph.add_node("ask_question_tts", ask_question_tts)
    graph.add_node("record_answer", record_answer)
    graph.add_node("transcribe_answer", transcribe_answer)
    graph.add_node("evaluate_answer", evaluate_answer)

    graph.set_entry_point("generate_questions")

    graph.add_edge("generate_questions", "ask_question_tts")
    graph.add_edge("ask_question_tts", "record_answer")
    graph.add_edge("record_answer", "transcribe_answer")
    graph.add_edge("transcribe_answer", "evaluate_answer")
    

    def continue_or_end(state: InterviewState):
        return "ask_question_tts" if state["current_q"] < len(state["questions"]) else END

    graph.add_conditional_edges("evaluate_answer", continue_or_end, {
        "ask_question_tts": "ask_question_tts",
        END: END
    })

    return graph.compile()



