with open("input", "r") as file:
    input = list(map(lambda number: int(number), file.read().splitlines()))

pair_found = True
invalid_number = None

for i, number in enumerate(input):
    j = i
    for j in range(i, i + 25):
        pair_to_find = input[i + 25] - input[j]
        if pair_to_find in input[i : i + 24] and pair_to_find != input[j]:
            pair_found = True
            break
        else:
            pair_found = False
    if not pair_found:
        invalid_number = input[i + 25]
        break

print(invalid_number)


