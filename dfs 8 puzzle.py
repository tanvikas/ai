START = [1, 2, 3, 4, 0, 6, 7, 5, 8]
GOAL  = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def show(s):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x) for x in s[i:i+3]))
    print()


def next_states(s):
    z = s.index(0)
    r, c = divmod(z, 3)

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            n = s[:]
            p = nr * 3 + nc
            n[z], n[p] = n[p], n[z]
            yield n


def dfs():
    stack = [(START, [START])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == GOAL:
            return path

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        for n in next_states(state):
            stack.append((n, path + [n]))


print("===== DFS =====")
print("INITIAL STATE:")
show(START)

print("GOAL STATE:")
show(GOAL)

path = dfs()

print("SOLUTION:")
for i, state in enumerate(path):
    print("Step", i)
    show(state)

print("Total moves:", len(path) - 1)

