#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def dice_roll() -> int:
    """
    Simule le jet d'un dé à 6 faces
    """
    return random.choice(range(1, 6))


def alteration_of_speed(actual_speed: int) -> int:
    """
    Calcule l'altération de vitesse en fonction de la vitesse actuelle, d'un lancé de dé simulé par la
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


def horse_progress(speed: int) -> int:
    """
    Calcule la progression d'un cheval en fonction de sa vitesse actuelle.
    """
    return [i * 23 for i in range(7)][speed]


def horse(num: int) -> dict:
    """
    Crée un cheval avec un nom, une vitesse initiale et une distance parcourue initiale.
    """
    return {'Name': f'Horse_{num}',
            'Speed': 0,
            'Distances covered': 0
            }


def horse_factory(number_of_horses: int):
    """
    Crée une liste de chevaux en utilisant la fonction horse.
    """
    return [horse(n+1) for n in range(number_of_horses)]


def main():
    ...


if __name__ == '__main__':
    print(horse_factory(12))
