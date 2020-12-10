with open("input", "r") as file:
    input = list(map(int, file.read().splitlines()))

input.append(0)
input = sorted(input)
input.append(input[-1] + 3)
print(input)

one_jolt_diffs, three_jolt_diffs = 0, 0

for i in range(1, len(input)):

    diff = input[i] - input[i - 1]

    if diff == 1:
        one_jolt_diffs += 1
    elif diff == 3:
        three_jolt_diffs += 1
    else:
        break

print(one_jolt_diffs * three_jolt_diffs)
