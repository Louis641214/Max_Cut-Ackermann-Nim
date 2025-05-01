import random
from PIL import Image, ImageTk
import tkinter as tk


class Nim_Game:

    def __init__(self, window, player1, player2):

        self.window = window
        self.window.title('Nim Game')
        self.window.geometry('700x300')
        self.window.resizable(False, False)

        self.matches = 16
        self.match_image = ImageTk.PhotoImage(Image.open('src/match.jpg').resize((30, 100)))
        self.players = [player1, player2]
        self.current_player_index = random.choice([0, 1])

        self.matches_area = tk.Frame(self.window)
        self.matches_area.pack(pady=12)

        self.message= tk.Label(self.window, text='To start the game, press start')
        self.message.pack()

        self.buttons_area = tk.Frame(self.window)
        self.buttons_area.pack(pady=12)

        self.launch_game()
    
    def launch_game(self):
        tk.Button(self.buttons_area, text="start", command=self.initialize_game).pack()

    def initialize_game(self):
        self.buttons_area.winfo_children()[0].destroy()

        for i in range(1, 4):
            tk.Button(self.buttons_area, text=f"{i}", command=lambda x=i: self.remove(x)).pack(side=tk.LEFT, padx=7)
        self.display_matches()

    def display_matches(self):
        for widget in self.matches_area.winfo_children():
            widget.destroy()

        for _ in range(self.matches):
            tk.Label(self.matches_area, image=self.match_image).pack(side=tk.LEFT, padx=4)

        self.message.config(text=f"{self.players[self.current_player_index]}'s turn : {self.matches} matches remaining")

    def remove(self, n):

        if n > self.matches:
            self.message.config(text=f"Too many matches : Try again {self.players[self.current_player_index]} : {self.matches} matches remaining!")
            return

        self.matches -= n
        self.display_matches()

        if self.matches == 0:
            self.message.config(text=f"You took the last one {self.players[self.current_player_index]}. You lose !")
            self.end_game()
        else:
            self.current_player_index = 1 - self.current_player_index
            self.message.config(text=f"{self.players[self.current_player_index]}'s turn : {self.matches} matches remaining")
    
    def end_game(self):
        for widget in self.buttons_area.winfo_children():
            widget.destroy()

        tk.Button(self.buttons_area, text="end game", command= self.window.destroy).pack()
