with open("passwords", "r") as file:
    input = file.read().splitlines()

length = len(input)
valid_passwords_count = 0

for i in range(length):
    policy, password = input[i].split(":")
    occurence, character = policy.split(" ")
    min_occ, max_occ = list(map(int, occurence.split("-")))

    if min_occ <= password.count(character) <= max_occ:
        valid_passwords_count += 1

print(valid_passwords_count)
