# import random

# class HillClimbingSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
#         current_state = initial_state
#         while True:
#             neighbors = HillClimbingSolver.get_neighbors(current_state)
#             print("neighbors : ",neighbors)
#             next_state = min(neighbors, key=lambda state: HillClimbingSolver.heuristic(state, goal_state))
#             print(next_state)
#             if HillClimbingSolver.heuristic(next_state, goal_state) >= HillClimbingSolver.heuristic(current_state, goal_state):
#                 print("ga3mezna")
#                 print(HillClimbingSolver.heuristic(next_state, goal_state))
#                 print(HillClimbingSolver.heuristic(current_state, goal_state))
#                 return None  # Local minimum or goal state reached
#             elif next_state == goal_state:
#                 return [initial_state, next_state]  # Solution found
#             else:
#                 current_state = next_state

#     @staticmethod
#     def get_neighbors(state):
#         neighbors = []
#         empty_tile_i, empty_tile_j = None, None
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     empty_tile_i, empty_tile_j = i, j

#         for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
#             if 0 <= new_i < 3 and 0 <= new_j < 3:
#                 new_state = [list(row) for row in state]
#                 new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
#                 neighbors.append(tuple(map(tuple, new_state)))

#         return neighbors

#     @staticmethod
#     def heuristic(state, goal_state):
#         # Manhattan distance heuristic
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] != goal_state[i][j] and state[i][j] != 0:
#                     tile = state[i][j] - 1
#                     x, y = divmod(tile, 3)
#                     target_x, target_y = None, None
#                     # Find the target position of the current tile
#                     for tx in range(3):
#                         for ty in range(3):
#                             if goal_state[tx][ty] == state[i][j]:
#                                 target_x, target_y = tx, ty
#                     distance += abs(target_x - i) + abs(target_y - j)
#         return distance
# --------------------------------------------
# import random

# class HillClimbingSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
#         current_state = initial_state
#         while True:
#             neighbors = HillClimbingSolver.get_neighbors(current_state)
#             # Select the best neighbor
#             next_state = min(neighbors, key=lambda state: HillClimbingSolver.heuristic(state, goal_state))

#             current_heuristic = HillClimbingSolver.heuristic(current_state, goal_state)
#             next_heuristic = HillClimbingSolver.heuristic(next_state, goal_state)
            
#             # Debug prints
#             print("Current state:", current_state)
#             print("Current heuristic:", current_heuristic)
#             print("Best next state:", next_state)
#             print("Next state heuristic:", next_heuristic)

#             # Check if the next state is the goal state
#             if next_state == goal_state:
#                 print("Solution found!")
#                 return [initial_state, next_state]  # Solution found

#             # Check for local minimum or no improvement
#             if next_heuristic >= current_heuristic:
#                 print("Stuck at a local minimum or no improvement, stopping.")
#                 return None

#             # Update current state
#             current_state = next_state

#     @staticmethod
#     def get_neighbors(state):
#         neighbors = []
#         empty_tile_i, empty_tile_j = None, None
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     empty_tile_i, empty_tile_j = i, j
#         moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         for move in moves:
#             new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
#             if 0 <= new_i < 3 and 0 <= new_j < 3:
#                 new_state = [list(row) for row in state]  # Copy state
#                 new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
#                 neighbors.append(tuple(map(tuple, new_state)))
#         return neighbors

#     @staticmethod
#     def heuristic(state, goal_state):
#         # Manhattan distance heuristic
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
#                     # Find the goal position of the current tile
#                     tile = state[i][j]
#                     target_x, target_y = None, None
#                     for tx in range(3):
#                         for ty in range(3):
#                             if goal_state[tx][ty] == tile:
#                                 target_x, target_y = tx, ty
#                     distance += abs(target_x - i) + abs(target_y - j)
#         return distance

# import random

# class HillClimbingSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
#         current_state = initial_state
#         visited_states = set()
#         visited_states.add(tuple(map(tuple, current_state)))  # Add the initial state to the visited set

#         while True:
#             neighbors = HillClimbingSolver.get_neighbors(current_state)
#             print("Current state:", current_state)
#             print("Current heuristic:", HillClimbingSolver.heuristic(current_state, goal_state))
#             print("Neighbors:", neighbors)
            
#             next_state = None
#             next_state_heuristic = float('inf')

#             for state in neighbors:
#                 state_heuristic = HillClimbingSolver.heuristic(state, goal_state)
#                 if state_heuristic < next_state_heuristic and state not in visited_states:
#                     next_state = state
#                     next_state_heuristic = state_heuristic

#             # if next_state is None or next_state_heuristic >= HillClimbingSolver.heuristic(current_state, goal_state):
#             #     print("Stuck at a local minimum or no improvement, stopping.")
#             #     return None  # Local minimum or no improvement found

#             if next_state == goal_state:
#                 print("Goal state reached!")
#                 return [initial_state, next_state]  # Solution found

#             visited_states.add(next_state)
#             current_state = next_state

