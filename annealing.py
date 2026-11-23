import random
import math

def calculate_cost(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j]:
                conflicts += 1

            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def simulated_annealing():

    while True:

        board = [random.randint(0, 7) for _ in range(8)]

        T = 100
        cooling_rate = 0.99

        while T > 0.01:

            current_cost = calculate_cost(board)

            if current_cost == 0:
                return board

            new_board = board.copy()

            col = random.randint(0, 7)
            new_board[col] = random.randint(0, 7)

            new_cost = calculate_cost(new_board)

            delta = new_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / T):
                board = new_board

            T *= cooling_rate


solution = simulated_annealing()

print("Solution found:", solution)
print("Cost:", calculate_cost(solution))

print("\nChess Board:")

for row in range(8):
    for col in range(8):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
