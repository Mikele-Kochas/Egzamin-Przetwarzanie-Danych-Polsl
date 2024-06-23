import streamlit as st
import random

def shuffle_options(question):
    options = question['options']
    correct_answer = question['answer']
    correct_option = options[ord(correct_answer) - ord('A')]

    shuffled_options = random.sample(options, len(options))
    new_correct_index = shuffled_options.index(correct_option)
    new_correct_letter = chr(ord('A') + new_correct_index)

    return {
        'question': question['question'],
        'options': shuffled_options,
        'answer': new_correct_letter
    }

def quiz():
    original_questions = [
        {
            "question": "Czym charakteryzują się systemy ewidencyjne?",
            "options": ["A) Analizują strategiczne problemy decyzyjne",
                        "B) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                        "C) Informują o stanie obiektu i jego poszczególnych parametrach",
                        "D) Dokonują inteligentnej analizy danych"],
            "answer": "B"
        },
        {
            "question": "Jakie zadanie mają systemy informowania kierownictwa?",
            "options": ["A) Informują o stanie obiektu i jego poszczególnych parametrach",
                        "B) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                        "C) Analizują strategiczne problemy decyzyjne",
                        "D) Dokonują inteligentnej analizy danych"],
            "answer": "A"
        },
        {
            "question": "Co charakteryzuje systemy wspomagania decyzji?",
            "options": ["A) Informują o stanie obiektu i jego poszczególnych parametrach",
                        "B) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                        "C) Analizują strategiczne problemy decyzyjne",
                        "D) Dokonują analizy danych z wykorzystaniem sztucznej inteligencji"],
            "answer": "C"
        },
        {
            "question": "Czym charakteryzują się systemy ekspertowe?",
            "options": ["A) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                        "B) Informują o stanie obiektu i jego poszczególnych parametrach",
                        "C) Analizują strategiczne problemy decyzyjne",
                        "D) Są 'samouczące się', dokonują inteligentnej analizy danych"],
            "answer": "D"
        }
    ]

    if 'shuffled_questions' not in st.session_state:
        st.session_state.shuffled_questions = [shuffle_options(q) for q in random.sample(original_questions, len(original_questions))]

    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

    st.title("Quiz z systemów informatycznych")

    if not st.session_state.quiz_started:
        if st.button("Rozpocznij quiz"):
            st.session_state.quiz_started = True
            st.experimental_rerun()

    if st.session_state.quiz_started:
        if st.session_state.question_index < len(st.session_state.shuffled_questions):
            question = st.session_state.shuffled_questions[st.session_state.question_index]
            st.write(f"\n**Pytanie {st.session_state.question_index + 1}:** {question['question']}")

            options = [f"{chr(65 + i)}) {option.split(')', 1)[1].strip()}" for i, option in enumerate(question['options'])]
            user_answer = st.radio("Twoja odpowiedź:", options, key=str(st.session_state.question_index))

            if st.button("Następne pytanie"):
                st.session_state.user_answers.append(user_answer)
                if user_answer.startswith(question['answer']):
                    st.session_state.score += 1
                st.session_state.question_index += 1
                st.experimental_rerun()

        else:
            st.write(f"\n**Quiz zakończony! Twój wynik to:** {st.session_state.score}/{len(st.session_state.shuffled_questions)}")

            st.write("\n**Lista poprawnych odpowiedzi:**")
            for idx, (question, user_answer) in enumerate(zip(st.session_state.shuffled_questions, st.session_state.user_answers)):
                correct_option = question['options'][ord(question['answer']) - ord('A')]
                is_correct = user_answer.startswith(question['answer'])

                st.write(f"{idx + 1}. {question['question']}")
                st.write(f"   Poprawna odpowiedź: {correct_option}")
                st.write(f"   Twoja odpowiedź: {user_answer}")
                st.write(f"   {'✅ Poprawnie' if is_correct else '❌ Niepoprawnie'}")
                st.write("")

            if st.button("Rozpocznij quiz ponownie"):
                st.session_state.score = 0
                st.session_state.question_index = 0
                st.session_state.user_answers = []
                st.session_state.shuffled_questions = [shuffle_options(q) for q in random.sample(original_questions, len(original_questions))]
                st.experimental_rerun()

if __name__ == "__main__":
    quiz()
