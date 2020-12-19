import time


def main():
    input = [9, 6, 0, 10, 18, 2, 1]

    my_dict = {
        number: {
            "once": True,
            "second-last": i + 1,
            "last-turn": i + 1,
        }
        for i, number in enumerate(input)
    }

    n = input[-1]

    for turn in range(len(input) + 1, 30000000 + 1):

        n = 0 if my_dict[n]["once"] else (turn - 1 - my_dict[n]["second-last"])
        my_dict[n] = (
            {"once": False, "second-last": my_dict[n]["last-turn"], "last-turn": turn}
            if n in my_dict
            else {"once": True, "second-last": turn, "last-turn": turn}
        )

    print(n)


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
