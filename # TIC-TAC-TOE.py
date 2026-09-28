# TIC-TAC-TOE
# X = Human, O = Computer

b = [" "] * 9
wins = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def win(p):
    return any(b[a] == b[c] == b[d] == p for a,c,d in wins)

def full():
    return " " not in b

def mini(maximizing):
    if win("O"): return 1
    if win("X"): return -1
    if full(): return 0

    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if maximizing else "X"
            scores.append(mini(not maximizing))
            b[i] = " "

    return max(scores) if maximizing else min(scores)

def best_move():
    best, move = -2, 0

    for i in range(9):
        if b[i] == " ":
            b[i] = "O"
            score = mini(False)
            b[i] = " "

            if score > best:
                best, move = score, i

    return move

def show():
    print(f"{b[0]} | {b[1]} | {b[2]}")
    print("---------")
    print(f"{b[3]} | {b[4]} | {b[5]}")
    print("---------")
    print(f"{b[6]} | {b[7]} | {b[8]}")

print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")
show()

while True:

    # Human
    while True:
        try:
            p = int(input("Enter position (1-9): "))

            if not 1 <= p <= 9 or b[p-1] != " ":
                print("Invalid move. Try again.")
            else:
                b[p-1] = "X"
                break
        except:
            print("Invalid move. Try again.")

    show()

    if win("X"):
        print("You win!")
        break

    if full():
        print("Draw!")
        break

    # Computer
    p = best_move()
    b[p] = "O"

    print("Computer chose position:", p + 1)
    show()

    if win("O"):
        print("Computer wins!")
        break

    if full():
        print("Draw!")
        break