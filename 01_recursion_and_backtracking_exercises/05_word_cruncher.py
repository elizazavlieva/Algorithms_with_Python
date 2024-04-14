def solutions(index, target, words_by_index, words_count, used_words):
    if index >= len(target):
        print(" ".join(used_words))
        return

    if index not in words_by_index.keys():
        return

    for word in words_by_index[index]:
        if words_count[word] == 0:
            continue

        used_words.append(word)
        words_count[word] -= 1

        solutions(index + len(word), target, words_by_index, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


text = input().split(", ")
target = input()

words_by_index = {}
words_count = {}

for word in text:
    if word in words_count:
        words_count[word] += 1
        continue

    words_count[word] = 1
    try:
        idx = 0
        while True:
            idx = target.index(word, idx)

            if idx not in words_by_index:
                words_by_index[idx] = []
            words_by_index[idx].append(word)
            idx += len(word)

    except ValueError:
        pass


solutions(0, target, words_by_index, words_count, [])
