from collections import deque

# function to print the puzzle in 3x3 form
def show(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

# function to get next possible states by moving blank (0)
def get_next(state):
    blank = state.index(0)   # find position of empty space
    next_states = []

    # allowed swap positions for each index
    moves = {
        0: [1,3],
        1: [0,2,4],
        2: [1,5],
        3: [0,4,6],
        4: [1,3,5,7],
        5: [2,4,8],
        6: [3,7],
        7: [4,6,8],
        8: [5,7]
    }

    # swapping to generate new states
    for m in moves[blank]:
        new_state = state.copy()
        new_state[blank], new_state[m] = new_state[m], new_state[blank]
        next_states.append(new_state)

    return next_states

# BFS algorithm to find solution
def bfs(start, goal):
    q = deque()
    q.append(start)

    visited = set()
    visited.add(tuple(start))

    parent = {}   # to store path

    while q:
        curr = q.popleft()

        if curr == goal:
            return parent   # solution found

        for nxt in get_next(curr):
            t = tuple(nxt)
            if t not in visited:
                visited.add(t)
                parent[t] = curr
                q.append(nxt)

    return None


# function to print solution path
def print_path(start, goal, parent):
    path = []
    state = goal

    while state != start:
        path.append(state)
        state = parent[tuple(state)]
    path.append(start)

    path.reverse()

    print("Steps to solve the puzzle:\n")
    for p in path:
        show(p)


# --------------------------
#      MAIN PROGRAM
# --------------------------

start = [1,2,3,
         4,0,5,
         6,7,8]

goal  = [1,2,3,
         4,5,6,
         7,8,0]

print("Initial Puzzle:")
show(start)

result = bfs(start, goal)

if result:
    print_path(start, goal, result)
else:
    print("No solution exists.")
