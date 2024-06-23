import streamlit as st


def quiz():
    questions = [
        {
            "question": "Które z poniższych najlepiej definiuje 'dane'?",
            "options": ["A) Zorganizowane fakty, które mają znaczenie dla użytkownika.",
                        "B) Surowe, nieprzetworzone fakty i liczby bez kontekstu.",
                        "C) Zrozumienie informacji, jej analiza i interpretacja.",
                        "D) Zdolność do podejmowania trafnych decyzji na podstawie wiedzy."],
            "answer": "B"
        },
        {
            "question": "Informacja to:",
            "options": ["A) Surowe fakty i liczby bez kontekstu.",
                        "B) Dane zorganizowane lub przetworzone w sposób, który nadaje im kontekst.",
                        "C) Zrozumienie i interpretacja danych.",
                        "D) Zdolność do podejmowania decyzji na podstawie wiedzy."],
            "answer": "B"
        },
        {
            "question": "Wiedza to:",
            "options": ["A) Dane zorganizowane lub przetworzone w sposób, który nadaje im kontekst.",
                        "B) Zrozumienie informacji, jej analiza i interpretacja.",
                        "C) Zdolność do podejmowania trafnych decyzji na podstawie informacji.",
                        "D) Surowe, nieprzetworzone fakty i liczby."],
            "answer": "B"
        },
        {
            "question": "Mądrość to:",
            "options": ["A) Surowe, nieprzetworzone fakty i liczby.",
                        "B) Zrozumienie informacji, jej analiza i interpretacja.",
                        "C) Zdolność do podejmowania trafnych decyzji na podstawie wiedzy.",
                        "D) Dane zorganizowane lub przetworzone w sposób, który nadaje im kontekst."],
            "answer": "C"
        },
        {
            "question": "Które z poniższych jest kryterium oceny jakości informacji?",
            "options": ["A) Dyspozycyjność",
                        "B) Różnorodność",
                        "C) Ilość",
                        "D) Złożoność"],
            "answer": "A"
        },
        {
            "question": "Które z poniższych NIE jest kryterium oceny jakości informacji?",
            "options": ["A) Dyspozycyjność",
                        "B) Dokładność",
                        "C) Aktualność",
                        "D) Użyteczność"],
            "answer": "D"
        },
        {
            "question": "System informacyjny to:",
            "options": ["A) System przechowujący, przetwarzający i przekazujący informacje.",
                        "B) System skupiający się tylko na przechowywaniu danych.",
                        "C) Tylko sprzęt komputerowy i oprogramowanie.",
                        "D) Tylko sieci komputerowe."],
            "answer": "A"
        },
        {
            "question": "System informatyczny to:",
            "options": ["A) System skupiający się na przetwarzaniu danych przy użyciu technologii informacyjnych.",
                        "B) System skupiający się tylko na przechowywaniu danych.",
                        "C) Tylko sieci komputerowe.",
                        "D) System przechowujący, przetwarzający i przekazujący informacje."],
            "answer": "A"
        },
        {
            "question": "System komputerowy to:",
            "options": ["A) Zbiór sprzętu komputerowego, oprogramowania i sieci komputerowych.",
                        "B) System przechowujący, przetwarzający i przekazujący informacje.",
                        "C) System skupiający się tylko na przechowywaniu danych.",
                        "D) Zbiór sprzętu komputerowego i procesów biznesowych firmy."],
            "answer": "A"
        },
        {
            "question": "Który z poniższych elementów NIE jest typowym składnikiem systemu informacyjnego?",
            "options": ["A) Sprzęt komputerowy",
                        "B) Oprogramowanie",
                        "C) Procesy informacyjne",
                        "D) Interfejs użytkownika"],
            "answer": "D"
        }
    ]

    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

    st.title("Quiz z przetwarzania danych")

    if not st.session_state.quiz_started:
        if st.button("Rozpocznij quiz"):
            st.session_state.quiz_started = True
            st.experimental_rerun()

    if st.session_state.quiz_started:
        if st.session_state.question_index < len(questions):
            question = questions[st.session_state.question_index]
            st.write(f"\n**Pytanie {st.session_state.question_index + 1}:** {question['question']}")

            user_answer = st.radio("Twoja odpowiedź:", options=question['options'],
                                   key=str(st.session_state.question_index))

            if st.button("Następne pytanie"):
                st.session_state.user_answers.append(user_answer)
                if user_answer.startswith(question['answer']):
                    st.session_state.score += 1
                st.session_state.question_index += 1
                st.experimental_rerun()

        else:
            st.write(f"\n**Quiz zakończony! Twój wynik to:** {st.session_state.score}/{len(questions)}")

            st.write("\n**Lista poprawnych odpowiedzi:**")
            for idx, question in enumerate(questions):
                correct_option = question['options'][ord(question['answer']) - ord('A')]
                user_answer = st.session_state.user_answers[idx]
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
                st.experimental_rerun()


if __name__ == "__main__":
    quiz()