import streamlit as st
import random

# Fonction pour générer et mélanger les questions et options
@st.cache_data
def load_questions():
    questions = [
        {
            "question": "Quelle est la définition de la RSE ?",
            "options": [
                "Responsabilité Sociale des Entreprises",
                "Réforme du Système d'Entreprise",
                "Réduction des Salaires Excessifs",
                "Régulation Sociale et Économique"
            ],
            "answer": "Responsabilité Sociale des Entreprises"
        },
        {
            "question": "Que signifie le sigle SWOT ?",
            "options": [
                "Strengths, Weaknesses, Opportunities, Threats",
                "Systematic Weakness Optimization Technique",
                "Strategic Way of Thinking",
                "Strengths and Weakness Tracking"
            ],
            "answer": "Strengths, Weaknesses, Opportunities, Threats"
        },
        {
            "question": "Qu’est-ce qu’un marché oligopolistique ?",
            "options": [
                "Un marché avec un seul vendeur",
                "Un marché dominé par quelques vendeurs",
                "Un marché parfaitement concurrentiel",
                "Un marché sans vendeurs"
            ],
            "answer": "Un marché dominé par quelques vendeurs"
        },
        {
            "question": "Quelle est la principale fonction des RH ?",
            "options": [
                "Maximiser les ventes",
                "Gérer le personnel de l’entreprise",
                "Créer de nouveaux produits",
                "Analyser la concurrence"
            ],
            "answer": "Gérer le personnel de l’entreprise"
        },
        {
            "question": "Que mesure le taux de rentabilité ?",
            "options": [
                "La satisfaction des clients",
                "La capacité à générer des profits",
                "Le nombre de ventes",
                "La productivité des salariés"
            ],
            "answer": "La capacité à générer des profits"
        }
    ]

    # Mélanger l'ordre des questions et des options
    random.shuffle(questions)
    for q in questions:
        random.shuffle(q["options"])
    return questions

# Chargement des questions
questions = load_questions()

# Configuration de la page
st.set_page_config(
    page_title="Quiz Culture Générale",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialisation de l'état de la session
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.validated = False
    st.session_state.selected = None

# Affichage dans la sidebar
st.sidebar.title("Progression du Quiz")
st.sidebar.write(f"Question {st.session_state.current_q + 1} / {len(questions)}")
progress = (st.session_state.current_q + 1) / len(questions)
st.sidebar.progress(progress)
st.sidebar.write(f"Score actuel: **{st.session_state.score}**")

# Titre principal
st.title("🧠 Quiz Culture Générale - Gestion")

# Affichage de la question ou résultat final
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(q["question"])

    # Affichage des options avant validation
    if not st.session_state.validated:
        st.session_state.selected = st.radio(
            "Choisissez une réponse :", q["options"], key=f"opt_{st.session_state.current_q}"
        )

        if st.button("Valider", key=f"val_{st.session_state.current_q}"):
            st.session_state.validated = True
            if st.session_state.selected == q["answer"]:
                st.session_state.score += 1
                st.success("Correct ! 🎉")
            else:
                st.error(f"Faux ! La bonne réponse était : **{q['answer']}**")

    # Après validation, proposition de passer à la suite
    else:
        st.markdown(f"**Votre réponse :** {st.session_state.selected}")
        st.markdown(f"**Bonne réponse :** {q['answer']}")
        if st.button("Suivant", key=f"next_{st.session_state.current_q}"):
            # Passer à la question suivante
            st.session_state.current_q += 1
            st.session_state.validated = False
            st.session_state.selected = None

else:
    # Fin du quiz
    st.balloons()
    st.success(f"Quiz terminé ! Votre score : {st.session_state.score} / {len(questions)} 🎯")
    if st.button("Rejouer"):
        # Réinitialiser l'état
        questions = load_questions()
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.validated = False
        st.session_state.selected = None

# Style custom (CSS) pour meilleure interaction
st.markdown(
    """
<style>
body {
    background-color: #f0f2f6;
}
.stApp {
    max-width: 800px;
    margin: auto;
}
button[kind="primary"] {
    background: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)
