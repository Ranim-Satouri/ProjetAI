# import heapq

# class BFSSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
#         open_set = [(0 + BFSSolver.manhattan_distance(initial_state, goal_state), 0, initial_state)]
#         closed_set = set()
#         iterations = 0
#         while open_set:
#             _, depth, state = heapq.heappop(open_set)
#             if state == goal_state:
#                 return BFSSolver.reconstruct_path(state), iterations
#             if state in closed_set:
#                 continue
#             closed_set.add(state)
#             successors = BFSSolver.generate_successors(state)
#             print("successors",successors)
#             for successor in successors:
#                 h = BFSSolver.manhattan_distance(successor, goal_state)
#                 if successor in closed_set:
#                     continue
#                 if successor not in open_set:
#                     heapq.heappush(open_set, (depth + h, depth + 1, successor))
#                 elif successor in open_set:
#                     idx = open_set.index(successor)
#                     if open_set[idx][0] > depth + h:
#                         open_set[idx] = (depth + h, depth + 1, successor)
#             heapq.heapify(open_set)
#             iterations += 1
#             print(open_set)
#             print(closed_set)
#         return None, iterations

#     @staticmethod
#     def generate_successors(state):
#         successors = []
#         for i in range(len(state)):
#             for j in range(len(state[0])):
#                 if state[i][j] == 0:
#                     for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                         new_i, new_j = i + dx, j + dy
#                         if 0 <= new_i < len(state) and 0 <= new_j < len(state[0]):
#                             new_state = list(map(list, state))
#                             new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
#                             successors.append(tuple(map(tuple, new_state)))
#         return successors

#     @staticmethod
#     def manhattan_distance(state, goal_state):
#         distance = 0
#         for i in range(len(state)):
#             for j in range(len(state[0])):
#                 if state[i][j] != 0:
#                     value = state[i][j]
#                     goal_i, goal_j = divmod(value - 1, len(state[0]))
#                     distance += abs(i - goal_i) + abs(j - goal_j)
#         return distance

#     @staticmethod
#     def reconstruct_path(state):
#         path = [state]
#         while state.get('parent'):
#             state = state.get('parent')
#             path.append(state)
#         return path[::-1]



# from queue import PriorityQueue

# class BFSSolver:
#     @staticmethod
#     def solve_puzzle(initial_state, goal_state):
        
#         frontier = PriorityQueue()
#         frontier.put((0, initial_state))
#         came_from = {initial_state: None}
#         iterations = 0

#         while not frontier.empty():
#             _, current_state = frontier.get()
#             iterations+=1
#             if current_state == goal_state:
#                 # Reconstruct path
#                 path = []
#                 while current_state in came_from:
#                     path.insert(0, current_state)
#                     current_state = came_from[current_state]
#                 return path,  iterations

#             for next_state in BFSSolver.get_neighbors(current_state):
#                 if next_state not in came_from:
#                     frontier.put((BFSSolver.heuristic(next_state, goal_state), next_state))
#                     came_from[next_state] = current_state
#             print("frontier ",frontier.queue)
            

#         return None , iterations

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
#                     x, y = divmod(goal_state[i][j], 3)
#                     distance += abs(x - i) + abs(y - j)
#         return distance


import heapq

class BFSSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state):
        
        frontier = []
        heapq.heappush(frontier, (0, initial_state))
        came_from = {initial_state: None}
        iterations = 0

        while frontier:
            _, current_state = heapq.heappop(frontier)
            iterations+=1
            if current_state == goal_state:
                # Reconstruct path
                path = []
                while current_state in came_from:
                    path.insert(0, current_state)
                    current_state = came_from[current_state]
                return path,  iterations

            for next_state in BFSSolver.get_neighbors(current_state):
                if next_state not in came_from:
                    heapq.heappush(frontier, (BFSSolver.heuristic(next_state, goal_state), next_state))
                    came_from[next_state] = current_state
            # print("frontier ",frontier)
            

        return None , iterations

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
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                    x, y = divmod(goal_state[i][j], 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
