#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
import time


def dice_roll() -> int:
    """
    Simule le jet d'un dé à 6 faces
    """
    return random.choice(range(1, 6))


def alteration_of_speed(actual_speed: int) -> int:
    """
    Calcule l'altération de vitesse en fonction de la vitesse actuelle, d'un jet de dé simulé par la
    fonction dice_roll() et d'une matrice.
    La matrice contient des valeurs numériques représentant l'altération de vitesse ainsi qu'une valeur
    'DQ' qui représenter une disqualification.

    :return:
    """
    sheet: list[list] = [
        [1, 2, 3, 4, 5, 6],
        [0, 1, 1, 1, 2, 2],
        [0, 0, 1, 1, 1, 2],
        [0, 0, 1, 1, 1, 2],
        [-1, 0, 0, 1, 1, 1],
        [-1, 0, 0, 0, 1, 1],
        [-2, -1, 0, 0, 0, 1],
        [-2, -1, 0, 0, 0, 'DQ'],
    ]
    dice: int = dice_roll()
    return sheet[actual_speed + 1][dice - 1]


def horse_progress(actual_speed: int) -> int:
    """
    Calcule la progression d'un cheval en fonction de sa vitesse actuelle.
    """
    return [i * 23 for i in range(7)][actual_speed]


def horse(num: int) -> dict:
    """
    Crée un cheval avec un nom, une vitesse initiale et une distance parcourue initiale.
    """
    return {'Name': f'Horse_{num}',
            'Speed': 0,
            "Distances covered": 0
            }


def horse_factory(number_of_horses: int):
    """
    Crée une liste de chevaux en utilisant la fonction horse.
    """
    return [horse(n + 1) for n in range(number_of_horses)]


def game_conf() -> tuple[list[dict], int]:
    """
    Configure la course en demandant à l'utilisateur de saisir le nombre de chevaux et le type de course.

    Les entrées sont validées pour s'assurer qu'elles sont numériques et dans les plages spécifiées :
    - Le nombre de chevaux doit être entre 12 et 20 inclus.
    - Le type de course doit être 3 (tiercé), 4 (quarté) ou 5 (quinté).

    :return: Une liste de chevaux et le type de course si les entrées sont valides.
    """
    options: list = [
        input("\nNombre de chevaux (12 à 20): "),
        input("Type de course (tiercé (3), quarté(4), quinté(5): "),
    ]

    if (
            options[0].isnumeric()  # Vérifie si le premier élément est un nombre.
            and options[1].isnumeric()  # Vérifie si le deuxième élément est un nombre.
            and 12 <= int(options[0]) <= 20  # Vérifie si le premier élément est entre 12 et 20 inclus.
            and 3 <= int(options[1]) <= 5  # Vérifie si le deuxième élément est entre 3 et 5 inclus.
    ):
        return horse_factory(int(options[0])), int(options[1])

    else:
        print(
            "Attention! vous devez saisir des entiers dans les conditions demandées")


def game_round(participants):
    """
    Effectue un tour de jeu pour chaque participant.
    """
    for participant in participants:
        participant['Speed'] = alteration_of_speed(participant['Speed'])
        participant['Distances covered'] += horse_progress(participant['Speed'])


def visual_progression(hosres: list[dict]):
    """
    Affiche la progression visuelle de chaque cheval sur la piste.
    """
    for h in hosres:
        print('-' * (h['Distances covered'] // 23) + 'P')


def crossed_the_finish_line(horses, list_of_winners):
    """
    Vérifie quels chevaux ont franchi la ligne d'arrivée et les ajoute à la liste des gagnants.
    """
    for h in horses:
        if h['Distances covered'] > 2400:
            winners = horses.pop(horses.index(h))
            list_of_winners.append(winners)


def display_of_winners(winners: list):
    """
    Affiche les gagnants dans l'ordre d'arrivée.
    """
    print(f"\tDans l'ordre d'arrivé les gagnats son:\n")
    for winer in winners:
        print(f"\t{winer['Name']}")


def main():
    horses, type_of_race = game_conf()
    list_of_winners: list = []

    while len(list_of_winners) < type_of_race:
        game_round(horses)
        visual_progression(horses)
        crossed_the_finish_line(horses, list_of_winners)
        time.sleep(.1)
        os.system('cls')

    display_of_winners(list_of_winners)

    input('FINISH')


if __name__ == '__main__':
    main()
