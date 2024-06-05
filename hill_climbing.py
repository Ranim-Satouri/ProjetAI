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

        if current_state == goal_state:
            return [initial_state], iteration

        while True:
            iteration += 1
            visited.add(current_state)

            neighbors = HillClimbingSolver.get_neighbors(current_state)
            neighbors.sort(key=lambda state: HillClimbingSolver.heuristic(state, goal_state))
            print("Neighbors sorted in ascending order by heuristic:", neighbors)

            for neighbor in neighbors:
                if neighbor not in visited:
                    open.appendleft(neighbor)

            print("Open deque after adding neighbors:", open)

            if not open:
                return None, iteration  

            next_state = open.popleft()
            while next_state in visited:
                if not open:  
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
                return None, iteration
            if next_state == goal_state:
                return [initial_state, next_state], iteration  

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
        one_d_state = [tile for row in state for tile in row]
        inversions = 0
        for i in range(len(one_d_state)):
            for j in range(i + 1, len(one_d_state)):
                if one_d_state[i] != 0 and one_d_state[j] != 0 and one_d_state[i] > one_d_state[j]:
                    inversions += 1
        return inversions % 2 == 0
