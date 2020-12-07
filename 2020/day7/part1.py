with open("input", "r") as file:
    input = file.read().splitlines()


def find_which_bag_contains(this_bag):
    for line in input:
        current_bag, contained_bags = line.split(" bags contain ")
        if this_bag in contained_bags:
            bags.add(current_bag)


bags = set()

find_which_bag_contains("shiny gold")
bags_count = len(bags)

while True:
    current_bags = bags.copy()
    for bag in current_bags:
        find_which_bag_contains(bag)
    if len(bags) == bags_count:
        break
    else:
        bags_count = len(bags)

print(f"Number of bags found: {bags_count}\nBags: {bags}")
