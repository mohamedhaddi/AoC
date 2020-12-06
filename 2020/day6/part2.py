import functools

with open("answers", "r") as file:
    input = file.read().split("\n\n")

sum = 0
for group in input:
    persons = [x for x in group.split("\n") if x]
    common_answers = "".join(
        functools.reduce(lambda prsn, nxt_prsn: set(prsn) & set(nxt_prsn), persons)
    )
    sum += len(common_answers)

print(sum)
