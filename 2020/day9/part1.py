with open("input", "r") as file:
    input = list(map(lambda number: int(number), file.read().splitlines()))

pair_found = True
invalid_number = None
preamble = 25

for i in range(len(input)):

    j = i

    for j in range(i, i + preamble):

        pair_to_find = input[i + preamble] - input[j]

        if pair_to_find in input[i : i + (preamble - 1)] and pair_to_find != input[j]:

            pair_found = True
            break

        else:

            pair_found = False

    if not pair_found:

        invalid_number = input[i + preamble]
        break

print(invalid_number)
