with open("input", "r") as file:
    instructions = file.read().splitlines()


def loop(jump_to_alter, nop_to_alter):

    index = 0
    global acc

    while index < length:

        if index in been_here:
            return False

        been_here.append(index)
        operation, argument = instructions[index].split(" ")

        if operation == "nop":
            been_to_these_nops.append(index)
            if index != nop_to_alter:
                index += 1
            else:
                index += int(argument)

        elif operation == "acc":
            acc += int(argument)
            index += 1

        elif operation == "jmp":
            been_to_these_jmps.append(index)
            if index != jump_to_alter:
                index += int(argument)
            else:
                index += 1

    return True


been_here = []
been_to_these_jmps = []
been_to_these_nops = []
length = len(instructions)
acc = 0

loop(None, None)

jmps_to_loop_through = been_to_these_jmps[:]
nops_to_loop_through = been_to_these_nops[:]

for jmp in jmps_to_loop_through:
    acc = 0
    been_here.clear()
    if loop(jmp, None):
        print(acc)

for nop in nops_to_loop_through:
    acc = 0
    been_here.clear()
    if loop(None, nop):
        print(acc)
