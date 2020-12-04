with open("passwords", "r") as file:
    input = file.read().splitlines()

length = len(input)
valid_passwords_count = 0

for i in range(length):
    policy, password = input[i].split(":")
    positions, character = policy.split(" ")
    pos_1, pos_2 = list(map(int, positions.split("-")))

    if (password[pos_1] == character) ^ (password[pos_2] == character):
        valid_passwords_count += 1

print(valid_passwords_count)
