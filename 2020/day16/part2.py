from collections import OrderedDict

with open("input", "r") as file:
    og_input = list(map(lambda x: x.splitlines(), file.read().split("\n\n")))


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
    for field in input["fields"]:
        for range in field:
            min, max = range[0], range[1]
            if min <= x <= max:
                return True
    return False


def remove_invalid_tickets(x):
    temp_list = x[:]
    for ticket in x:
        for val in ticket:
            if is_in_ranges(val) == False:
                temp_list.remove(ticket)
                break
    return temp_list


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


input = og_input

# split input
input = {
    "fields": list(map(split_ranges, input[0])),
    "my-ticket": split_tickets(input[1][1]),
    "nearby-tickets": list(map(split_tickets, input[2][1:])),
}

# ignore invalid tickets
all_valid_tickets = remove_invalid_tickets(input["nearby-tickets"]) + [
    input["my-ticket"]
]

# get how many fields we have in our input
number_of_fields = len(input["fields"])

# initialize dictionary that will store everything
fields_positions = {}

# initialize set of all fields (their indexes in the input)
fields = set(range(number_of_fields))

# store every position in a ticket against its possible fields (their indexes in the input)
for pos in range(number_of_fields):

    # initialize set where we'll add all fields did not match a certain position
    blacklist = set()

    # getting a list for all numbers of the current position
    position_numbers = [ticket[pos] for ticket in all_valid_tickets]

    # checking which fields every number in position do not exist in
    for number in position_numbers:

        # add field to blacklist
        blacklist |= not_in_fields(number)

    # after iterating through all numbers of current position
    # we add to the dictionary the new position againt its possible fields
    # (which we get by substrating the blacklist from all fields)
    fields_positions[pos] = fields - blacklist

# order all positions by length of possible fields in ascending order
fields_positions = OrderedDict(
    sorted(fields_positions.items(), key=lambda i: len(i[1]))
)

# initialize indexed which will store the new results of
# positions and their possible fields in as list of lists
indexed, i = [], 0

# from the current set of possible fields, substract all previous
# possible fields (union of all the past sets of possible fields)
for pos in list(fields_positions.keys()):
    if i > 0:
        fields_positions[pos] = fields_positions[pos] - set.union(
            *[val[1] for val in indexed[:i]]
        )
    # also add the new values to indexed
    indexed.append([pos, fields_positions[pos]])
    i += 1

# collect all fields that start with the word "departure" in list: departure_fields
count = 0
departure_fields = []
for i, field in enumerate(og_input[0]):
    if field.split()[0] == "departure":
        departure_fields.append(i)
    count += 1
    if count == 6:
        break

# loop through all fields, check if their "possible field position" value matches
# one of the "departure" fields, if so, multiply it with other matched values
count = 0
product = 1
for i in range(number_of_fields):
    if next(iter(indexed[i][1])) in departure_fields:
        product *= input["my-ticket"][indexed[i][0]]
        count += 1
        if count == 6:
            break

# thanks for reading through my messy code, my sincere apologies
print(product)
