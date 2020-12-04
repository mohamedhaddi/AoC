with open("passports", "r") as file:
    input = file.read()

passports = list(
    map(
        lambda el: list(map(lambda info: info.split(":")[0], el.split())),
        input.split("\n\n"),
    )
)
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = 0

for passport in passports:
    if len(set(passport) & set(required_fields)) == 7:
        valid_passports += 1

print(valid_passports)
