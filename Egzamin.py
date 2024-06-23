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
        },
        {
            "question": "Co to jest funkcja ewidencji danych w systemie informatycznym?",
            "options": ["A) Zbieranie danych o istotnych parametrach organizacyjnych",
                        "B) Przechowywanie i zabezpieczanie danych",
                        "C) Sortowanie i przetwarzanie danych",
                        "D) Wyszukiwanie danych w celu uzyskania odpowiedzi"],
            "answer": "A"
        },
        {
            "question": "Jakie operacje można wykonywać w ramach funkcji przekształcania danych w systemie informatycznym?",
            "options": ["A) Bezpieczeństwo danych i ich dostępność",
                        "B) Wyszukiwanie i wyprowadzanie danych",
                        "C) Różnorodne operacje na danych, np. sortowanie, obliczenia",
                        "D) Określanie nośników danych i ich dostępności"],
            "answer": "C"
        },
        {
            "question": "Co obejmuje funkcja przechowywania danych w systemie informatycznym?",
            "options": ["A) Ewidencja i przekształcanie danych",
                        "B) Bezpieczeństwo danych i ich dostępność",
                        "C) Zbieranie danych o istotnych parametrach organizacyjnych",
                        "D) Określenie nośników danych i sposobu ich dostępu"],
            "answer": "B"
        },
        {
            "question": "Jakie są główne zadania funkcji ewidencji danych w systemie informatycznym?",
            "options": ["A) Zbieranie danych o istotnych parametrach organizacyjnych",
                        "B) Wyszukiwanie i wyprowadzanie danych",
                        "C) Przechowywanie i zabezpieczanie danych",
                        "D) Różnorodne operacje na danych, np. sortowanie, obliczenia"],
            "answer": "A"
        },
        {
            "question": "Czym charakteryzują się systemy ewidencyjne?",
            "options": [
                "A) Analizują strategiczne problemy decyzyjne",
                "B) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                "C) Informują o stanie obiektu i jego poszczególnych parametrach",
                "D) Dokonują inteligentnej analizy danych"
            ],
            "answer": "B"
        },
        {
            "question": "Jakie zadanie mają systemy informowania kierownictwa?",
            "options": [
                "A) Informują o stanie obiektu i jego poszczególnych parametrach",
                "B) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                "C) Analizują strategiczne problemy decyzyjne",
                "D) Dokonują inteligentnej analizy danych"
            ],
            "answer": "A"
        },
        {
            "question": "Czym charakteryzują się systemy ekspertowe?",
            "options": [
                "A) Tworzą zbiory elementarnych danych o funkcjonowaniu obiektu",
                "B) Informują o stanie obiektu i jego poszczególnych parametrach",
                "C) Analizują strategiczne problemy decyzyjne",
                "D) Są 'samouczące się', dokonują inteligentnej analizy danych"
            ],
            "answer": "D"
        },
        {
            "question": "Co obejmuje funkcja przekształcania danych w systemie informatycznym?",
            "options": ["A) Określanie nośników danych i ich dostępności",
                        "B) Różnorodne operacje na danych, np. sortowanie, obliczenia",
                        "C) Bezpieczeńwo danych i ich dostępność",
                        "D) Zbieranie danych o istotnych parametrach organizacyjnych"],
            "answer": "B"
        },
        {
            "question": "Jakie są główne aspekty funkcji przechowywania danych w systemie informatycznym?",
            "options": ["A) Ewidencja i przekształcanie danych",
                        "B) Sortowanie i przetwarzanie danych",
                        "C) Bezpieczeńwo danych i ich dostępność",
                        "D) Wyszukiwanie danych w celu uzyskania odpowiedzi"],
            "answer": "C"
        },
        {
            "question": "Czym charakteryzuje się funkcja wyszukiwania i wyprowadzania danych w systemie informatycznym?",
            "options": ["A) Przechowywanie i zabezpieczanie danych",
                        "B) Zbieranie danych o istotnych parametrach organizacyjnych",
                        "C) Określanie nośników danych i ich dostępności",
                        "D) Sposoby przeszukiwania danych w celu uzyskania odpowiedzi"],
            "answer": "D"
        }
    ]

    if 'shuffled_questions' not in st.session_state:
        st.session_state.shuffled_questions = [shuffle_options(q) for q in
                                               random.sample(original_questions, len(original_questions))]

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
        if st.session_state.question_index < len(st.session_state.shuffled_questions):
            question = st.session_state.shuffled_questions[st.session_state.question_index]
            st.write(f"\n**Pytanie {st.session_state.question_index + 1}:** {question['question']}")

            options = [f"{chr(65 + i)}) {option.split(')', 1)[1].strip()}" for i, option in
                       enumerate(question['options'])]
            user_answer = st.radio("Twoja odpowiedź:", options, key=str(st.session_state.question_index))

            if st.button("Następne pytanie"):
                st.session_state.user_answers.append(user_answer)
                if user_answer.startswith(question['answer']):
                    st.session_state.score += 1
                st.session_state.question_index += 1
                st.experimental_rerun()

        else:
            st.write(
                f"\n**Quiz zakończony! Twój wynik to:** {st.session_state.score}/{len(st.session_state.shuffled_questions)}")

            st.write("\n**Lista poprawnych odpowiedzi:**")
            for idx, (question, user_answer) in enumerate(
                    zip(st.session_state.shuffled_questions, st.session_state.user_answers)):
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
                st.session_state.shuffled_questions = [shuffle_options(q) for q in
                                                       random.sample(original_questions, len(original_questions))]
                st.experimental_rerun()


if __name__ == "__main__":
    quiz()
