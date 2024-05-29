import heapq

class BFSSolver:
    @staticmethod
    def solve_puzzle(initial_state, goal_state):
        # Initialisation de la file de priorité (frontier)
        frontier = []
        heapq.heappush(frontier, (0, initial_state))
        # Dictionnaire pour stocker d'où vient chaque état
        came_from = {initial_state: None}
        # Compteur pour le nombre d'itérations
        iterations = 0

        # Boucle principale : continue tant que la file n'est pas vide
        while frontier:
            # Retirer l'état avec la plus petite priorité de la file
            _, current_state = heapq.heappop(frontier)
            # Incrémenter le compteur d'itérations
            iterations += 1

            # Vérifier si l'état actuel est l'état cible
            if current_state == goal_state:
                # Reconstituer le chemin vers l'état initial
                path = []
                while current_state in came_from:
                    path.insert(0, current_state)
                    current_state = came_from[current_state]
                return path, iterations

            # Générer les états voisins de l'état actuel
            for next_state in BFSSolver.get_neighbors(current_state):
                # Vérifier si le voisin n'a pas été visité
                if next_state not in came_from:
                    # Ajouter le voisin à la file avec sa priorité (heuristique)
                    heapq.heappush(frontier, (BFSSolver.heuristic(next_state, goal_state), next_state))
                    # Mettre à jour la relation 'came_from' pour le voisin
                    came_from[next_state] = current_state

        # Si la boucle se termine sans trouver de solution, retourner None pour le chemin
        return None, iterations

    @staticmethod
    def get_neighbors(state):
        # Méthode pour générer les états voisins d'un état donné
        neighbors = []
        empty_tile_i, empty_tile_j = None, None
        # Trouver la position de la case vide dans l'état
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    empty_tile_i, empty_tile_j = i, j

        # Générer les états voisins en déplaçant la case vide dans toutes les directions possibles
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_i, new_j = empty_tile_i + move[0], empty_tile_j + move[1]
            # Vérifier si le déplacement est valide (reste dans la grille)
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                # Créer un nouvel état en effectuant le déplacement
                new_state = [list(row) for row in state]
                new_state[empty_tile_i][empty_tile_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_tile_i][empty_tile_j]
                neighbors.append(tuple(map(tuple, new_state)))

        return neighbors

    @staticmethod
    def heuristic(state, goal_state):
        # Méthode pour calculer l'heuristique d'un état par rapport à l'état cible
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                    # Calcul de la distance de Manhattan pour chaque tuile
                    x, y = divmod(goal_state[i][j], 3)
                    distance += abs(x - i) + abs(y - j)
        return distance