#     @staticmethod
#     def get_neighbors(state):
#         neighbors = []
#         empty_tile_i, empty_tile_j = None, None
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] == 0:
#                     empty_tile_i, empty_tile_j = i, j

#         for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
#             if 0 <= new_i < 3 and 0 <= new_j < 3:
#                 new_state = [list(row) for row in state]
#                 new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
#                 neighbors.append(tuple(map(tuple, new_state)))

#         return neighbors

#     @staticmethod
#     def heuristic(state, goal_state):
#         # Manhattan distance heuristic
#         distance = 0
#         for i in range(3):
#             for j in range(3):
#                 if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
#                     tile = state[i][j]
#                     target_x, target_y = None, None
#                     for tx in range(3):
#                         for ty in range(3):
#                             if goal_state[tx][ty] == tile:
#                                 target_x, target_y = tx, ty
#                     distance += abs(target_x - i) + abs(target_y - j)
#         return distance

import random
from collections import deque
class HillClimbingSolver:

    @staticmethod
    def solve_puzzle(initial_state, goal_state, max_restarts=1):
        for restart in range(max_restarts):
            result, iteration = HillClimbingSolver.hill_climb(initial_state, goal_state)
            if result:
                print(f"Solution found after {iteration} iterations.")
                return result, iteration
            initial_state = HillClimbingSolver.random_state()
            print(f"Restarting... {restart + 1}/{max_restarts}")
        print("No solution found after maximum restarts.")
        return None, iteration

    @staticmethod
    
    def hill_climb(initial_state, goal_state):
        iteration = 0
        current_state = initial_state
        open = deque()
        visited = set()

        # Vérifiez si l'état initial est déjà l'état objectif
        if current_state == goal_state:
            return [initial_state], iteration

        while True:
            iteration += 1
            visited.add(current_state)

            # Obtenez et triez les voisins par heuristique (ordre croissant)
            neighbors = HillClimbingSolver.get_neighbors(current_state)
            neighbors.sort(key=lambda state: HillClimbingSolver.heuristic(state, goal_state))
            print("Neighbors sorted in ascending order by heuristic:", neighbors)

            # Ajoutez les voisins triés à la deque open s'ils ne sont pas visités
            for neighbor in neighbors:
                if neighbor not in visited:
                    open.appendleft(neighbor)

            print("Open deque after adding neighbors:", open)

            # Vérifiez si open est vide, ce qui signifie qu'il n'y a plus d'états à explorer
            if not open:
                return None, iteration  # Échec : aucun voisin non visité

            # Sélectionnez le prochain état à partir de la deque open
            next_state = open.popleft()
            while next_state in visited:
                if not open:  # Si open est vide et tous les états sont visités, échec
                    return None, iteration
                next_state = open.popleft()

            print("Next state selected:", next_state)
            print("Open deque after selecting next state:", open)

            current_heuristic = HillClimbingSolver.heuristic(current_state, goal_state)
            next_heuristic = HillClimbingSolver.heuristic(next_state, goal_state)
            
            print(f"Iteration: {iteration}")
            print("Current State:")
            for row in current_state:
                print(row)
            print("Next State:")
            for row in next_state:
                print(row)
            print(f"Current Heuristic: {current_heuristic}")
            print(f"Next Heuristic: {next_heuristic}")
            print("-------------")

            if next_heuristic >= current_heuristic:
                return None, iteration  # Local minimum reached
            if next_state == goal_state:
                return [initial_state, next_state], iteration  # Solution found

            current_state = next_state
            
                

    @staticmethod
    def get_neighbors(state):
        neighbors = []
        empty_tile_i, empty_tile_j = None, None
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_tile_i, empty_tile_j = i, j

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [list(row) for row in state]
                new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
                neighbors.append(tuple(map(tuple, new_state)))

        return neighbors

    # @staticmethod
    # def heuristic(state, goal_state):
    #     distance = 0
    #     for i in range(3):
    #         for j in range(3):
    #             if state[i][j] != goal_state[i][j] and state[i][j] != 0:
    #                 target_x, target_y = None, None
    #                 for tx in range(3):
    #                     for ty in range(3):
    #                         if goal_state[tx][ty] == state[i][j]:
    #                             target_x, target_y = tx, ty
    #                 distance += abs(target_x - i) + abs(target_y - j)
    #     return distance
    @staticmethod
    def heuristic(state, goal_state):
        misplaced_tiles = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                    misplaced_tiles += 1
        return misplaced_tiles

    @staticmethod
    def random_state():
        state = list(range(9))
        while True:
            random.shuffle(state)
            new_state = tuple(tuple(state[i:i+3]) for i in range(0, 9, 3))
            if HillClimbingSolver.is_solvable(new_state):
                return new_state

    @staticmethod
    def is_solvable(state):
        # Convert 2D state to 1D list
        one_d_state = [tile for row in state for tile in row]
        inversions = 0
        for i in range(len(one_d_state)):
            for j in range(i + 1, len(one_d_state)):
                if one_d_state[i] != 0 and one_d_state[j] != 0 and one_d_state[i] > one_d_state[j]:
                    inversions += 1
        return inversions % 2 == 0
