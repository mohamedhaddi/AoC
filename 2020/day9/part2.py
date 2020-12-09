with open("input", "r") as file:
    input = list(map(lambda number: int(number), file.read().splitlines()))

### PART 1

pair_found = True
preamble = 25
invalid_number = 0

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

### PART 2: Used the sliding window technique

right_index = 1
sublist_found = [input[0], input[right_index]]
sublist_sum = 0

while True:

    sublist_sum = sum(sublist_found)

    if sublist_sum == invalid_number:

        break

    elif sublist_sum < invalid_number:

        right_index += 1
        sublist_found.append(input[right_index])

    elif sublist_sum > invalid_number:

        sublist_found.pop(0)

print(max(sublist_found) + min(sublist_found))
