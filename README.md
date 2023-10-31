# TodoList - Gestionnaire de Tâches

TodoList est une application de gestion de tâches simple et efficace pour vous aider à organiser votre vie quotidienne.

<!-- ![Aperçu de Taskify](link-to-image.png) -->

## Fonctionnalités Principales

- Créer, modifier et supprimer des tâches.
- Marquer les tâches comme terminées.
- Filtrer les tâches par statut (en cours, terminées) et priorité.
- Gestion des utilisateurs.

## Installation

1. Clonez ce référentiel sur votre machine locale :

   ```bash
   git clone https://github.com/votre-utilisateur/taskify.git

2. Installez poetry :

   ```bash
   pip install poetry

3. Installez les dépendances du projet :

   ```bash
   poetry install

4. Creer ensuite un repertoire de logs :

   ```bash
   mkdir logs

5. Lancer ensuite le pojoet :

   ```bash
   poetry run streamlit run src/accueil.py

NB: Le fichier .env a été volontairemnt laissé dans le projet afin de permettre à toutes les personnes ayant accès au projet de le lancer aisement.
