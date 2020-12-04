with open("expense-report", "r") as file:
    input = list(map(int, file.read().split()))

length = range(len(input))
my_set = set()


def search(n):
    for i in length:
        lookup_value = n - input[i]
        if lookup_value not in my_set:
            my_set.add(input[i])
        else:
            return lookup_value * input[i]


for i in length:
    rs = search(2020 - input[i])
    if rs:
        print(input[i] * rs)
        break
