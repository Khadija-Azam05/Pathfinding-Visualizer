# Pathfinding Visualizer (A* and GBFS)

This project is a Python-based Pathfinding Visualizer built using Tkinter.  
It demonstrates A* (A-Star) and Greedy Best-First Search (GBFS) algorithms 
with Manhattan and Euclidean heuristics.

---

## Features

- Grid-based environment (10x10)
- A* Search Algorithm
- Greedy Best-First Search (GBFS)
- Manhattan and Euclidean Heuristics
- Dynamic obstacle generation
- Real-time path re-planning
- Visual display of:
  - Visited nodes
  - Frontier nodes
  - Final path
  - Path cost
  - Execution time

---

## Technologies Used

- Python 3
- Tkinter (built-in GUI library)
- heapq
- math
- random
- time

---

## How to Run

### 1. Install Python
Make sure Python 3 is installed on your system.

Check version:
```
python --version
```

### 2. Clone Repository
```
git clone https://github.com/Khadija-Azam05/Pathfinding-Visualizer.git
```

### 3. Navigate to Project Folder
```
cd Pathfinding-Visualizer
```

### 4. Run the Program
```
python main.py
```

---

## Controls

- Left Click:
  - Select Wall mode → Create/remove obstacles
  - Select Start mode → Set start node
  - Select Goal mode → Set goal node
- Search → Run selected algorithm
- Dynamic → Enable dynamic obstacle mode

---

## Algorithms

### A* Search
Uses:
f(n) = g(n) + h(n)

Where:
- g(n) = cost from start to current node
- h(n) = heuristic (Manhattan or Euclidean)

### Greedy Best-First Search
Uses:
f(n) = h(n)

---

## Project Structure

```
main.py
README.md
```

---

## Author
Khadija Azam
