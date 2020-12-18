with open("input", "r") as file:
    input = file.read().splitlines()

mem = {}
curr_mask, curr_value = 0, 0

for line in input:

    words = line.split()
    words.remove("=")

    if words[0] == "mask":
        curr_mask = words[1]
    else:
        curr_value = format(int(words[1]), "036b")
        new_value = "".join(
            [
                bit if char.isalpha() else char
                for char, bit in zip(curr_mask, curr_value)
            ]
        )
        exec("%s = %d" % (words[0], int(new_value, 2)))

print(sum(mem.values()))
print(mem)
