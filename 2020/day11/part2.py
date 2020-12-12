with open("input", "r") as file:
    input = file.read().splitlines()


def seat_checker(tmp, result, seat):

    # find the first seats in all directions around this seat

    indices = [i for i, c in enumerate(tmp) if c == seat]

    for i in indices:
        first_seats_in_all_directions = ""

        lines_above = i // h_length
        lines_under = (full_length - i) // h_length
        left_columns = i - lines_above * h_length
        right_columns = h_length - left_columns - 1

        # top left direction
        if i % h_length != 0 and i >= h_length:
            for j in range(1, lines_above + 1):
                top_left = i - ((h_length + 1) * j)
                if 0 <= top_left < full_length and tmp[top_left] in "L#":
                    first_seats_in_all_directions += tmp[top_left]
                    break  # break after finding first seat in direction
                if top_left % h_length == 0:
                    break

        # top direction
        if i >= h_length:
            for j in range(1, lines_above + 1):
                top = i - (h_length * j)
                if 0 <= top < full_length and tmp[top] in "L#":
                    first_seats_in_all_directions += tmp[top]
                    break

        # top right direction
        if (i + 1) % h_length != 0 and i >= h_length:
            for j in range(1, lines_above + 1):
                top_right = i - ((h_length - 1) * j)
                if 0 <= top_right < full_length and tmp[top_right] in "L#":
                    first_seats_in_all_directions += tmp[top_right]
                    break
                if (top_right + 1) % h_length == 0:
                    break

        # left direction
        if i % h_length != 0:
            for j in range(1, left_columns + 1):
                left = i - (1 * j)
                if 0 <= left < full_length and tmp[left] in "L#":
                    first_seats_in_all_directions += tmp[left]
                    break

        # right direction
        if (i + 1) % h_length != 0:
            for j in range(1, right_columns + 1):
                right = i + (1 * j)
                if 0 <= right < full_length and tmp[right] in "L#":
                    first_seats_in_all_directions += tmp[right]
                    break

        # bottom left direction
        if i % h_length != 0 and i < full_length - h_length:
            for j in range(1, lines_under + 1):
                bottom_left = i + ((h_length - 1) * j)
                if 0 <= bottom_left < full_length and tmp[bottom_left] in "L#":
                    first_seats_in_all_directions += tmp[bottom_left]
                    break
                if bottom_left % h_length == 0:
                    break

        # bottom direction
        if i < full_length - h_length:
            for j in range(1, lines_under + 1):
                bottom = i + (h_length * j)
                if 0 <= bottom < full_length and tmp[bottom] in "L#":
                    first_seats_in_all_directions += tmp[bottom]
                    break

        # bottom right direction
        if (i + 1) % h_length != 0 and i < full_length - h_length:
            for j in range(1, lines_under + 1):
                bottom_right = i + ((h_length + 1) * j)
                if 0 <= bottom_right < full_length and tmp[bottom_right] in "L#":
                    first_seats_in_all_directions += tmp[bottom_right]
                    break
                if (bottom_right + 1) % h_length == 0:
                    break

        # change state of seat if it meets rules
        if seat == "#":
            if first_seats_in_all_directions.count("#") >= 5:
                result[i] = "L"
        else:
            if first_seats_in_all_directions.count("#") == 0:
                result[i] = "#"

    return result


h_length = len(input[0])
result = list("".join(input))
full_length = len(result)

while True:
    tmp = result[:]

    # check if empty seat can be occupied
    result = seat_checker(tmp, result, "L")

    # check it occupied seat can be emptied
    result = seat_checker(tmp, result, "#")

    if result == tmp:
        break

print(str(result).count("#"))
