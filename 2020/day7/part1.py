import time


def main():

    """
    split input by lines
    """

    with open("input", "r") as file:
        input = file.read().splitlines()

    """
    defining the function that directly searches within the input, every line,
    if the bag we get as argument is a substring of the right side of the line
    (the contained bags). if found, we add its container bag (left side of the line)
    to the set of "bags".
    """

    def find_which_bag_contains(this_bag):
        for line in input:
            current_bag, contained_bags = line.split(" bags contain ")
            if this_bag in contained_bags:
                all_bags_found.add(current_bag)
                new_bags_to_look_for.add(current_bag)

    """
    initializing the set that will collect our bags with the first bag of which we
    want to find its container bag: "shiny gold"
    """

    all_bags_found = {"shiny gold"}

    """
    initializing the set that we'll use to only store the recently found bags (we
    clear it out after every iteration), because using the previous set will make us
    search again for what has already been searched
    """

    new_bags_to_look_for = all_bags_found.copy()

    """
    inside this infinite loop:

    1. we save the length of the current set of bags (all the container bags we've found)
    to "current_bags_count", to compare it later with the length of the updated set
    (len(all_bags_found)), so that once the new set (all_bags_found) has the
    same length as the old set (current_bags_count), we get out of the loop.

    2. we copy the content of the (new_bags_to_look_for) set into a new set
    (new_bags_copy) so that we could clear it out before the for loop.

    3. inside the for loop that iterates over our new bags (copied set), for each bag
    in the set we call the function that loops through the input to find which bag
    contains it, and adds it to both (all_bags_found) and (new_bags_to_look_for).

    4. once out of the fort loop, we check if there were actually any new bags added to
    the original set (all_bags_found) by checking its length against its old length
    (current_bags_count), if they were the same, it means that we have found all the bags
    and get out of the infinite loop; else, we repeat.
    """

    while True:
        current_bags_count = len(all_bags_found)
        new_bags_copy = new_bags_to_look_for.copy()
        new_bags_to_look_for.clear()
        for new_bag in new_bags_copy:
            find_which_bag_contains(new_bag)
        if len(all_bags_found) == current_bags_count:
            break

    """
    after getting out of the infinite loop, a.k.a finding all the bags, we save the count
    in a new variable "bags_found_count" minus 1 (for the "shiny gold" with which we
    initialized the bags set at first).
    """

    bags_found_count = current_bags_count - 1
    print(f"Number of bags found: {bags_found_count}\nBags: {all_bags_found}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
