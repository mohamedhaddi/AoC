with open("input", "r") as file:
    instructions = file.read().splitlines()

been_here = []
acc, index = 0, 0
length = len(instructions)

while index < length:

    if index in been_here:
        break

    been_here.append(index)
    operation, argument = instructions[index].split(" ")

    if operation == "nop":
        index += 1

    elif operation == "acc":
        acc += int(argument)
        index += 1

    elif operation == "jmp":
        index += int(argument)

print(acc)
