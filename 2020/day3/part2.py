with open("map", "r") as file:
    input = file.read().splitlines()


def solve(steps, jumps):
    v_length, h_length = len(input), len(input[0])
    column, count_trees = 0, 0

    for row in range(jumps, v_length, jumps):
        column += steps
        if column >= h_length - 1:
            column = column - h_length
        if input[row][column] == "#":
            count_trees += 1

    return count_trees


print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
