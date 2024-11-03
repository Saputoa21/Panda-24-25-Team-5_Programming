# Python Recap Exercise 2

# lab: list of strings that represent a row in a labyrinth; path: list of tuples containing 2 integers that represent coordinates of the path (row & column)
from collections import deque

def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None): # None is the default value: if we don't give the function a path
    # function to replace a specific character in the original string s with another string r at index idx
    def replace_at_index(s: str, r: str, idx: int) -> str:
        return s[:idx] + r + s[idx + len(r):]

    # stores the number of columns since each character in the string represents a column
    n_columns = len(lab[0])
    # creates a string of numbers to indicate the column indices; 'str(i % 10)' -> so that numbers loop from 0-9
    numbers = " " + "".join([str(i % 10) for i in range(n_columns)])

    print(numbers) # print column numbers
    for i, row in enumerate(lab): # iterate through each row of the labyrinth
        if path:
            # check if path coordinates match index
            # If they match the current row, the corresponding column is replaced with 'X'
            for item in path:
                if item[0] == i:
                    row = replace_at_index(row, "X", item[1])

        print(f"{i %10}{row}{i % 10}") # print each row with numbers on the side

    print(numbers) # print numbers again to complete the grid

    # function that asks user for input
def prompt_integer(message: str) -> int:
    text = input(message)

    # if input is not a digit, the functions asks for valid input
    while not text.isdigit():
        print("Only integers accepted!")
        text = input(message)

    return int(text) # convert input to an integer

# prompt user to input the row and column
def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer(f"Row of {name} location: ")
    column = prompt_integer(f"Column of {name} location: ")
    return row, column # if you return comma separated values, you automatically get a tuple


def is_traversable(lab: list[str], location: tuple[int, int]) -> bool:
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[0]):
        return lab[row][col] == " "  # A space means traversable
    return False


# BFS function to find the shortest path
def bfs(lab: list[str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = deque([[start]])  # Queue holds all paths considered so far
    visited_locations = set()  # Visited set to track visited positions

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible moves: down, up, right, left

    while queue:
        path = queue.popleft()  # Dequeue the first path
        last = path[-1]  # Get the last position in the path

        if last == end:  # If last position is the end, return the path
            return path

        if last not in visited_locations:  # If the last position hasn't been visited
            visited_locations.add(last)  # Mark it as visited

            for move in moves:  # Explore all possible moves
                next_pos = last[0] + move[0], last[1] + move[1]

                # Use the is_traversable function to check if the next position is walkable
                if is_traversable(lab, next_pos):
                    queue.append(path + [next_pos])   # Enqueue the new path

    return []  # If no path is found, return an empty list


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
