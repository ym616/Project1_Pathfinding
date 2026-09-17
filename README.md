project 1: a* pathfinding 

how to run and test:
pip install pygame
run main.py.
use left mouse click to place nodes. the first click sets the start node (orange). the second sets the end node (turquoise). any clicks after that draw barriers (black).
use right mouse click to erase anything.
hit spacebar to run the algorithm and watch it find the path.
hit 'c' to clear the grid and start over.

a* vs bfs vs dijkstra
bfs (breadth first search): explores equally in all directions in a circle. it finds the shortest path on unweighted grids, but it is slow because it checks everything blindly.
dijkstra's algorithm: an upgrade to bfs that factors in movement costs/weights to guarantee the shortest path, but it still searches outward in all directions blindly.
a* algorithm: takes dijkstra's and adds a heuristic (kinda like a smart guess) to estimate the distance to the goal. instead of exploring everywhere, it prioritizes nodes that look like they are heading directly toward the target. this makes it significantly faster and more efficient. this is similar to the algorithm used in pcb autorouting.

heuristic exploration
for this project, i chose the manhattan distance heuristic, which calculates distance by only allowing horizontal and vertical movements. the general formula is  abs(x1 - x2) + abs(y1 - y2).

i tested the idea of using euclidean distance (a straight line like sqrt(x^2 + y^2) ), but on a grid where it can only move 4 ways, euclidean distance actually underestimates the actual travel cost. this underestimation causes a* to lose confidence and check too many extra nodes. manhattan matches the actual grid constraints, balancing performance and speed while ensuring the shortest path.