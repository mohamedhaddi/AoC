input = [9, 6, 0, 10, 18, 2, 1]

for turns in range(len(input), 2020):
    input.append(
        0 if input.count(input[-1]) == 1 else input[-2::-1].index(input[-1]) + 1
    )

print(input[-1])
