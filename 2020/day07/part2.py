import time
import re


def main():

    """
    split input by lines
    """

    with open("input", "r") as file:
        input = file.read().splitlines()

    """
    updating the same function used in part1-v2.py, except this time we give it as argument
    the container bag (key) to search for its contained bags (value), which in turn are recursively
    given to the function to search for as keys.
    
    when we find a container bag (key), we append all the numbers of its contained bags to
    the "count" list. once we find "shiny gold" as a value (contained bag) of a certain key bag,
    we return the count list to stop the recursion.
    """

    def find_which_bag_contains(this_bag, count):
        for container_bag, contained_bags in bags_dict.items():
            if this_bag == container_bag:
                if "shiny gold" in [el[1] for el in contained_bags]:
                    return count
                for el in contained_bags:
                    if el[0] != "no":
                        count.append(int(el[0]))
                bags_found.add(container_bag)
                for el in contained_bags:
                    if el[0] != "no":
                        for i in range(int(el[0])):
                            find_which_bag_contains(el[1], count)

    bags_dict = {}
    bags_found = set()
    count = []

    """
    splitting the input into a dictinary of key: value, where key is the container bag,
    and value is a list of contained bags (sublists), where each one has a number as a first item
    (how many bags), and the bag as second item.

    e.g.:
    {'shiny gold': [
        [2, 'dark red'],
        [4, 'vibrant plum'],
        [1, 'dark olive']
    ]}
    """

    for line in input:
        key, value = line.split(" bags contain ")
        value = value.replace("bag.", "").replace("bags.", "")
        value = list(
            map(
                lambda el: list(map(lambda el2: el2.strip(), el.split(" ", 1))),
                re.split(" bags, | bag, ", value),
            )
        )
        bags_dict[key] = value

    """
    start looking for bags contained by "shiny gold" recursively
    """

    find_which_bag_contains("shiny gold", count)

    """
    print the result
    """

    print("Shiny gold contains", sum(count), "other bags.")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
