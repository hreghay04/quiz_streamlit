import streamlit as st
import random
import json

# === Données des quiz par thème ===
with open("quiz_referentiel.json", 'r') as f:
    quiz_referentiel = json.load(f)

# Configuration
st.set_page_config(page_title="Quiz Thématique", layout="centered", initial_sidebar_state="expanded")
st.title("🎓 Quiz Thématique")

# Sélection du thème
theme = st.sidebar.selectbox("Choisissez votre thème", list(quiz_referentiel.keys()))

# Initialisation du quiz dès que le thème change
if ("theme_selected" not in st.session_state) or (st.session_state.theme_selected != theme):
    st.session_state.theme_selected = theme
    questions = quiz_referentiel[theme].copy()
    random.shuffle(questions)
    for q in questions:
        random.shuffle(q["options"])
    st.session_state.questions = questions
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.validated = False
    st.session_state.last_result = None  # "correcte" ou "incorrecte"

# Raccourcis
questions = st.session_state.questions
idx = st.session_state.current_q
total = len(questions)

# Barre de progression
progress = (idx + 1) / total if idx < total else 1.0
st.sidebar.progress(progress)
st.sidebar.write(f"Question {min(idx+1, total)}/{total}")
st.sidebar.write(f"Score : {st.session_state.score} / {total}")

# Callback pour valider
def validate_answer():
    sel = st.session_state["selected_option"]
    bonne = questions[idx]["answer"]
    if sel == bonne:
        st.session_state.score += 1
        st.session_state.last_result = "correcte"
    else:
        st.session_state.last_result = "incorrecte"
    st.session_state.validated = True

# Callback pour passer à la suivante
def next_question():
    st.session_state.current_q += 1
    st.session_state.validated = False
    st.session_state.last_result = None

# Callback pour rejouer
def replay():
    # Réinitialise tout depuis le thème courant
    st.session_state.theme_selected = None

# Affichage du quiz
if idx < total:
    q = questions[idx]
    st.subheader(q["question"])
    # Radio, valeur par défaut contrôlée
    st.radio("Votre réponse :", q["options"],
             key="selected_option",
             on_change=lambda: None)  # force la clé

    # Bouton Valider
    if not st.session_state.validated:
        st.button("Valider", on_click=validate_answer)
    else:
        # Message résultat
        if st.session_state.last_result == "correcte":
            st.success("✓ Correcte ! 🎉")
        else:
            st.error(f"✗ Incorrecte ! La bonne réponse est : **{q['answer']}**")

        # Bouton Suivant
        st.button("Suivant", on_click=next_question)

else:
    # Quiz terminé
    st.subheader("🎯 Quiz Terminé !")
    st.write(f"Votre score final : **{st.session_state.score} / {total}**")
    st.balloons()
    st.button("Rejouer", on_click=replay)
