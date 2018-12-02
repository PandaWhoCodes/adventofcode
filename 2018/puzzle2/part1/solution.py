def return_count(word):
    d = {}
    for alpha in word:
        if alpha in d:
            d[alpha] += 1
        else:
            d[alpha] = 1
    return d


def do_the_math(counts, twos_and_threes):
    two = 0
    three = 0
    for alpha in counts:
        if counts[alpha] == 2:
            two = 1
        if counts[alpha] == 3:
            three = 1
    twos_and_threes["two"] = twos_and_threes["two"] + two
    twos_and_threes["three"] = twos_and_threes["three"] + three
    return twos_and_threes


if __name__ == "__main__":
    with open('input.txt') as data:
        twos_and_threes = {"two": 0, "three": 0}
        for line in data.readlines():
            twos_and_threes = do_the_math(return_count(line), twos_and_threes)
        print(twos_and_threes["two"] * twos_and_threes["three"])
