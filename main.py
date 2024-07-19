#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def dice_roll() -> int:
    """
    Simule le jet d'un dé à 6 faces
    """
    return random.choice(range(1, 6))


def main():
    ...


if __name__ == '__main__':
    main()


