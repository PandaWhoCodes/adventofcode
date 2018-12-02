if __name__ == "__main__":
    with open('input.txt') as data:
        numbers = [int(number) for number in data.readlines()]
        current_freq = 0
        idx = 0
        past_frequencies = set()
        while True:
            if idx == len(numbers):
                idx = 0
            if current_freq in past_frequencies:
                break
            past_frequencies.add(current_freq)
            current_freq += numbers[idx]
            idx += 1
        print(f"The first repeated frequency is {current_freq}")
