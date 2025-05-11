import streamlit as st
import random

# Initialisation des questions dans la session pour persistance
if "questions" not in st.session_state:
    base_questions = [
        {"question": "Quelle est la définition de la RSE ?",
         "options": ["Responsabilité Sociale des Entreprises", "Réforme du Système d'Entreprise", "Réduction des Salaires Excessifs", "Régulation Sociale et Économique"],
         "answer": "Responsabilité Sociale des Entreprises"},
        {"question": "Que signifie le sigle SWOT ?",
         "options": ["Strengths, Weaknesses, Opportunities, Threats", "Systematic Weakness Optimization Technique", "Strategic Way of Thinking", "Strengths and Weakness Tracking"],
         "answer": "Strengths, Weaknesses, Opportunities, Threats"},
        {"question": "Qu’est-ce qu’un marché oligopolistique ?",
         "options": ["Un marché avec un seul vendeur", "Un marché dominé par quelques vendeurs", "Un marché parfaitement concurrentiel", "Un marché sans vendeurs"],
         "answer": "Un marché dominé par quelques vendeurs"},
        {"question": "Quelle est la principale fonction des RH ?",
         "options": ["Maximiser les ventes", "Gérer le personnel de l’entreprise", "Créer de nouveaux produits", "Analyser la concurrence"],
         "answer": "Gérer le personnel de l’entreprise"},
        {"question": "Que mesure le taux de rentabilité ?",
         "options": ["La satisfaction des clients", "La capacité à générer des profits", "Le nombre de ventes", "La productivité des salariés"],
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

# Page Config and Theme
st.set_page_config(
    page_title="Quiz Culture Générale",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for card layout and styling
st.markdown("""
<style>
    .card {
        background: #ffffff;
        padding: 2rem;
        margin: 2rem auto;
        border-radius: 1rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        max-width: 700px;
    }
    .question {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    .option-label {
        font-size: 1.2rem;
    }
    .btn-validate {
        background-color: #008cff;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 0.5rem;
        cursor: pointer;
        font-size: 1rem;
        margin-right: 1rem;
    }
    .btn-validate:hover {
        background-color: #006bb3;
    }
    .btn-next {
        background-color: #4CAF50;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 0.5rem;
        cursor: pointer;
        font-size: 1rem;
    }
    .btn-next:hover {
        background-color: #388e3c;
    }
    .sidebar .stProgress > div > div {
        background-color: #008cff;
    }
    .sidebar-text {
        font-size: 1rem;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar: progress and score
with st.sidebar:
    st.markdown("### Progression")
    if st.session_state.current_q < len(questions):
        display_q = st.session_state.current_q + 1
        progress_val = display_q / len(questions)
    else:
        display_q = len(questions)
        progress_val = 1.0
    st.markdown(f"<p class='sidebar-text'>Question <b>{display_q}</b> / {len(questions)}</p>", unsafe_allow_html=True)
    st.progress(progress_val)
    st.markdown(f"<p class='sidebar-text'>Score : <b>{st.session_state.score}</b></p>", unsafe_allow_html=True)

# Main quiz card
st.markdown("<div class='card'>", unsafe_allow_html=True)

if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.markdown(f"<div class='question'>{q['question']}</div>", unsafe_allow_html=True)
    selected = st.radio("", q['options'], key=f"opt_{st.session_state.current_q}")

    # Buttons
    col1, col2 = st.columns([1,1], gap='small')
    with col1:
        if st.button("Valider", key=f"val_{st.session_state.current_q}", help="Valider votre réponse"):
            st.session_state.validated = True
            st.session_state.last_selected = selected
            if selected == q['answer']:
                st.success("Correct ! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"Faux ! La bonne réponse était : **{q['answer']}**")
    with col2:
        if st.session_state.validated and st.button("Suivant", key=f"next_{st.session_state.current_q}"):
            st.session_state.current_q += 1
            st.session_state.validated = False
            st.experimental_rerun()

    # After validation
    if st.session_state.validated:
        st.markdown(f"**Votre réponse :** {st.session_state.last_selected}")
        st.markdown(f"**Bonne réponse :** {q['answer']}")

else:
    st.balloons()
    st.success(f"Quiz terminé ! Votre score : {st.session_state.score} / {len(questions)} 🎯")
    if st.button("Rejouer"):
        for key in ["questions", "current_q", "score", "validated", "last_selected"]:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)
