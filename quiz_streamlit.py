import streamlit as st
import random

# Fonction pour mélanger les questions
def generate_questions():
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
        },
    ]
    random.shuffle(questions)
    return questions

# Charger les questions
questions = generate_questions()

# Configuration de la page
st.set_page_config(page_title="Quiz Culture Générale", layout="centered")

# Initialisation de l'état
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
    st.session_state.score = 0

# Obtenir l'index actuel de la question
current_question_index = st.session_state.current_question_index

# Afficher le titre
st.title("Quiz Culture Générale - Gestion")

if current_question_index < len(questions):
    # Question actuelle
    question = questions[current_question_index]
    st.subheader(f"Question {current_question_index + 1}/{len(questions)}")
    st.write(question["question"])

    # Options de réponse
    selected_option = st.radio("Choisissez une réponse :", question["options"], key=current_question_index)

    # Bouton pour valider
    if st.button("Valider"):
        if selected_option == question["answer"]:
            st.session_state.score += 1
            st.success("Correct ! 🎉")
        else:
            st.error(f"Faux ! La bonne réponse était : {question['answer']}")

        # Mettre à jour l'index de la question
        st.session_state.current_question_index += 1
        st.experimental_rerun()  # Relancer l'application pour la prochaine question
else:
    # Fin du quiz
    st.subheader("Quiz Terminé !")
    st.write(f"Votre score final est : {st.session_state.score}/{len(questions)} 🎯")
    st.balloons()

    # Bouton pour rejouer
    if st.button("Rejouer"):
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.experimental_rerun()
