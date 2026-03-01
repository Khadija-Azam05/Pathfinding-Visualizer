import tkinter as tk
import heapq
import random
import time
import math

# basic settings
ROWS = 10
COLS = 10
SIZE = 40

grid = []
start = None
goal = None

visited = set()
frontier = set()
path = []

dynamic = False
agent = None


# create grid
def make_grid():
    global grid
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]


# draw grid
def draw():
    canvas.delete("all")

    for r in range(ROWS):
        for c in range(COLS):

            x1 = c * SIZE
            y1 = r * SIZE
            x2 = x1 + SIZE
            y2 = y1 + SIZE

            color = "white"

            if grid[r][c] == 1:
                color = "black"
            if (r, c) in frontier:
                color = "yellow"
            if (r, c) in visited:
                color = "lightblue"
            if (r, c) in path:
                color = "green"
            if (r, c) == start:
                color = "pink"
            if (r, c) == goal:
                color = "red"

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")


# heuristics
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


# search
def search():
    global visited, frontier, path

    if start is None or goal is None:
        return

    visited = set()
    frontier = set()
    path = []

    algo = algo_var.get()
    heur = heur_var.get()

    h = manhattan if heur == "manhattan"else euclidean

    pq = []
    heapq.heappush(pq, (0, start))

    parent = {}
    g = {start: 0}

    t1 = time.time()

    while pq:
        f, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            node = current
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            break

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = current[0] + dr
            nc = current[1] + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] != 1:

                nxt = (nr, nc)
                new_g = g[current] + 1

                if nxt not in g or new_g < g[nxt]:
                    g[nxt] = new_g
                    parent[nxt] = current

                    if algo == "gbfs":
                        f_val = h(nxt, goal)
                    else:
                        f_val = new_g + h(nxt, goal)

                    heapq.heappush(pq, (f_val, nxt))
                    frontier.add(nxt)

    t2 = time.time()

    visited_label.config(text=str(len(visited)))
    cost_label.config(text=str(len(path)))
    time_label.config(text=str(round((t2 - t1) * 1000, 2)))

    draw()


# dynamic mode
def start_dynamic():
    global dynamic, agent

    if start is None or goal is None:
        return

    dynamic = True
    search()

    if not path:
        return

    agent = start
    move()


def move():
    global agent, path

    if not dynamic:
        return

    # random obstacle
    if random.random() < 0.05:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        if grid[r][c] == 0 and (r, c) != start and (r, c) != goal:
            grid[r][c] = 1

    # replan if blocked
    if len(path) > 1:
        nxt = path[1]
        if grid[nxt[0]][nxt[1]] == 1:
            search()

    # move agent
    if len(path) > 1:
        agent = path[1]
        path.pop(0)

    draw()
    root.after(500, move)


# mouse click
def click(event):
    global start, goal

    c = event.x // SIZE
    r = event.y // SIZE

    if mode_var.get() == "start":
        start = (r, c)
    elif mode_var.get() == "goal":
        goal = (r, c)
    else:
        grid[r][c] = 1 if grid[r][c] == 0 else 0

    draw()


# GUI
root = tk.Tk()
root.title("Pathfinding")

canvas = tk.Canvas(root, width=COLS*SIZE, height=ROWS*SIZE)
canvas.pack()
canvas.bind("<Button-1>", click)

mode_var = tk.StringVar(value="wall")
tk.Radiobutton(root, text="Wall", variable=mode_var, value="wall").pack(side="left")
tk.Radiobutton(root, text="Start", variable=mode_var, value="start").pack(side="left")
tk.Radiobutton(root, text="Goal", variable=mode_var, value="goal").pack(side="left")

algo_var = tk.StringVar(value="astar")
tk.OptionMenu(root, algo_var, "astar", "gbfs").pack(side="left")

heur_var = tk.StringVar(value="manhattan")
tk.OptionMenu(root, heur_var, "manhattan", "euclidean").pack(side="left")

tk.Button(root, text="Search", command=search).pack(side="left")
tk.Button(root, text="Dynamic", command=start_dynamic).pack(side="left")

visited_label = tk.Label(root, text="0")
visited_label.pack(side="left")

cost_label = tk.Label(root, text="0")
cost_label.pack(side="left")

time_label = tk.Label(root, text="0")
time_label.pack(side="left")

make_grid()
draw()
root.mainloop()