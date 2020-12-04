with open("expense-report", "r") as file:
    input = list(map(int, file.read().split()))

my_dict = {key: value for value, key in enumerate(input)}
length = range(len(input))

for i in length:

    value = input[i]
    lookup_value = 2020 - input[i]
    index = my_dict.get(lookup_value)

    if index:

        print(input[i] * input[index])
        break
