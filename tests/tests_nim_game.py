import tkinter as tk
from src.Nim_Game import Nim_Game


def test_nim_game():
    player1 = input("Player 1 :")
    player2 = input("Player 2 :")
    window = tk.Tk()
    Nim_Game(window, player1, player2)
    window.mainloop()

# ================================
# Main
# ================================

test_nim_game()