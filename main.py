import tkinter as tk
import random
import numpy as np
import setup_module as sm

width = 10
height = 10
root = tk.Tk()
root.title("Hunting for your village")

board = sm.gen_board(width, height)
revealed = np.zeros((height, width), dtype=bool)
result_label = tk.Label(root, text="")
result_label.grid(row=13, column=0, columnspan=5, pady=10)

def reveal_tile(x, y):
    if not revealed[x][y]:
        revealed[x][y] = False
        buttons[x][y].config(text=board[x][y])
    if revealed[x][y] == False:
        tile = board[x][y]
        if tile == "🏹":
            inventory["arrows"] += 1
            revealed[x][y] = True
        if tile == "🍖":
            inventory["meat"] += 1
            revealed[x][y] = True
        if tile == "💰":
            inventory["gold"] += 1
            revealed[x][y] = True
        if tile == "👹":
            if inventory["arrows"] > 0:
                inventory["arrows"] -= 1
                result_label.config(text="Monster Defeated", fg="blue")
            else:
                result_label.config(text="Game Over", fg="red")
                for y in range(height):
                    for x in range(width):
                        revealed[x][y] = True
        if inventory["meat"] >= 10 and inventory["gold"] >= 10:
            result_label.config(text="You Win! You can now feed the villagers.", fg="green")
    
    update_inventory_label()

def clear():
    result_label.config(text="")
    for row in range(height):
        for col in range(width):
            buttons[row][col].config(text="")
            revealed[row][col] = False
    inventory["arrows"] = 0
    inventory["meat"] = 0
    inventory["gold"] = 0

    update_inventory_label()


inventory = {
        "meat": 0,
        "gold": 0,
        "arrows": 0
    }

inventory_label = tk.Label(root, font=("Arial", 14))
inventory_label.grid(row=11, column=0, columnspan=width)

def update_inventory_label():
    inventory_label.config(text=f"Inventory: Meat: {inventory['meat']}, Gold: {inventory['gold']}, Arrows: {inventory['arrows']}")


buttons = []
for row in range(height):
    button_row = []
    for col in range(width):
        button = tk.Button(root, text=" ", font=("Arial", 20), width=2, height=1, command=lambda x=row, y=col: reveal_tile(x, y))
        button.grid(row=row + 1, column=col)
        button_row.append(button)
    buttons.append(button_row)

clear_button = tk.Button(root, text="Clear Board", font=("Arial", 14), command=clear)
clear_button.grid(row=12, column=0, columnspan=width, pady=10)

root.mainloop()