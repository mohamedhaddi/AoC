import time
import re


def main():

    """
    split input by lines
    """
    with open("input", "r") as file:
        input = file.read().splitlines()

    """
    defining the function that searches for each item in the dictionary, which container
    bag (key) contains within its value (list of contained bags) the bag we get as
    argument, then recursively finds which bag contains the container bag we found,
    until the container bag is, again: "shiny gold" itself.
    """

    def find_which_bag_contains(this_bag):
        for container_bag, contained_bags in bags_dict.items():
            if this_bag in contained_bags:
                if container_bag == "shiny gold":
                    return
                bags_found.add(container_bag)
                find_which_bag_contains(container_bag)

    bags_dict = {}
    bags_found = set()

    """
    splitting the input into a dictinary of key: value
    where key is the container bag, and value is its contained bags
    """
    for line in input:
        key, value = line.split(" bags contain ")
        value = value.replace("bag.", "").replace("bags.", "")
        value = list(
            map(
                lambda el: re.sub("\d", "", el).strip(),
                re.split(" bags, | bag, ", value),
            )
        )
        bags_dict[key] = value

    """
    start looking for container bags recursively,
    starting from the lowest bag: "shiny gold"
    """
    find_which_bag_contains("shiny gold")

    """
    print the result
    """
    print(f"Number of bags found: {len(bags_found)}\nBags: {bags_found}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
