import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Charger les données
data = pd.read_csv("data.csv")
X = data["commentaire"]
y = data["label"]

# Entraîner le modèle
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

def analyser():
    texte = entree.get()
    vect = vectorizer.transform([texte])
    resultat = model.predict(vect)[0]
    resultat_label.config(text=f"Sentiment : {resultat}")

# Interface
fenetre = tk.Tk()
fenetre.title("Sentiment ai 📆")
fenetre.geometry("400x200")

titre = tk.Label(fenetre, text="Analyseur de sentiment", font=("Times New Romans", 16, "bold"))
titre.pack(pady=10)

entree = tk.Entry(fenetre, width=45)
entree.pack(pady=10)

bouton = tk.Button(fenetre, text="Analyser", command=analyser)
bouton.pack(pady=10)

resultat_label = tk.Label(fenetre, text="", font=("Times New Romans", 14))
resultat_label.pack(pady=10)

fenetre.mainloop()
