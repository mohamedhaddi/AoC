import pprint
import functools

with open("test-input", "r") as file:
    input = list(map(lambda x: x.splitlines(), file.read().split("\n\n")))


def split_ranges(x):
    return list(map(lambda x: list(map(int, x.split("-"))), x.split(" ")[1::2]))


def split_tickets(x):
    return list(map(int, x.split(",")))


input = {
    "fields": list(map(split_ranges, input[0])),
    "my-ticket": split_tickets(input[1][1]),
    "nearby-tickets": list(map(split_tickets, input[2][1:])),
}


def val_not_in_ranges(x):
    for field in input["fields"]:
        for range in field:
            min, max = range[0], range[1]
            if not min <= x < -max:
                return x
    return 0


error_rate = 0
for ticket in input["nearby-tickets"]:
    error_rate += functools.reduce(lambda acc, x: acc + val_not_in_ranges(x), ticket)

print(error_rate)
# pprint.pprint(input)
