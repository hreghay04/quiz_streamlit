import streamlit as st
import random

# Initialisation des questions dans la session pour persistance
if "questions" not in st.session_state:
    base_questions = [
        {"question": "Quelle est la définition de la RSE ?",
         "options": ["Responsabilité Sociale des Entreprises", "Réforme du Système d'Entreprise",
                     "Réduction des Salaires Excessifs", "Régulation Sociale et Économique"],
         "answer": "Responsabilité Sociale des Entreprises"},
        {"question": "Que signifie le sigle SWOT ?",
         "options": ["Strengths, Weaknesses, Opportunities, Threats",
                     "Systematic Weakness Optimization Technique", "Strategic Way of Thinking",
                     "Strengths and Weakness Tracking"],
         "answer": "Strengths, Weaknesses, Opportunities, Threats"},
        {"question": "Qu’est-ce qu’un marché oligopolistique ?",
         "options": ["Un marché avec un seul vendeur", "Un marché dominé par quelques vendeurs",
                     "Un marché parfaitement concurrentiel", "Un marché sans vendeurs"],
         "answer": "Un marché dominé par quelques vendeurs"},
        {"question": "Quelle est la principale fonction des RH ?",
         "options": ["Maximiser les ventes", "Gérer le personnel de l’entreprise",
                     "Créer de nouveaux produits", "Analyser la concurrence"],
         "answer": "Gérer le personnel de l’entreprise"},
        {"question": "Que mesure le taux de rentabilité ?",
         "options": ["La satisfaction des clients", "La capacité à générer des profits",
                     "Le nombre de ventes", "La productivité des salariés"],
         "answer": "La capacité à générer des profits"}
    ]
    random.shuffle(base_questions)
    for q in base_questions:
        random.shuffle(q["options"])
    st.session_state.questions = base_questions
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.validated = False

questions = st.session_state.questions

st.set_page_config(
    page_title="Quiz Culture Générale",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar: progression et score
if st.session_state.current_q < len(questions):
    display_q = st.session_state.current_q + 1
    progress_val = display_q / len(questions)
else:
    display_q = len(questions)
    progress_val = 1.0
st.sidebar.title("Progression")
st.sidebar.text(f"Question {display_q} / {len(questions)}")
st.sidebar.progress(progress_val)
st.sidebar.text(f"Score: {st.session_state.score}")

# Titre principal
st.title("🧠 Quiz Culture Générale - Gestion")

# Contenu du quiz
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(q["question"])

    selected = st.radio("Choisissez une réponse :", q["options"], key=f"opt_{st.session_state.current_q}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Valider", key=f"val_{st.session_state.current_q}"):
            st.session_state.validated = True
            st.session_state.last_selected = selected
            if selected == q["answer"]:
                st.session_state.score += 1
                st.success("Correct ! 🎉")
            else:
                st.error(f"Faux ! La bonne réponse était : **{q['answer']}**")
    with col2:
        if st.session_state.validated and st.button("Suivant", key=f"next_{st.session_state.current_q}"):
            st.session_state.current_q += 1
            st.session_state.validated = False

    if st.session_state.validated:
        st.markdown(f"- **Votre réponse :** {st.session_state.last_selected}")
        st.markdown(f"- **Bonne réponse :** {q['answer']}")
else:
    st.balloons()
    st.success(f"Quiz terminé ! Votre score : {st.session_state.score} / {len(questions)} 🎯")
    if st.button("Rejouer"):
        for key in ["questions", "current_q", "score", "validated", "last_selected"]:
            if key in st.session_state:
                del st.session_state[key]

# Style CSS pour l'interface
st.markdown(
    """
    <style>
    .stApp { max-width: 700px; margin: auto; }
    header { background-color: #4CAF50 !important; }
    </style>
    """, unsafe_allow_html=True)
