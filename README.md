### **Avancement:** ![](https://geps.dev/progress/80)
___

# Harnessed-Trotting-Race-Simulator

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Description

"Harnessed-Trotting-Race-Simulator" est un simulateur de course de trot attelé. Ce projet permet de simuler une course où 12 à 20 chevaux tractant chacun un sulky, menés par des drivers, s'affrontent sur une piste rectiligne de 2 400 mètres. La course peut être configurée en tiercé, quarté ou quinté. Les chevaux doivent maintenir l'allure du trot sous peine de disqualification pour passage au galop.

## Fonctionnalités

- **Configuration initiale** : L'utilisateur saisit le nombre de chevaux (12 à 20) et le type de course (tiercé, quarté ou quinté).
- **Simulation de course** : 
  - La course se déroule comme un jeu de plateau.
  - À chaque tour, un jet de dé à 6 faces détermine une altération possible de la vitesse de chaque cheval (augmentation, stabilisation, diminution).
  - La vitesse mise à jour détermine la distance parcourue par chaque cheval.
  - Chaque tour représente 10 secondes de la course.
  - L'utilisateur avance la course tour par tour à la suite d'un message du programme.
- **Disqualification** : Les chevaux passant au galop sont disqualifiés.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/votre-utilisateur/Harnessed-Trotting-Race-Simulator.git
    ```
2. Accédez au répertoire du projet :
    ```bash
    cd Harnessed-Trotting-Race-Simulator
    ```
3. Installez les dépendances nécessaires (si applicable).

## Utilisation

1. Lancez le programme :
    ```bash
    python main.py
    ```
2. Saisissez le nombre de chevaux et le type de course lorsque le programme le demande.
3. Avancez la course en suivant les instructions affichées à chaque tour.

## Exemples

- **Configuration initiale** :
    ```
    Nombre de chevaux (12-20) : 15
    Type de course (tiercé (3), quarté (4), quinté (5)) : 3
    ```
- **Déroulement d'un tour de course** :
    ```
    Tour 1 :
    Cheval 1 : vitesse augmentée, distance parcourue : 120 m
    Cheval 2 : vitesse stabilisée, distance parcourue : 115 m
    ...
    Appuyez sur Entrée pour continuer au tour suivant.
    ```
## Prérequis

- Python 3.x installé sur votre machine.

## Installation

Clonez ce dépôt sur votre machine locale :

```bash
git clone [https://github.com/JneiraS/Harnessed-Trotting-Race-Simulator.git]
cd Harnessed-Trotting-Race-Simulator
