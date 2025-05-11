import streamlit as st
import random

# === Données des quiz par thème ===
quiz_referentiel = {
    "Internet": [
        {
            "question": "Qu'est-ce que l'ARPANET et en quelle année a-t-il vu le jour ?",
            "options": [
                "Un réseau de recherche universitaire en 1965",
                "Un réseau militaire américain de 1969",
                "Le protocole de routage TCP/IP en 1983",
                "Un service de noms de domaine en 1985"
            ],
            "answer": "Un réseau militaire américain de 1969"
        },
        {
            "question": "En quelle année Internet est-il devenu opérationnel avec l'adoption du protocole TCP/IP ?",
            "options": [
                "1973",
                "1983",
                "1993",
                "2003"
            ],
            "answer": "1983"
        },
        {
            "question": "Quel est l'avantage principal d'IPv6 par rapport à IPv4 ?",
            "options": [
                "Une meilleure qualité de service (QoS)",
                "Un espace d'adressage beaucoup plus grand",
                "Un chiffrement obligatoire",
                "Une compatibilité complète avec IPv4"
            ],
            "answer": "Un espace d'adressage beaucoup plus grand"
        },
        {
            "question": "Qu'est-ce que la commutation de paquets ?",
            "options": [
                "La segmentation et le routage de données en petits paquets",
                "Le cryptage de paquets de données",
                "Le protocole d'établissement de session TCP",
                "Une méthode de transfert de fichiers par FTP"
            ],
            "answer": "La segmentation et le routage de données en petits paquets"
        },
        {
            "question": "Parmi ces topologies réseau, laquelle présente un point central unique ?",
            "options": [
                "Maillée",
                "En anneau",
                "En étoile",
                "En arbre"
            ],
            "answer": "En étoile"
        },
        {
            "question": "Quel service traduit un nom de domaine en adresse IP ?",
            "options": [
                "DHCP",
                "DNS",
                "FTP",
                "SMTP"
            ],
            "answer": "DNS"
        }
    ],
    "Le Web": [
        {
            "question": "Qui a inventé le World Wide Web et en quelle année a-t-il publié son premier site ?",
            "options": [
                "Tim Berners-Lee en 1989",
                "Ted Nelson en 1965",
                "Vint Cerf en 1974",
                "Marc Andreessen en 1993"
            ],
            "answer": "Tim Berners-Lee en 1989"
        },
        {
            "question": "Quelle architecture est à la base du fonctionnement du Web ?",
            "options": [
                "Pair à pair",
                "Client-serveur",
                "Monolithique",
                "Hybride"
            ],
            "answer": "Client-serveur"
        },
        {
            "question": "Qu'est-ce qu'une API REST ?",
            "options": [
                "Une interface web basée sur HTTP pour manipuler des ressources",
                "Un protocole de messagerie instantanée",
                "Un serveur de fichiers",
                "Un langage de balisage"
            ],
            "answer": "Une interface web basée sur HTTP pour manipuler des ressources"
        },
        {
            "question": "Quel format d'échange est plus léger et couramment utilisé par les API web ?",
            "options": [
                "JSON",
                "XML",
                "CSV",
                "YAML"
            ],
            "answer": "JSON"
        },
        {
            "question": "Quel sélecteur CSS cible toutes les balises <p> ?",
            "options": [
                "p",
                "#p",
                ".p",
                "*"
            ],
            "answer": "p"
        },
        {
            "question": "Quelle propriété CSS définit l'espace entre le contenu et la bordure d'un élément ?",
            "options": [
                "margin",
                "padding",
                "border",
                "width"
            ],
            "answer": "padding"
        }
    ],
    "Les réseaux sociaux": [
        {
            "question": "En quelle année Facebook a-t-il ouvert son inscription à tous les utilisateurs majeurs ?",
            "options": [
                "2004",
                "2005",
                "2006",
                "2007"
            ],
            "answer": "2006"
        },
        {
            "question": "Quelle était la limite initiale de caractères sur Twitter ?",
            "options": [
                "100",
                "140",
                "160",
                "280"
            ],
            "answer": "140"
        },
        {
            "question": "Qu'est-ce qu'une bulle de filtre ?",
            "options": [
                "Un algorithme qui montre du contenu aligné avec les préférences de l'utilisateur",
                "Une fonctionnalité de protection des données",
                "Un type de message sponsorisé",
                "Une limite de durée pour les vidéos"
            ],
            "answer": "Un algorithme qui montre du contenu aligné avec les préférences de l'utilisateur"
        },
        {
            "question": "Quel règlement européen protège les données personnelles des utilisateurs ?",
            "options": [
                "DMCA",
                "COPPA",
                "RGPD",
                "HIPAA"
            ],
            "answer": "RGPD"
        },
        {
            "question": "Quelle est la principale source de revenus des réseaux sociaux gratuits ?",
            "options": [
                "Abonnements payants",
                "Publicité ciblée",
                "Vente de matériel",
                "Dons"
            ],
            "answer": "Publicité ciblée"
        }
    ],
    "Données structurées et traitement": [
        {
            "question": "Qui a proposé le modèle relationnel pour les bases de données et en quelle année ?",
            "options": [
                "Edgar F. Codd en 1970",
                "Donald Chamberlin en 1974",
                "Michael Stonebraker en 1985",
                "Jim Gray en 1992"
            ],
            "answer": "Edgar F. Codd en 1970"
        },
        {
            "question": "Quelle requête SQL sélectionne toutes les colonnes de la table utilisateurs ?",
            "options": [
                "SELECT utilisateurs FROM *",
                "SELECT * FROM utilisateurs",
                "GET * FROM utilisateurs",
                "FETCH ALL FROM utilisateurs"
            ],
            "answer": "SELECT * FROM utilisateurs"
        },
        {
            "question": "À quoi sert une jointure (JOIN) en SQL ?",
            "options": [
                "À combiner des lignes de plusieurs tables selon une condition",
                "À chiffrer la base de données",
                "À créer une nouvelle table vide",
                "À dupliquer une table"
            ],
            "answer": "À combiner des lignes de plusieurs tables selon une condition"
        },
        {
            "question": "Quel format texte est destiné au stockage de tableaux de données simples ?",
            "options": [
                "JSON",
                "XML",
                "CSV",
                "YAML"
            ],
            "answer": "CSV"
        },
        {
            "question": "Quel type de base NoSQL stocke les données sous forme de documents JSON ?",
            "options": [
                "Clé-valeur",
                "Colonnes",
                "Document",
                "Graphe"
            ],
            "answer": "Document"
        },
        {
            "question": "Quel est l'intérêt principal d'un index dans une base de données ?",
            "options": [
                "Accélérer les opérations de recherche",
                "Augmenter la taille des données",
                "Crypter les données",
                "Modifier la structure de la table"
            ],
            "answer": "Accélérer les opérations de recherche"
        }
    ],
    "Localisation, cartographie et mobilité": [
        {
            "question": "Quel système a été déployé par le DoD américain en 1978 pour la géolocalisation ?",
            "options": [
                "GLONASS",
                "Galileo",
                "GPS",
                "Beidou"
            ],
            "answer": "GPS"
        },
        {
            "question": "Quel principe technique permet à un récepteur GPS de déterminer sa position ?",
            "options": [
                "Trilatération par satellite",
                "Triangulation radio-terrestre",
                "Mesure Doppler",
                "Balayage radar"
            ],
            "answer": "Trilatération par satellite"
        },
        {
            "question": "Quel projet collaboratif permet à des volontaires de cartographier le monde ?",
            "options": [
                "MapQuest",
                "OpenStreetMap",
                "Google Maps",
                "Waze"
            ],
            "answer": "OpenStreetMap"
        },
        {
            "question": "Qu'est-ce que GeoJSON ?",
            "options": [
                "Un protocole de communication IoT",
                "Un format de données géospatiales basé sur JSON",
                "Une API de cartographie",
                "Un système de positionnement indoor"
            ],
            "answer": "Un format de données géospatiales basé sur JSON"
        },
        {
            "question": "Qu'est-ce que le géofencing ?",
            "options": [
                "La création de zones géographiques virtuelles pour déclencher des actions",
                "Le placement de capteurs GPS dans des véhicules",
                "La modélisation 3D de terrains",
                "Une technique de triangulation améliorée"
            ],
            "answer": "La création de zones géographiques virtuelles pour déclencher des actions"
        }
    ],
    "Informatique embarquée et objets connectés": [
        {
            "question": "Quelle mission Apollo a utilisé l’un des premiers calculateurs embarqués pour le module lunaire ?",
            "options": [
                "Apollo 7",
                "Apollo 8",
                "Apollo 11",
                "Apollo 13"
            ],
            "answer": "Apollo 11"
        },
        {
            "question": "Qui a popularisé l'expression « Internet des objets » et en quelle année ?",
            "options": [
                "Marc Weiser en 1991",
                "Kevin Ashton en 1999",
                "Vint Cerf en 2005",
                "Tim Berners-Lee en 1989"
            ],
            "answer": "Kevin Ashton en 1999"
        },
        {
            "question": "À quoi sert MQTT dans l'IoT ?",
            "options": [
                "Un protocole de messagerie léger basé sur le modèle pub/sub",
                "Un système de fichiers distribué",
                "Un langage de programmation pour objets",
                "Un format d'image"
            ],
            "answer": "Un protocole de messagerie léger basé sur le modèle pub/sub"
        },
        {
            "question": "Quel protocole conçu pour l’IoT est une alternative légère à HTTP ?",
            "options": [
                "AMQP",
                "FTP",
                "CoAP",
                "SMTP"
            ],
            "answer": "CoAP"
        },
        {
            "question": "Que désigne « edge computing » ?",
            "options": [
                "Le traitement des données à la périphérie du réseau plutôt que dans le cloud",
                "Le chiffrement de périphériques IoT",
                "La virtualisation de serveurs",
                "La connexion de réseaux maillés"
            ],
            "answer": "Le traitement des données à la périphérie du réseau plutôt que dans le cloud"
        },
        {
            "question": "Citez une mesure de sécurité recommandée pour un objet connecté.",
            "options": [
                "Utiliser un chiffrement des communications",
                "Stocker les mots de passe en clair",
                "Désactiver toute authentification",
                "Changer régulièrement de système d'exploitation"
            ],
            "answer": "Utiliser un chiffrement des communications"
        }
    ],
    "Photographie numérique": [
        {
            "question": "Quel type de capteur, inventé en 1969, a révolutionné la photographie numérique ?",
            "options": [
                "CMOS",
                "CCD",
                "BSI",
                "Foveon"
            ],
            "answer": "CCD"
        },
        {
            "question": "Quels sont les trois paramètres du triangle d'exposition en photographie ?",
            "options": [
                "Ouverture, vitesse d'obturation, sensibilité ISO",
                "Contraste, saturation, luminosité",
                "Balance des blancs, résolution, format",
                "Ouverture, balance des blancs, taille du capteur"
            ],
            "answer": "Ouverture, vitesse d'obturation, sensibilité ISO"
        },
        {
            "question": "Qu'est-ce que le format RAW ?",
            "options": [
                "Un format d'image compressé avec perte",
                "Un format contenant les données brutes issues du capteur",
                "Un format destiné aux vidéos",
                "Un protocole de transfert de fichiers"
            ],
            "answer": "Un format contenant les données brutes issues du capteur"
        },
        {
            "question": "Quelle est la principale différence entre RAW et JPEG ?",
            "options": [
                "RAW est sans perte et non traité, JPEG est compressé avec perte et traité",
                "RAW est un format vidéo, JPEG est un format audio",
                "RAW est plus léger que JPEG",
                "RAW est un format de texte"
            ],
            "answer": "RAW est sans perte et non traité, JPEG est compressé avec perte et traité"
        },
        {
            "question": "Quelle est la différence entre un photosite et un pixel ?",
            "options": [
                "Le photosite capte la lumière, le pixel est la représentation finale pour l'affichage",
                "Le photosite est logiciel, le pixel est matériel",
                "Le pixel capte la lumière, le photosite est le point d'affichage",
                "Il n'y a aucune différence"
            ],
            "answer": "Le photosite capte la lumière, le pixel est la représentation finale pour l'affichage"
        },
        {
            "question": "Quel format d'image propose une compression sans perte ?",
            "options": [
                "JPEG",
                "GIF",
                "TIFF",
                "BMP"
            ],
            "answer": "TIFF"
        }
    ]
}

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
