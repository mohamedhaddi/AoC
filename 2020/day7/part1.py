import time


def main():
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
                bags.add(current_bag)

    """
    initializing the "bags" set with the first bag of which we want to find the
    the container bags: "shiny gold"
    """
    bags = {"shiny gold"}

    """
    """
    bags_count = len(bags)

    """
    inside this infinite loop, we copy the current set (bags) into a new set
    (current_bags) so that we can loop through it (otherwise we wouldn't be able to,
    as we're dynamically modifying the original set when we call the function inside
    the for loop).

    then we save the amount of the current bags into "bags_count", to compare it later
    with the length of the updated set (len(bags)), so that once the new set (bags) has
    the same length as the old set (current_bags), we get out of the loop.

    inside the for loop that iterates over our current bags (copied set), for each bag
    in the set we call the function that loops thought the input to find which bag
    contains it, and adds it to the set; once we do this for all the bags in our current
    bags (copied set), we check if there were actually any new bags added to the original
    set by checking its length against the copied set's length, if they were the same, it
    means that we have found all the bags and get out of the infinite loop; else, we
    update the current bags and the current length, and repeat.
    """
    while True:
        current_bags = bags.copy()
        bags_count = len(current_bags)
        for bag in current_bags:
            find_which_bag_contains(bag)
        if len(bags) == bags_count:
            break

    """
    after getting out of the infinite loop, a.k.a finding all the bags, we add the count
    to "bags_found" minus 1 (for the "shiny gold" with which we initialized the bags set).
    """
    bags_found = bags_count - 1
    print(f"Number of bags found: {bags_found}\nBags: {bags}")


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
