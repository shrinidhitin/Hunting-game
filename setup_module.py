import numpy as np
import tkinter as tk
import random
from tkinter import messagebox

width = 10
height = 10

board = np.zeros((height, width), dtype=int)

def place_tiles(board, tile, count, width, height):
    placed = 0
    while placed < count:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if board[y][x] == 0:
            board[y][x] = tile
            placed += 1

def gen_board(width, height):
    emoji = {
    0: "⬜",
    1: "👹",
    2: "💰",
    3: "🍖",
    4: "🏹"
}
    number_of_monsters = random.randint(10, 15)
    number_of_gold = 10
    number_of_meat = 10
    number_of_arrows = random.randint(8, 12)
    place_tiles(board, 1, number_of_monsters, width, height)
    place_tiles(board, 2, number_of_gold, width, height)
    place_tiles(board, 3, number_of_meat, width, height)
    place_tiles(board, 4, number_of_arrows, width, height)

    emoji_board = np.vectorize(emoji.get)(board)
    return emoji_board


    

