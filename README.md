# 🎯 TaskRT — Simulateur pédagogique d'ordonnancement Temps Réel

**TaskRT** est une application web pédagogique permettant de **simuler et visualiser les algorithmes d’ordonnancement temps réel** tels que :

- EDF (Earliest Deadline First)

Priorité dynamique : à chaque instant, on sélectionne la tâche dont la deadline absolue est la plus proche.

Très efficace lorsque la charge CPU totale ≤ 100%.

C’est optimal sur mono-processeur sans préemption coûteuse.

- RM (Rate Monotonic Scheduling)

Priorité statique : la tâche ayant la période la plus courte a la plus haute priorité.

Simple mais moins flexible que EDF.

Peut devenir impossible à planifier quand les tâches ont des périodes très différentes.

- DM (Deadline Monotonic Scheduling)

Variante de RM : priorité statique basée sur les deadlines (plus la deadline est courte, plus la priorité est haute).

Si deadlines ≈ périodes → DM devient équivalent à RM.

Peut être plus performant que RM quand les deadlines sont < périodes.

- FIFO (First In First Out)

Très simple : on exécute toujours la tâche arrivée en premier.

Pas du tout optimal pour des systèmes critiques.

Peut provoquer des violations de deadline même si le système est théoriquement faisable.

Le but est d’aider les étudiants, enseignants, ingénieurs et chercheurs à comprendre le comportement des ordonnanceurs temps réel à travers des simulations interactives et des diagrammes de Gantt dynamiques.

---

## 🚀 Fonctionnalités principales

✅ Support de plusieurs algorithmes d’ordonnancement :

- **EDF (Earliest Deadline First)**
- **RM (Rate Monotonic)**
- **DM (Deadline Monotonic)**
- **FIFO (First In First Out)**

✅ Interface web interactive 100% en ligne

✅ Visualisation sous forme de diagramme de Gantt (Chart.js)

✅ Analyse automatique de faisabilité :

- Calcul de la charge CPU totale
- Détection de surcharge (> 100% d’utilisation CPU)

✅ Léger, sans base de données

✅ Parfait pour les **cours d’informatique temps réel, TP étudiants, et démonstrations pédagogiques**

---

## 🎯 Objectifs pédagogiques

- Visualiser les décisions de planification et les préemptions en temps réel
- Comparer les approches d’ordonnancement statique vs dynamique
- Apprendre les tests de faisabilité (borne de Liu & Layland, surcharge)
- Observer l’impact des délais et priorités
- Renforcer les concepts fondamentaux : priorités, deadlines, préemption, périodicité, surcharge

---

## 🛠 Stack technique

| Composant | Technologie |
| --------- | ----------- |
| **Backend** | Python 3 + Flask |
| **Frontend** | HTML5 + Bootstrap 5 |
| **Visualisation** | Chart.js (Gantt via plugin) |
| **Déploiement cloud** | Render (hébergement gratuit possible) |

---

## 📦 Installation locale

Cloner le projet et exécuter localement :

```bash
git clone https://github.com/EJM0101/taskrt
cd taskrt
pip install -r requirements.txt
python app.py
```

---

## 🌐 Déploiement sur Render

L’application est totalement déployable gratuitement sur **Render.com** via :

- Le fichier `render.yaml` fourni
- Commande de build automatique : `pip install -r requirements.txt`
- Serveur de production : Gunicorn avec la commande :

    ```bash
    gunicorn app:app
    ```

L’application est immédiatement accessible en ligne après le déploiement.

---

## 🧪 Exemple de simulation

### Exemple de tâches à entrer :

| Tâche | Exécution | Période | Deadline |
| ----- | ---------- | ------- | -------- |
| T1    | 1          | 4       | 4        |
| T2    | 2          | 5       | 5        |
| T3    | 1          | 10      | 10       |

### Étapes de simulation :

- Choisir l’algorithme souhaité (EDF, RM, DM ou FIFO)
- Lancer la simulation
- Observer la visualisation du planning Gantt et le résultat de faisabilité

---

## 🔐 Pourquoi utiliser TaskRT ?

- Simplifie l’apprentissage des systèmes temps réel
- Très visuel et interactif pour les étudiants
- Permet de tester des scénarios en conditions normales et en surcharge
- Aucun besoin de base de données ni de dépendances lourdes

---

## 👨‍🏫 Développé par

**Emman Mlmb 🇨🇩**  
Université de Kinshasa — Licence 3 Informatique  
Projet de cours **Informatique Temps Réel**

---

## 💡 Perspectives d’amélioration

- Mode de simulation pas-à-pas
- Export PDF ou image du diagramme de Gantt
- Calcul des blocages (blocking time)
- Gestion de la gigue (jitter)
- Ajout de scénarios aléatoires générés automatiquement pour des TP

---

> Ce simulateur est librement utilisable dans le cadre pédagogique.