# 🔌 MLOps App

Une application MLOps complète combinant FastAPI, MongoDB et Streamlit pour la prédiction de fleurs Iris et la gestion de fruits.

## 📋 Description

Ce projet est une application de démonstration MLOps qui comprend :
- **Backend FastAPI** : API REST pour les prédictions de modèle ML et la gestion de données
- **Frontend Streamlit** : Interface utilisateur interactive
- **Base de données MongoDB** : Stockage des données
- **Modèle ML** : RandomForestClassifier entraîné sur le dataset Iris

## 🏗️ Architecture

```
.
├── client/
│   ├── app.py              # Interface Streamlit
│   ├── requirements.txt    # Dépendances client
│   └── Dockerfile
├── server/
│   ├── app.py              # API FastAPI
│   ├── train.py            # Script d'entraînement du modèle
│   ├── model.pkl           # Modèle ML sauvegardé
│   ├── requirements.txt    # Dépendances serveur
│   └── Dockerfile
└── docker-compose.yml
```

## ⚙️ Fonctionnalités

### Backend (FastAPI)
- ✅ Endpoint de santé (`/`)
- ➕ Ajout de fruits (`/add/{fruit}`)
- 📋 Liste des fruits (`/list`)
- 🌸 Prédiction de fleurs Iris (`/predict`)

### Frontend (Streamlit)
- 🔌 Vérification du statut de l'API
- 🍎 Ajout de fruits dans MongoDB
- 📋 Affichage de la liste des fruits
- 🌸 Prédiction interactive de fleurs Iris avec animations

## 🚀 Installation

### Prérequis
- Docker
- Docker Compose

### Étape 1 : Entraîner le modèle (facultatif si fichier pkl déjà présent)

Avant de construire les images Docker, entraînez le modèle ML :

```bash
python train.py
```

Cette commande va :
1. Charger le dataset Iris
2. Entraîner un RandomForestClassifier
3. Sauvegarder le modèle dans `server/model.pkl`

### Étape 2 : Construire les images Docker

Construisez les trois images Docker nécessaires :

```bash
# 1. Image du client Streamlit
docker build -t mlops-client ./client

# 2. Image du serveur FastAPI
docker build -t mlops-server ./server

# 3. Image MongoDB (sera téléchargée automatiquement)
docker pull mongo

# 4. Lancer tous les services avec docker-compose
docker-compose up
```

### Étape 3 : Accéder à l'application

Une fois les conteneurs démarrés :

- **Interface Streamlit** : http://localhost:8501
- **API FastAPI** : http://localhost:8000
- **Documentation API** : http://localhost:8000/docs

## 📦 Dépendances

### Serveur (FastAPI)
```
fastapi==0.110.0
uvicorn==0.29.0
pymongo==4.7.2
scikit-learn
joblib
pydantic
pandas
numpy
```

### Client (Streamlit)
```
streamlit==1.35.0
streamlit_extras
requests
```

## 🔧 Utilisation

### Ajouter un fruit
1. Entrez le nom d'un fruit dans le champ texte
2. Cliquez sur "Ajouter"
3. Une animation de neige apparaît en cas de succès

### Prédire une fleur Iris
1. Entrez les 4 mesures de la fleur :
   - Sepal length (longueur du sépale)
   - Sepal width (largeur du sépale)
   - Petal length (longueur du pétale)
   - Petal width (largeur du pétale)
2. Cliquez sur "Prédire"
3. Le type de fleur est affiché avec une animation d'emojis :
   - 🌺 Setosa
   - 🌼 Virginica
   - 🌻 Versicolor

## 🛠️ Commandes utiles

```bash
# Arrêter les conteneurs
docker-compose down

# Voir les logs
docker-compose logs -f

# Reconstruire et relancer
docker-compose up --build

# Nettoyer les conteneurs et images
docker-compose down --rmi all -v
```

## 📊 Modèle ML

Le modèle utilise un **RandomForestClassifier** avec les paramètres suivants :
- `n_estimators=100`
- `random_state=42`
- Entraîné sur 80% du dataset Iris
- Testé sur 20% du dataset

Les classes prédites sont :
- **Setosa** (classe 0)
- **Versicolor** (classe 1)
- **Virginica** (classe 2)

## 🐛 Troubleshooting

**Problème : L'API n'est pas accessible depuis Streamlit**
- Vérifiez que tous les conteneurs sont démarrés : `docker-compose ps`
- Attendez quelques secondes que les services soient complètement initialisés

**Problème : Le modèle n'est pas trouvé**
- Assurez-vous d'avoir exécuté `python train.py` avant de construire l'image serveur
- Vérifiez que `server/model.pkl` existe

**Problème : Port déjà utilisé**
- Modifiez les ports dans `docker-compose.yml` si 8000 ou 8501 sont déjà utilisés

## 📝 License

Ce projet est un exemple éducatif pour démontrer une architecture MLOps simple.