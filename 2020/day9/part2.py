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

left_index = 0
right_index = 1
sublist_sum = input[left_index] + input[right_index]

while True:

    if sublist_sum == invalid_number:

        sublist_found = input[left_index:right_index]
        break

    elif sublist_sum < invalid_number:

        right_index += 1
        sublist_sum += input[right_index]

    else:

        sublist_sum -= input[left_index]
        left_index += 1

print(max(sublist_found) + min(sublist_found))
