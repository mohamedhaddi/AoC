with open("map", "r") as file:
    input = file.read().splitlines()

v_length, h_length = len(input), len(input[0])
column, count_trees = 0, 0

for row in range(1, v_length):
    column += 3
    if column >= h_length - 1:
        column = column - h_length
    if input[row][column] == "#":
        count_trees += 1

print(count_trees)
