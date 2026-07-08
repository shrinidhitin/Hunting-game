import numpy as np
import tkinter as tk
import random
from tkinter import messagebox

width = 10
height = 10

emoji = {
    0: "⬜",
    1: "👹",
    2: "💰",
    3: "🍖",
    4: "🏹"
}

board = np.zeros((height, width), dtype=int)
revealed = np.zeros((height, width), dtype=bool)

def board(width, height):
    number_of_monsters = random.randint(10, 15)
    number_of_gold = 10
    number_of_meat = 10
    number_of_arrows = random.randint(8, 12)
    for i in range(number_of_monsters):
        while True:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            if board[y][x] == 0:
                board[y][x] = 1
                break
        for i in range(number_of_gold):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if board[y][x] == 0:
                    board[y][x] = 2
                    break
        for i in range(number_of_meat):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if board[y][x] == 0:
                    board[y][x] = 3
                    break
        for i in range(number_of_arrows):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if board[y][x] == 0:
                    board[y][x] = 4
                    break
    emoji_board = np.vectorize(emoji.get)(board)
    return emoji_board




inventory = {
    "meat": 0,
    "gold": 0,
    "arrows": 0
}


