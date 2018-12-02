if __name__ == "__main__":
    with open('input.txt') as data:
        total = sum([int(number) for number in data.readlines()])
        print(total)
