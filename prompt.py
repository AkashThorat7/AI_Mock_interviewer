from langchain_groq import ChatGroq
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

qa_llm = ChatGroq(model="llama-3.1-8b-instant")
eval_llm = ChatGroq(model="llama-3.1-8b-instant")
groq_client = Groq(api_key=GROQ_API_KEY)



def generate_interview_questions(role: str, round_type: str):

    first_question = "Tell me about yourself?"
    prompt = f"""
                You are an expert technical interviewer with deep knowledge of current industry hiring trends.

                The interview is for the role of "{role}" and the round type is "{round_type}".
                Research and consider the most frequently asked and trending questions from top companies and credible job sites (e.g., Glassdoor, LeetCode Discuss, InterviewBit, LinkedIn, GeeksforGeeks, Indeed).

                Based on that, generate 2 highly relevant, unique, and realistic interview questions specifically for this role and round type.
                Each question should be:
                - one question not more lengthy than a single sentence.
                - generate most of all question theoretical dont generate ant practical implementation question .
                - Concise and directly related to real interview scenarios.
                - Professionally worded (avoid generic phrasing like "Explain about yourself").
                - Focused on practical or conceptual depth depending on the round type.

                Do NOT include duplicates or introductory questions such as “Tell me about yourself.”
                Return only the questions, one per line, without numbering or extra explanation.

    """
    response = qa_llm.predict(prompt)

    other_questions = [
        q.strip("1234567890. ").strip()
        for q in response.split("\n")
        if q.strip() and "tell me about yourself" not in q.lower()
    ]

    questions = [first_question] + other_questions[:2]
    return questions


def summarize_interview_prompt(interview_history: dict, questions: list):

    qna_text = "\n".join(
        [f"Q: {q}\nA: {interview_history.get(q, '')}\n" for q in questions]
    )

    summary_prompt = f"""
    You are a professional technical interview evaluator and hiring expert.

    Here is the full interview transcript (questions and candidate answers):
    {qna_text}

    Based on the transcript, write a structured and detailed feedback report covering:

    1. **Overall Performance Summary** – Provide a concise overview of how the candidate performed in this interview, mentioning communication, confidence, technical accuracy, and logical thinking.
    2. **Key Strengths** – Highlight the candidate’s notable skills, knowledge areas, and strong responses.
    3. **Areas for Improvement** – Identify specific gaps, weak explanations, or skills that need development.
    4. **Final Rating (out of 10)** – Give a fair and realistic numeric rating that reflects the overall impression.

    Ensure the feedback tone is **professional, balanced, and constructive**, as if it were written by a real interviewer for an internal evaluation report.
    Do not repeat the transcript or questions. Keep it natural and analytical.
    """

    resp = eval_llm.invoke(summary_prompt)
    summary_text = getattr(resp, "content", None) or getattr(resp, "text", None) or str(resp)
    return summary_text
