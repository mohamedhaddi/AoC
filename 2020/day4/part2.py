with open("passports", "r") as file:
    input = file.read()

passports = list(
    map(lambda el: dict(s.split(":") for s in el.split()), input.split("\n\n"))
)
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = 0

for passport in passports:
    if len(set(passport.keys()) & set(required_fields)) == 7:

        byr, iyr, eyr, hgt, hcl, ecl, pid = (
            passport["byr"],
            passport["iyr"],
            passport["eyr"],
            passport["hgt"],
            passport["hcl"],
            passport["ecl"],
            passport["pid"],
        )
        hgt_number = int("".join(d for d in hgt if d.isdigit()))
        hcl_value_length = len(
            "".join(c for c in hcl[1:] if (c.isdigit() or c.isalpha()))
        )
        required_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        if (
            len(byr) == 4
            and 1920 <= int(byr) <= 2002
            and len(iyr) == 4
            and 2010 <= int(iyr) <= 2020
            and len(eyr) == 4
            and 2020 <= int(eyr) <= 2030
            and (
                (hgt[-2:] == "cm" and 150 <= hgt_number <= 193)
                or (hgt[-2:] == "in" and 59 <= hgt_number <= 76)
            )
            and (hcl[0] == "#" and hcl_value_length == 6)
            and ecl in required_ecl
            and (len(pid) == 9 and pid.isdigit())
        ):

            valid_passports += 1

print(valid_passports)
