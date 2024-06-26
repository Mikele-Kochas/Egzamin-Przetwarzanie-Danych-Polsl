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
    additional_questions = [
        {
            "question": "Czym charakteryzuje się proces standaryzacji danych?",
            "options": [
                "A) Przekształceniem danych tak, aby miały średnią równą zero i odchylenie standardowe równe jeden.",
                "B) Przekształceniem danych tak, aby mieściły się w zakresie od 0 do 1.",
                "C) Ustawianiem progów, które określają akceptowalne wartości danych.",
                "D) Grupowaniem danych w klastry na podstawie ich podobieństwa."
            ],
            "answer": "A"
        },
        {
            "question": "Które z poniższych najlepiej opisuje normalizację danych?",
            "options": [
                "A) Przekształcanie danych w taki sposób, aby miały średnią równą zero.",
                "B) Przekształcanie danych w taki sposób, aby mieściły się w określonym zakresie, zazwyczaj od 0 do 1.",
                "C) Ustawianie progów, które określają akceptowalne wartości danych.",
                "D) Analiza danych w celu wykrycia ukrytych wzorców."
            ],
            "answer": "B"
        },
        {
            "question": "Jakie jest główne zastosowanie progowania w przetwarzaniu danych?",
            "options": [
                "A) Skalowanie danych do określonego zakresu.",
                "B) Przekształcanie danych w taki sposób, aby miały średnią równą zero i odchylenie standardowe równe jeden.",
                "C) Ustawianie granic, które określają, które wartości danych są akceptowalne, a które nie.",
                "D) Grupowanie danych w klastry na podstawie ich podobieństwa."
            ],
            "answer": "C"
        },
        {
            "question": "Które z poniższych stwierdzeń jest prawdziwe o normalizacji i standaryzacji?",
            "options": [
                "A) Normalizacja i standaryzacja to dwa różne terminy na ten sam proces.",
                "B) Normalizacja przekształca dane do średniej równej zero, a standaryzacja skaluje dane do zakresu od 0 do 1.",
                "C) Standaryzacja przekształca dane do średniej równej zero i odchylenia standardowego równego jeden, podczas gdy normalizacja skaluje dane do określonego zakresu.",
                "D) Normalizacja ustawia granice akceptowalności danych, a standaryzacja grupuje dane w klastry."
            ],
            "answer": "C"
        }
    ]

    additional_questions_2 = [
        {
            "question": "Połącz skrót PCA z polską nazwą techniki:",
            "options": [
                "A) Analiza składowych głównych",
                "B) Analiza czynnikowa",
                "C) Rozkład macierzy nieujemnej",
                "D) Analiza głównych kierunków"
            ],
            "answer": "A"
        },
        {
            "question": "Połącz skrót FA z polską nazwą techniki:",
            "options": [
                "A) Analiza składowych głównych",
                "B) Analiza czynnikowa",
                "C) Rozkład macierzy nieujemnej",
                "D) Analiza czynnikowa"
            ],
            "answer": "D"
        },
        {
            "question": "Połącz skrót NMF z polską nazwą techniki:",
            "options": [
                "A) Analiza składowych głównych",
                "B) Analiza czynnikowa",
                "C) Rozkład macierzy nieujemnej",
                "D) Niedodatni rozkład macierzy"
            ],
            "answer": "D"
        }
    ]
    additional_questions_3 = [
        {
            "question": "Co to jest dana?",
            "options": ["A) Interpretacja przetworzonych informacji",
                        "B) Sformalizowana wiadomość o określonej strukturze",
                        "C) Wiedza nadająca się do użycia",
                        "D) Sygnał dotyczący zjawiska lub procesu"],
            "answer": "B"
        },
        {
            "question": "Co to jest informacja?",
            "options": ["A) Sformalizowana wiadomość o określonej strukturze",
                        "B) Powstaje na skutek interpretacji przetworzonych danych",
                        "C) Sygnał dotyczący zjawiska lub procesu",
                        "D) Zbiór obiektów przetwarzających dane"],
            "answer": "B"
        },
        {
            "question": "Która definicja najlepiej opisuje wiedzę?",
            "options": ["A) Surowa, sformalizowana wiadomość",
                        "B) Informacje nadające się do użycia",
                        "C) Sygnał dotyczący zjawiska lub procesu",
                        "D) Zbiór danych o określonej strukturze"],
            "answer": "B"
        },
        {
            "question": "Co to jest dyspozycyjność w kontekście kryteriów oceny jakości informacji?",
            "options": ["A) Wiarygodność informacji w danym momencie",
                        "B) Dokładność i poprawność informacji",
                        "C) Możliwość dostępu do każdej informacji w systemie w dowolnym momencie",
                        "D) Zdolność do przeprowadzenia analizy porównawczej"],
            "answer": "C"
        },
        {
            "question": "Czym charakteryzuje się system informacyjny?",
            "options": ["A) Jest to wyłącznie zbiór urządzeń komputerowych",
                        "B) Obejmuje tylko procesy przetwarzania danych",
                        "C) To zbiór obiektów przetwarzających informacje, ludzi, danych i procesów",
                        "D) Dotyczy tylko infrastruktury sieciowej"],
            "answer": "C"
        },
        {
            "question": "Co to jest system informatyczny?",
            "options": ["A) Zbiór obiektów przetwarzających informacje",
                        "B) Część systemu informacyjnego realizująca przetwarzanie informacji za pomocą systemów komputerowych",
                        "C) Zbiór ludzi, danych i procesów",
                        "D) Infrastruktura sieciowa i urządzenia komputerowe"],
            "answer": "B"
        },
        {
            "question": "Która z poniższych NIE jest funkcją systemu informatycznego?",
            "options": ["A) Ewidencja danych",
                        "B) Przekształcanie danych",
                        "C) Interpretacja emocjonalna danych",
                        "D) Wyszukiwanie i wyprowadzanie danych"],
            "answer": "C"
        },
        {
            "question": "Które z poniższych jest przykładem zmiennej jakościowej?",
            "options": ["A) Liczba studentów na wykładzie",
                        "B) Długość w metrach",
                        "C) Nazwa uczelni (np. AWF, AGH)",
                        "D) Temperatura powietrza w stopniach Celsjusza"],
            "answer": "C"
        },
        {
            "question": "Co to jest zmienna ilorazowa?",
            "options": ["A) Zmienna przyjmująca tylko dwie wartości",
                        "B) Zmienna mierzona w skali, np. długość w metrach",
                        "C) Zmienna określająca kolejność",
                        "D) Zmienna o nieuporządkowanych wartościach"],
            "answer": "B"
        },
        {
            "question": "Która z poniższych jest przykładem zmiennej binarnej?",
            "options": ["A) Wiek osoby",
                        "B) Ocena z egzaminu (2-5)",
                        "C) Prawda/fałsz",
                        "D) Nazwa miesiąca"],
            "answer": "C"
        },
        {
            "question": "Co to jest progowanie?",
            "options": ["A) Ograniczenie liczby wartości zmiennej do 2",
                        "B) Przekształcenie danych do tej samej skali",
                        "C) Zastąpienie zbioru wartości etykietą określającą przedział wartości",
                        "D) Przekształcanie danych do rozkładu o średniej 0 i odchyleniu standardowym 1"],
            "answer": "C"
        },
        {
            "question": "Co to jest binaryzacja?",
            "options": ["A) Przekształcenie danych do tej samej skali",
                        "B) Ograniczenie liczby wartości zmiennej do 2",
                        "C) Zastąpienie zbioru wartości etykietą określającą przedział wartości",
                        "D) Przekształcanie danych do rozkładu o średniej 0"],
            "answer": "B"
        },
        {
            "question": "Która metoda przekształca dane do rozkładu o średniej 0 i odchyleniu standardowym 1?",
            "options": ["A) Normalizacja",
                        "B) Binaryzacja",
                        "C) Progowanie",
                        "D) Standaryzacja"],
            "answer": "D"
        },
        {
            "question": "Co charakteryzuje rozkład skośny?",
            "options": ["A) Symetryczna dystrybucja",
                        "B) Niesymetryczna dystrybucja przypominająca rozkład normalny",
                        "C) Zawsze ma ogon skierowany w lewo",
                        "D) Ma zawsze średnią równą 0"],
            "answer": "B"
        },
        {
            "question": "Co oznacza pojęcie wielowymiarowości w analizie danych?",
            "options": ["A) Analiza danych wyłącznie w trzech wymiarach",
                        "B) Sytuacja, gdy analizujemy dane charakteryzujące się wieloma zmiennymi",
                        "C) Badanie tylko nieskorelowanych zmiennych",
                        "D) Analiza wyłącznie zmiennych ilościowych"],
            "answer": "B"
        },
        {
            "question": "Która metoda redukcji wymiarów zastępuje zbiór zmiennych mniejszym zbiorem ich kombinacji liniowych?",
            "options": ["A) Analiza składowych głównych (PCA)",
                        "B) Analiza czynnikowa (FA)",
                        "C) Rozkład macierzy nieujemnej (NMF)",
                        "D) Jednoklasowa maszyna wektorów nośnych (One-class SVM)"],
            "answer": "A"
        },
        {
            "question": "Co to jest analiza czynnikowa (FA)?",
            "options": ["A) Metoda redukcji wymiarów oparta na liniowej kombinacji zmiennych",
                        "B) Technika wykrywania anomalii",
                        "C) Sposób normalizacji danych",
                        "D) Metoda imputacji brakujących wartości"],
            "answer": "A"
        },
        {
            "question": "Co to jest korelacja?",
            "options": ["A) Miara centralnej tendencji danych",
                        "B) Sposób normalizacji danych",
                        "C) Unormowana kowariancja",
                        "D) Metoda redukcji wymiarów"],
            "answer": "C"
        },
        {
            "question": "Czym charakteryzuje się detektor anomalii oparty na gęstości rozkładu?",
            "options": ["A) Zakłada, że normalne obserwacje umieszczone są gęsto, a anomalie leżą w oddaleniu",
                        "B) Bazuje wyłącznie na grupowaniu danych",
                        "C) Wykorzystuje funkcje jądrowe do separacji danych",
                        "D) Jest oparty na sieciach neuronowych"],
            "answer": "A"
        },
        {
            "question": "Która metoda wykrywania anomalii wykorzystuje kolekcję drzew izolacyjnych?",
            "options": ["A) K-Nearest Neighborhood",
                        "B) Local Outlier Factor",
                        "C) One-class SVM",
                        "D) Isolation Forest (Las izolacyjny)"],
            "answer": "D"
        },
        {
            "question": "Która metoda redukcji szumów w obrazie wykorzystuje wzory z okolicznych pikseli?",
            "options": ["A) Median filter (Filtr medianowy)",
                        "B) Non-Local Means Denoising (NLMeans)",
                        "C) Gaussian filter (Filtr Gaussa)",
                        "D) Bilateral filter (Filtr bilateralny)"],
            "answer": "B"
        },
        {
            "question": "Który filtr wygładza obraz, zachowując krawędzie?",
            "options": ["A) Median filter (Filtr medianowy)",
                        "B) Non-Local Means Denoising (NLMeans)",
                        "C) Gaussian filter (Filtr Gaussa)",
                        "D) Bilateral filter (Filtr bilateralny)"],
            "answer": "D"
        },
        {
            "question": "Co to jest wariancja?",
            "options": ["A) Miara centralnej tendencji danych",
                        "B) Miara rozrzutu danych",
                        "C) Miara symetrii rozkładu",
                        "D) Miara korelacji między zmiennymi"],
            "answer": "B"
        },
        {
            "question": "Co mierzy test ANOVA?",
            "options": ["A) Symetrię rozkładu",
                        "B) Różnice średnich między grupami",
                        "C) Stopień korelacji",
                        "D) Rozkład danych"],
            "answer": "B"
        },
        {
            "question": "Który test służy do porównań post hoc po wykonaniu ANOVA?",
            "options": ["A) Test HSD Tukeya",
                        "B) Test t-Studenta",
                        "C) Test Chi-kwadrat",
                        "D) Test Wilcoxona"],
            "answer": "A"
        },
        {
            "question": "Która metoda wykrywania anomalii wykorzystuje sieci neuronowe do modelowania danych?",
            "options": ["A) K-Nearest Neighborhood",
                        "B) Local Outlier Factor",
                        "C) Autodekodery (Autoencoders)",
                        "D) Isolation Forest (Las izolacyjny)"],
            "answer": "C"
        },
        {
            "question": "Która metoda regularyzacji dodaje karę za sumę wartości bezwzględnych współczynników?",
            "options": ["A) Regresja LASSO",
                        "B) Regresja Ridge",
                        "C) Elastic Net",
                        "D) Principal Component Regression"],
            "answer": "A"
        },
        {
            "question": "Która metoda wykrywania anomalii opiera się na podobieństwie lokalnym?",
            "options": ["A) Isolation Forest",
                        "B) One-class SVM",
                        "C) Local Outlier Factor",
                        "D) Autodekodery"],
            "answer": "C"
        },
        {
            "question": "Która metoda imputacji brakujących danych polega na zastąpieniu brakujących wartości średnią lub medianą?",
            "options": ["A) Imputacja wielokrotna",
                        "B) Uzupełnianie braków przez predykcję",
                        "C) Imputacja prostą średnią lub medianą",
                        "D) Usuwanie braków"],
            "answer": "C"
        },
        {
            "question": "Która metoda imputacji brakujących danych zastępuje brakujące wartości najbardziej prawdopodobną wartością na podstawie innych danych?",
            "options": ["A) Imputacja prostą średnią lub medianą",
                        "B) Uzupełnianie braków przez predykcję",
                        "C) Usuwanie braków",
                        "D) Imputacja wielokrotna"],
            "answer": "B"
        },
        {
            "question": "Która technika próbkuje dane w taki sposób, aby zapewnić reprezentatywność próby?",
            "options": ["A) Próbkowanie losowe",
                        "B) Próbkowanie warstwowe",
                        "C) Próbkowanie systematyczne",
                        "D) Próbkowanie nielosowe"],
            "answer": "B"
        },
        {
            "question": "Która technika próbkuje dane w równych odstępach?",
            "options": ["A) Próbkowanie losowe",
                        "B) Próbkowanie warstwowe",
                        "C) Próbkowanie systematyczne",
                        "D) Próbkowanie nielosowe"],
            "answer": "C"
        },
        {
            "question": "Czym charakteryzuje się kroswalidacja?",
            "options": ["A) Wykorzystuje cały zbiór danych do trenowania i testowania",
                        "B) Podział danych na podzbiory, na których naprzemiennie trenuje się i testuje model",
                        "C) Wykorzystanie tylko części danych do trenowania",
                        "D) Wykonywanie analizy na wszystkich dostępnych danych bez podziału"],
            "answer": "B"
        },
        {
            "question": "Która metoda testowania modeli polega na iteracyjnym usuwaniu jednego elementu z próby i trenowaniu modelu na pozostałych?",
            "options": ["A) Kroswalidacja",
                        "B) Bootstrap",
                        "C) Próbkowanie warstwowe",
                        "D) Metoda jackknife"],
            "answer": "D"
        },
        {
            "question": "Która technika wykrywania anomalii wykorzystuje minimalną przestrzeń zamknięcia?",
            "options": ["A) K-Nearest Neighborhood",
                        "B) Local Outlier Factor",
                        "C) One-class SVM",
                        "D) Isolation Forest (Las izolacyjny)"],
            "answer": "C"
        },
        {
            "question": "Która technika jest używana do redukcji szumów w obrazach i jest bardziej zaawansowana od filtra medianowego?",
            "options": ["A) Non-Local Means Denoising (NLMeans)",
                        "B) Gaussian filter (Filtr Gaussa)",
                        "C) Bilateral filter (Filtr bilateralny)",
                        "D) Median filter (Filtr medianowy)"],
            "answer": "A"
        }
    ]

    original_questions.extend(additional_questions)

    original_questions.extend(additional_questions_2)

    original_questions.extend(additional_questions_3)

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
