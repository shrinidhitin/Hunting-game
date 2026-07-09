import numpy as np
import tkinter as tk
import random

width = 10
height = 10

def place_tiles(board, tile, count, width, height):
    placed = 0
    while placed < count:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if board[y][x] == 0:
            board[y][x] = tile
            placed += 1

def gen_board(width, height):
    board = np.zeros((height, width), dtype=float)
    number_of_monsters = random.randint(10, 15)
    number_of_gold = 10
    number_of_meat = 10
    number_of_arrows = random.randint(7, 10)
    place_tiles(board, 1, number_of_monsters, width, height)
    place_tiles(board, 2, number_of_gold, width, height)
    place_tiles(board, 3, number_of_meat, width, height)
    place_tiles(board, 4, number_of_arrows, width, height)
    for y in range(height):
        for x in range(width):
            tile = board[y][x]
            if tile == 1:
                for i in range(max(0, y - 1), min(height, y + 2)):
                    for j in range(max(0, x - 1), min(width, x + 2)):
                        if board[i][j] == 0:
                            board[i][j] += 0.1
    return board
    
    

emoji = {
    0: "⬜",
    0.1: "🟨",
    0.2: "🟥",
    1: "👹",
    2: "💰",
    3: "🍖",
    4: "🏹"
}
 
def get_emoji_board(board):
    
    emoji_board = np.vectorize(emoji.get)(board)
    return emoji_board

   

