import pprint

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


def remove_invalid_tickets(x):
    temp_list = x
    for ticket in x:
        for val in ticket:
            if not is_in_ranges(val):
                temp_list.remove(ticket)
                break
    return temp_list


input = {
    "fields": list(map(split_ranges, input[0])),
    "my-ticket": split_tickets(input[1][1]),
    "nearby-tickets": list(map(split_tickets, input[2][1:])),
}
input["nearby-ticket"] = remove_invalid_tickets(input["nearby-tickets"])

all_valid_tickets = input["nearby-ticket"] + [input["my-ticket"]]
number_of_fields = len(input["fields"])
fields_positions = []


def not_in_fields(x):
    fields, count = set(), 0
    ccc = 0
    for i, field in enumerate(input["fields"]):
        count = 0
        for range in field:
            min, max = range[0], range[1]
            if not min <= x <= max:
                count += 1
                if count == 2:
                    fields.add(i)
                    ccc += 1
        if ccc == 19:
            print(x)
    return fields


"""
def in_fields(x):
    fields = set()
    for i, field in enumerate(input["fields"]):
        for range in field:
            min, max = range[0], range[1]
            if min <= x <= max:
                fields.add(i)
    return fields
"""


for pos in range(number_of_fields):
    blacklist = set()
    fields = set()
    pos_numbers = [ticket[pos] for ticket in all_valid_tickets]
    for number in pos_numbers:
        blacklist |= not_in_fields(number)
        # fields |= in_fields(number)
    fields = set(range(number_of_fields))
    """
    print(pos)
    print(blacklist)
    print(fields)
    print()
    """
    fields_positions.append(fields - blacklist)
    """
    if pos > 0:
        fields_positions[pos] = fields_positions[pos] - set.union(
            *fields_positions[:pos]
        )
    """

# for i in reversed(range(1, number_of_fields)):
# fields_positions[i] = fields_positions[i] - fields_positions[i - 1]


# pprint.pprint(fields_positions)
