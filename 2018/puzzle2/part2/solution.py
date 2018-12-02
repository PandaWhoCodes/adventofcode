def return_diff(word1, word2):
    if abs(len(word1) - len(word2)) > 2:
        return False
    d = {}
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            d[i] = word1[i]
    return d


def return_intersection(word1, word2,d):
    word = word1[:d] + word1[d+1:]
    return word


if __name__ == "__main__":
    with open('input.txt') as data:
        words = data.read().split("\n")
        print(words)
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                count = return_diff(words[i], words[j])
                if len(count) == 1:
                    print(words[i], words[j], return_intersection(words[i], words[j],list(count.keys())[0]))

