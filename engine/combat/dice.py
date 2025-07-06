# Dice rolling system
import random

def roll_dice(sides: int = 20, times: int = 1):
    return [random.randint(1, sides) for _ in range(times)]