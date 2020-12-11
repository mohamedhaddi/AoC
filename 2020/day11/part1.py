with open("input", "r") as file:
    input = file.read().splitlines()


def seat_checker(tmp, result, seat):

    # find seat's adjacents seats

    indices = [i for i, c in enumerate(tmp) if c == seat]

    for i in indices:
        adjacents = ""

        # top left seat
        top_left = i - h_length - 1
        if top_left >= 0 and i % h_length != 0:
            adjacents += tmp[top_left]

        # top seat
        top = i - h_length
        if top >= 0 and i >= h_length:
            adjacents += tmp[top]

        # top right seat
        top_right = i - h_length + 1
        if top_right >= 0 and (i + 1) % h_length != 0:
            adjacents += tmp[top_right]

        # left seat
        left = i - 1
        if left >= 0 and i % h_length != 0:
            adjacents += tmp[left]

        # right seat
        right = i + 1
        if right < full_length and (i + 1) % h_length != 0:
            adjacents += tmp[right]

        # bottom left seat
        bottom_left = i + h_length - 1
        if bottom_left < full_length and i % h_length != 0:
            adjacents += tmp[bottom_left]

        # bottom seat
        bottom = i + h_length
        if bottom < full_length and i < full_length - h_length:
            adjacents += tmp[bottom]

        # bottom right seat
        bottom_right = i + h_length + 1
        if bottom_right < full_length and (i + 1) % h_length != 0:
            adjacents += tmp[bottom_right]

        # change state of seat if it meets rules
        if seat == "#":
            if adjacents.count("#") >= 4:
                result[i] = "L"
        else:
            if adjacents.count("#") == 0:
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
