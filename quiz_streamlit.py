import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Nécessite Pillow pour redimensionner le GIF
import random

class StylishQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Culture Générale - Gestion")

        # Dimensions de la fenêtre
        window_width = 600
        window_height = 500

        # Obtenir les dimensions de l'écran
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculer la position pour centrer la fenêtre
        position_top = int((screen_height / 2) - (window_height / 2))
        position_right = int((screen_width / 2) - (window_width / 2))

        # Appliquer les dimensions et position centrée
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.configure(bg="#f4f4f9")

        # Initialisation des variables
        self.score = 0
        self.current_question_index = 0
        self.questions = self.generate_questions()

        # Interface utilisateur
        self.create_widgets()
        self.display_question()

    def generate_questions(self):
        """Retourne une liste de questions mélangées."""
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

    def create_widgets(self):
        """Crée les widgets de l'interface."""

        # Logo GIF redimensionné
        try:
            original_logo = Image.open("Logo_SNT_Pursuit.gif")  # Charger le fichier GIF
            resized_logo = original_logo.resize((300, 150))  # Redimensionner à 50x50 pixels
            self.logo = ImageTk.PhotoImage(resized_logo)  # Convertir pour Tkinter
            self.logo_label = tk.Label(self.root, image=self.logo, bg="#f4f4f9")
            self.logo_label.pack(pady=10)
        except Exception as e:
            print(f"Erreur de chargement du logo : {e}")
            self.logo_label = tk.Label(self.root, text="🎯", font=("Arial", 40), bg="#f4f4f9")
            self.logo_label.pack(pady=10)

        # Titre du Quiz
        self.title_label = tk.Label(
            self.root, text="Quiz Culture Générale - Gestion", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333"
        )
        self.title_label.pack(pady=10)

        # Zone de question
        self.question_label = tk.Label(
            self.root, text="", font=("Arial", 14), wraplength=500, justify="center", bg="#f4f4f9", fg="#555"
        )
        self.question_label.pack(pady=20)

        # Zone des options
        self.options_var = tk.StringVar(value="")
        self.options_frame = tk.Frame(self.root, bg="#f4f4f9")
        self.options_frame.pack(pady=10)

        # Bouton de validation
        self.submit_button = tk.Button(
            self.root,
            text="Valider",
            font=("Arial", 14),
            bg="#007BFF",
            fg="white",
            activebackground="#0056b3",
            activeforeground="white",
            command=self.check_answer,
            relief="raised",
            borderwidth=2,
            padx=10,
            pady=5
        )
        self.submit_button.pack(pady=20)

        # Affichage du score
        self.score_label = tk.Label(
            self.root, text="Score : 0", font=("Arial", 12), bg="#f4f4f9", fg="#777"
        )
        self.score_label.pack(side="bottom", pady=10)

    def display_question(self):
        """Affiche la question actuelle et ses options."""
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])

            # Efface les anciennes options
            for widget in self.options_frame.winfo_children():
                widget.destroy()

            # Affiche les nouvelles options
            for option in question_data["options"]:
                tk.Radiobutton(
                    self.options_frame,
                    text=option,
                    variable=self.options_var,
                    value=option,
                    font=("Arial", 12),
                    bg="#f4f4f9",
                    fg="#333",
                    activebackground="#d6e4ff",
                    activeforeground="#000",
                    wraplength=450,
                    anchor="w",
                    justify="left",
                ).pack(anchor="w")
        else:
            self.end_quiz()

    def check_answer(self):
        """Vérifie si la réponse est correcte."""
        selected_option = self.options_var.get()
        if not selected_option:
            messagebox.showwarning("Alerte", "Veuillez sélectionner une réponse.")
            return

        correct_answer = self.questions[self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            messagebox.showinfo("Résultat", "Correct ! 🎉")
        else:
            messagebox.showinfo(
                "Résultat", f"Faux. La bonne réponse était : {correct_answer}"
            )

        self.current_question_index += 1
        self.update_score()
        self.display_question()

    def update_score(self):
        """Met à jour l'affichage du score."""
        self.score_label.config(text=f"Score : {self.score}")

    def end_quiz(self):
        """Affiche le score final et termine le jeu."""
        messagebox.showinfo(
            "Fin du Quiz", f"Quiz terminé ! Votre score final est : {self.score}/{len(self.questions)}"
        )
        self.root.destroy()


# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = StylishQuizApp(root)
    root.mainloop()
