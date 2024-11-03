from collections import deque

def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):

    def replace_at_index(s: str, r: str, idx: int) -> str:
        return s[:idx] + r + s[idx + len(r):]

    n_columns = len(lab[0])
    numbers = " " + "".join([str(i % 10) for i in range(n_columns)])

    print(numbers)
    for i, row in enumerate(lab):
        if path:
            for item in path:
                if item[0] == i:
                    row = replace_at_index(row, "X", item[1])

        print(f"{i %10}{row}{i % 10}")

    print(numbers)

def prompt_integer(message: str) -> int:
    text = input(message)

    while not text.isdigit():
        print("Only integers accepted!")
        text = input(message)

    return int(text)

def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer(f"Row of {name} location: ")
    column = prompt_integer(f"Column of {name} location: ")
    return row, column

# Function for checking the traversability in lab
def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    if lab[location[0]][location[1]] == "█":
        return False
    return True

# BFS function to traverse a graph
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> None:
    # ... your implementation here...
    q = deque()
    q.append([start])
    visited = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if is_traversable(lab, start) == False:
        return print("Choose other starting end ending points.")
    while len(q) != 0:
        path = q.popleft()
        last = path[-1]
        if last == end:
            return path
        if last not in visited:
            visited.add(last)
            for move in moves:
                next = (last[0] + move[0], last[1] + move[1])
                if is_traversable(lab, next) == True:
                    q.append(path+[next])

# Labyrinth represented as a list of strings
labyrinth = [
    "█████████████",
    "█           █",
    "█ █████ █████",
    "█ █   █     █",
    "█ ███ █ █████",
    "█     █     █",
    "█████████████"
]

print_labyrinth(labyrinth)

start_location = prompt_user_for_location("start")
end_location = prompt_user_for_location("end")

# Find path using breadth-first search between start and end locations
path = bfs(labyrinth, start_location, end_location)

print_labyrinth(labyrinth, path)

# #checking if function "is_traversable" works
#print(is_traversable(labyrinth, (0,0)))
#print(is_traversable(labyrinth, (1,1)))
