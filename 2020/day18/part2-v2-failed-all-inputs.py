with open("test-input", "r") as file:
    og_input = file.read().splitlines()

og_input = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

input = []
for line in og_input:
    temp_list = list(line)
    i = 0
    count = 0
    while i < len(line):
        if line[i] == "+":
            count += 1
        i += 1
    parantheses = count * 2
    i = 0
    while i < len(line) + parantheses - 3:
        line_list = temp_list[:]
        if line_list[i + 2] == "+":
            if line_list[i].isdigit():
                temp_list.insert(i, "(")
                if line_list[i + 4] == "(":
                    j = i + 4
                    while j < len(line_list):
                        if line_list[j] == ")":
                            temp_list.insert(j, ")")
                            break
                        j += 1
                elif line_list[i + 4].isdigit():
                    temp_list.insert(i + 6, ")")
            elif line_list[i] == ")":
                j = i
                count = 0
                while line_list[j] != "(":
                    if line_list[j] == ")":
                        count += 1
                    j -= 1
                j = i
                while j >= 0:
                    if line_list[j] == "(":
                        count -= 1
                        if count == 0:
                            temp_list.insert(j, "(")
                            break
                    j -= 1
                if line_list[i + 4] == "(":
                    j = i + 4
                    while j < len(line_list):
                        if line_list[j] == ")":
                            temp_list.insert(j, ")")
                            break
                        j += 1
                elif line_list[i + 4].isdigit():
                    temp_list.insert(i + 6, ")")
            i += 1
        i += 1
    input.append("".join(temp_list))

print(og_input)
print(input)


"""
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
"""
