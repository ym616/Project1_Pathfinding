


#flint session: https://app.flintk12.com/classes/us-7415-g-adv-m-ef82a8/chats/ae8eb649-5a09-490e-aa56-b0a04cd763be
#i used flint to walk me through how a* searching algo works and to get me started on the basics of pygame cuz i never took into to game design unfortunately
#also used this video to help me with the python implementation of the A*. It gave me the idea of using priority queue so it will auto keep track of which node it should check next. the priority queue sorts all the nodes so the node with total lowest distance is always at front.
#https://www.youtube.com/watch?v=JtiK0DOeI4A
import pygame
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* searching algo")

# colors for the start end point and grid color
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
GREY = (128, 128, 128)


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.neighbors = []  # Added an empty list for neighbors (needed later)

    def reset(self):
        self.color = WHITE

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col


#new a* added w/o implementation uet. USED MANHATTAN DISTAnCE!!!

def heuristic(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    #
    open_set.put((0, count, start))

    # "storage" kinda as it keeps track of where it came from
    came_from = {}


    #g_score is shortest curr dist.
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic((start.row, start.col), (end.row, end.col))

    open_set_hash = {start}

    while not open_set.empty():

        current = open_set.get()[2]
        open_set_hash.remove(current)


        if current == end:
            return True


        for neighbor in current.neighbors:

            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic((neighbor.row, neighbor.col), (end.row, end.col))


                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)

    return False





def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None
    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.make_start()
                elif not end and node != start:
                    end = node
                    end.make_end()


            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

               #when user presses spacebar on keyboard itll start the run for a*.
                if event.key == pygame.K_SPACE and start and end:
                    pass

    pygame.quit()


if __name__ == "__main__":
    main(WIN, WIDTH)