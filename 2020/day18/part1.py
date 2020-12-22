with open("input", "r") as file:
    input = file.read().splitlines()


def calc(i, line, res, op):
    while i < len(line):
        char = line[i]
        if char.isdigit():
            if op == "+":
                res += int(char)
            elif op == "*":
                res *= int(char)
        elif char == "+":
            op = "+"
        elif char == "*":
            op = "*"
        elif char == "(":
            last_op = op
            op = "+"
            p_res = 0
            i, p_res, op = calc(i + 1, line, p_res, op)
            if last_op == "+":
                res += p_res
            elif last_op == "*":
                res *= p_res
        elif char == ")":
            break
        i += 1
    return i, res, op


summ = 0
for line in input:
    i, res, op = 0, 0, "+"
    i, res, op = calc(i, line, res, op)
    summ += res

print(summ)
