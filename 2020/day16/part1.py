with open("input", "r") as file:
    input = list(map(lambda x: x.splitlines(), file.read().split("\n\n")))


def split_ranges(x):
    return list(
        map(
            lambda x: list(map(int, x.split("-"))),
            x.split(":")[1].split(" ")[1::2],
        )
    )


def split_tickets(x):
    return list(map(int, x.split(",")))


def is_in_ranges(x):
    valid = False
    for field in input["fields"]:
        for range in field:
            min, max = range[0], range[1]
            if min <= x <= max:
                valid = True
                break
    return valid


error_rate = 0
input = {
    "fields": list(map(split_ranges, input[0])),
    "my-ticket": split_tickets(input[1][1]),
    "nearby-tickets": list(map(split_tickets, input[2][1:])),
}


for ticket in input["nearby-tickets"]:
    for val in ticket:
        if not is_in_ranges(val):
            error_rate += val
            break

print(error_rate)
