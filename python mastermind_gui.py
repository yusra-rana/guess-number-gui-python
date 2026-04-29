import random
import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Mastermind Number Guessing Game')
        self.root.geometry('420x380')
        self.root.resizable(False, False)

        self.secret = random.randrange(1000, 10000)
        self.tries = 0

        tk.Label(root, text='Guess the 4 Digit Number', font=('Arial', 16, 'bold')).pack(pady=15)

        self.entry = tk.Entry(root, font=('Arial', 18), justify='center')
        self.entry.pack(pady=10)

        tk.Button(root, text='Check Guess', font=('Arial', 12), command=self.check_guess).pack(pady=8)
        tk.Button(root, text='New Game', font=('Arial', 12), command=self.new_game).pack(pady=4)

        self.result = tk.Label(root, text='', font=('Arial', 12), wraplength=360)
        self.result.pack(pady=15)

        self.history = tk.Text(root, height=10, width=45)
        self.history.pack(pady=10)
        self.history.config(state='disabled')

    def check_guess(self):
        guess = self.entry.get().strip()
        if not guess.isdigit() or len(guess) != 4:
            messagebox.showerror('Invalid Input', 'Enter exactly 4 digits.')
            return

        self.tries += 1
        guess_num = int(guess)

        if guess_num == self.secret:
            self.result.config(text=f'Congratulations! You guessed it in {self.tries} tries.')
            self.add_history(f'{guess} -> Correct!')
            return

        correct = 0
        secret_str = str(self.secret)
        for i in range(4):
            if guess[i] == secret_str[i]:
                correct += 1

        self.result.config(text=f'You got {correct} digit(s) in correct position.')
        self.add_history(f'{guess} -> {correct} correct')
        self.entry.delete(0, tk.END)

    def add_history(self, text):
        self.history.config(state='normal')
        self.history.insert(tk.END, text + '\n')
        self.history.config(state='disabled')
        self.history.see(tk.END)

    def new_game(self):
        self.secret = random.randrange(1000, 10000)
        self.tries = 0
        self.result.config(text='New game started!')
        self.entry.delete(0, tk.END)
        self.history.config(state='normal')
        self.history.delete('1.0', tk.END)
        self.history.config(state='disabled')

root = tk.Tk()
app = MastermindGame(root)
root.mainloop()
