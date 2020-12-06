with open("answers", "r") as file:
    input = file.read().split("\n\n")

sum = 0
for group in input:
    set_of_answers = set(group)
    length = len(set_of_answers)

    sum += length - 1 if "\n" in set_of_answers else length

print(sum)
