with open("boarding-passes", "r") as file:
    input = file.read().splitlines()

    seat_ids = []


def search(str, min, mid, max, min_char, max_char):
    for character in str:
        if character == min_char:
            max = mid
            mid = min + int((max - min) / 2)
        elif character == max_char:
            min = mid + 1
            mid = min + int((max - min) / 2)
    return mid


for boarding_pass in input:
    # finding row
    min_front, mid, max_back = 0, 63, 127
    row = search(boarding_pass[:7], min_front, mid, max_back, "F", "B")

    # finding column
    min_left, mid, max_right = 0, 3, 7
    col = search(boarding_pass[-3:], min_left, mid, max_right, "L", "R")

    # calculating seat ID and adding it to a list of seat IDs
    seat_id = row * 8 + col
    seat_ids.append(seat_id)

    print(
        "Boarding pass:",
        boarding_pass[:7],
        "- Row:",
        row,
        "- Column:",
        col,
        "- Seat ID:",
        seat_id,
    )

print("Highest ID:", max(seat_ids))
