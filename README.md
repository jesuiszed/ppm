# Playpark Manager (PPM)

## Description
Playpark Manager (PPM) est un projet Django conçu pour gérer un parc de loisirs. Il offre des fonctionnalités telles que la gestion des attractions, des employés, etc.

## Installation
1. Cloner le dépôt depuis GitHub :
    ```
    git clone https://github.com/jesuiszed/ppm.git
    cd ppm
    ```

2. Installer les dépendances Python :
    ```
    pip install -r requirements.txt
    ```

3. Appliquer les migrations de la base de données :
    ```
    python manage.py migrate
    ```

4. Créer un superutilisateur pour accéder à l'interface d'administration :
    ```
    python manage.py createsuperuser
    ```

5. Lancer le serveur de développement :
    ```
    python manage.py runserver
    ```

6. Accéder à l'application dans votre navigateur à l'adresse suivante : `http://zedflorian.pythonanywhere.com/admin`

## Connexion
Pour accéder à l'interface d'administration, utilisez les informations de connexion suivantes :

- Nom d'utilisateur : kou
- Mot de passe : kou

## Fonctionnalités
- Gestion des attractions
- Gestion des employés
- etc.

## Contributions
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une pull request ou à signaler un problème.

## Auteurs
- Kokou Florian(https://github.com/jesuiszed)

## Licence
Ce projet est sous licence [MIT](LICENSE).
