import itertools

with open("input", "r") as file:
    input = file.read().splitlines()

mem = {}
curr_mask, curr_value, new_address = 0, 0, []

for line in input:

    words = line.split()
    words.remove("=")

    if words[0] == "mask":
        curr_mask = words[1]
    else:
        curr_value = format(
            int("".join(char for char in words[0] if char.isdigit())), "036b"
        )
        floating_indexes, index = [], 0
        new_address.clear()
        for char, bit in zip(curr_mask, curr_value):
            if char == "0":
                new_address.append(bit)
            elif char == "1":
                new_address.append(char)
            else:
                new_address.append(char)
                floating_indexes.append(index)
            index += 1
        combinations = list(itertools.product([0, 1], repeat=len(floating_indexes)))
        for combination in combinations:
            i = 0
            for index in floating_indexes:
                new_address[index] = str(combination[i])
                i += 1
            address = "".join(new_address)
            mem[address] = int(words[1])

print(sum(mem.values()))
