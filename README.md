# Projet d'Analyse Énergétique

Ce projet est une application web pour l'analyse des données énergétiques. Il utilise Flask pour le backend et inclut des fonctionnalités pour visualiser les données et générer des rapports.

## Structure du Projet

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/aouadayoub/energy_consumption_prediction.git
    ```
2. Créez un environnement virtuel :
    ```sh
    python -m venv enerygy
    ```
3. Activez l'environnement virtuel :
    - Sur Windows :
        ```sh
        .\enerygy\Scripts\activate
        ```
    - Sur macOS/Linux :
        ```sh
        source enerygy/bin/activate
        ```
4. Installez les dépendances :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez l'application Flask :
    ```sh
    python app.py
    ```
2. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

## Structure des Dossiers

- [app.py](http://_vscodecontentref_/6) : Le fichier principal pour lancer l'application Flask.
- [enerygy](http://_vscodecontentref_/7) : Contient l'environnement virtuel et les dépendances.
- [model.pkl](http://_vscodecontentref_/8) : Le modèle de machine learning pré-entraîné.
- [notboook.ipynb](http://_vscodecontentref_/9) : Un notebook Jupyter pour l'analyse des données.
- [requirements.txt](http://_vscodecontentref_/10) : Liste des dépendances Python.
- [static](http://_vscodecontentref_/11) : Contient les fichiers statiques (CSS, images, JavaScript).
- [templates](http://_vscodecontentref_/12) : Contient les templates HTML pour l'application web.

## Contribuer

1. Forkez le projet.
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`).
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Poussez votre branche (`git push origin feature/AmazingFeature`).
5. Ouvrez une Pull Request.
