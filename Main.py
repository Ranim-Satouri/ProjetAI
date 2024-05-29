import tkinter as tk
import random
from tkinter import messagebox
from a_star import AStarSolver
from collections import deque
from BFS import BFSSolver

class EightPuzzle:
    def __init__(self, master):
        # Initialisation de la fenêtre principale
        self.master = master
        self.master.title("8-Puzzle Game")
        self.master.geometry("290x370")
        self.tiles = [[None for _ in range(3)] for _ in range(3)]
        self.empty_tile = (2, 2)
        self.initialize_puzzle()
        self.create_buttons()
        self.master.config(bg="#FFB6C1")

    def initialize_puzzle(self):
        # Initialisation du puzzle en mélangeant les nombres
        numbers = list(range(1, 9)) + [0]
        random.shuffle(numbers)
        idx = 0
        for i in range(3):
            for j in range(3):
                number = numbers[idx]
                idx += 1
                self.tiles[i][j] = number
                if number == 0:
                    self.empty_tile = (i, j)
        
    def create_buttons(self):
        # Création des boutons pour afficher les tuiles du puzzle
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j] != 0:
                    btn = tk.Button(self.master, text=str(self.tiles[i][j]), font=('Arial', 24), width=4, height=2)
                    btn.grid(row=i, column=j, padx=5, pady=5)
                    self.buttons[i][j] = btn
                else:
                    self.buttons[i][j] = None
        # Bouton pour réinitialiser le puzzle
        reset_button = tk.Button(self.master, text="Reset", width=9, height=1, font=('Arial', 10), command=self.reset)
        reset_button.grid(row=3, column=1, padx=5, pady=5)
        # Boutons pour exécuter les algorithmes de résolution
        a_star_button = tk.Button(self.master, text="A*", width=9, height=1, font=('Arial', 10), command=self.run_a_star)
        a_star_button.grid(row=3, column=0, padx=5, pady=5)

        bfs_button = tk.Button(self.master, text="BFS", width=9, height=1, font=('Arial', 10), command=self.run_bfs)
        bfs_button.grid(row=3, column=2, padx=5, pady=5)
            
    def reset(self):
        # Méthode pour réinitialiser le puzzle
        self.shuffle()

    def shuffle(self):
        # Méthode pour mélanger les tuiles du puzzle
        self.initialize_puzzle()
        self.update_ui_with_state(self.tiles)
        
    def update_ui_with_state(self, state):
        # Méthode pour mettre à jour l'interface utilisateur avec un nouvel état du puzzle
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    if self.buttons[i][j]:
                        self.buttons[i][j].grid_forget()
                        self.buttons[i][j] = None
                else:
                    if self.buttons[i][j]:
                        self.buttons[i][j].config(text=str(state[i][j]))
                    else:
                        btn = tk.Button(self.master, text=str(state[i][j]), font=('Arial', 24), width=4, height=2)
                        btn.grid(row=i, column=j, padx=5, pady=5)
                        self.buttons[i][j] = btn

    def animate_solution(self, solution ,time):
        # Méthode pour animer la solution trouvée
        if solution:
            def step(index):
                if index < len(solution):
                    self.update_ui_with_state(solution[index])
                    self.master.after(time, step, index + 1)  # Mise à jour toutes les 'time' millisecondes
            step(0)
        else:
            messagebox.showinfo("Result", "No solution found.")

    def run_a_star(self):
        # Méthode pour exécuter l'algorithme A*
        initial_state = tuple(map(tuple, self.tiles))
        goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        solution, iterations = AStarSolver.solve_puzzle(initial_state, goal_state)
        self.animate_solution(solution,800)
        if solution:
            print("Solution found:")
            i = 0
            for step in solution:
                i += 1
                print("Step:", i)
                for s in step:
                    print(s)
                print("-------------")
            print("resolved in ", i, " step")    
            print("Resolved in ", iterations, " iterations")
        else:
            print("No solution found.")

    def run_bfs(self):
        # Méthode pour exécuter l'algorithme BFS
        initial_state = tuple(map(tuple, self.tiles))
        goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
        solution, iterations = BFSSolver.solve_puzzle(initial_state, goal_state)
        self.animate_solution(solution,600)
        if solution:
            print("Solution found:")
            i = 0
            for step in solution:
                i += 1
                print("Step:", i)
                for s in step:
                    print(s)
                print("-------------")
            print("resolved in ", i, " step")
            print("Resolved in ", iterations, " iterations")
        else:
            print("No solution found.")

if __name__ == "__main__":
    # Création de la fenêtre principale et démarrage de l'application
    root = tk.Tk()
    game = EightPuzzle(root)
    root.mainloop()
