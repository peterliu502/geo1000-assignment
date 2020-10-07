# Exercise 12.0
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4))


# Exercise 12.1
def most_frequent():
    char_frequent = {}
    with open("chapter10Exercises_10_9.txt", "r+", encoding="utf-8") as fn:
        for line in fn.readlines():
            for char in list(line[:-1]):
                if char.isalpha():
                    char_frequent[char] = char_frequent.get(char, 0) + 1
        # print(char_frequent)
        return sorted(list(char_frequent.items()), key=lambda x: x[1], reverse=True)


print(most_frequent())


# Exercise 12.2
words_list = ["12", "21",
              "123", "321", "231", "312", "123", "213", "231", "312",
              "abcd1111", "dbac1111", "acdb1111", "adcb1111", "abcd1111", "bdac1111", "dcba1111",
              "mama2222", "amma2222", "amam2222", "maam2222", "maam2222",
              "QAQ", "AQQ", "QQA", "QQA",
              "12345", "wasd", "!!!"]


# Exercise 12.2.1
def anagram1(words_list):
    anagram_dict = {}
    result_list = []
    for word in words_list:
        word_sorted = sorted(word)
        if tuple(word_sorted) in anagram_dict:
            anagram_dict[tuple(word_sorted)] += [word]
        else:
            anagram_dict[tuple(word_sorted)] = [word]
    for elm in anagram_dict.values():
        if len(elm) > 1:
            result_list.append(sorted(list(set(elm))))
            print(elm)
    return result_list


# Exercise 12.2.2
def anagram2(words_list):
    length_anagram_list = []
    anagram_list = []
    for elm in words_list:
        length_anagram_list.append((len(elm), elm))
    for length, anagram in sorted(length_anagram_list, reverse=True):
        anagram_list.append(anagram)
        print(anagram)
    return anagram_list


anagram2(anagram1(words_list))


# Exercise 12.2.2
def anagram3(words_list):
    anagram_dict = {}
    bingos = ("start", 0)
    for word in words_list:
        word_sorted = sorted(word)
        if tuple(word_sorted) in anagram_dict:
            anagram_dict[tuple(word_sorted)] += [word]
        else:
            anagram_dict[tuple(word_sorted)] = [word]
    for key, value in anagram_dict.items():
        if len(value) > bingos[1]:
            bingos = (key, len(value))
            print(bingos)
    return bingos


anagram3(words_list)


# Exercise 12.2.3
def metathesis(word_list):
    anagram_list = anagram1(words_list)
    metathesis_list = []
    for sublist in anagram_list:
        for first_index in range(len(sublist))[:-1]:
            for second_index in range(len(sublist))[first_index + 1:]:
                compare_list = []
                for i in range(len(sublist[0])):
                    if sublist[first_index][i] == sublist[second_index][i]:
                        compare_list.append(True)
                    else:
                        compare_list.append(False)
                if compare_list.count(False) == 2:
                    metathesis_list.append((sublist[first_index], sublist[second_index]))
    print(metathesis_list)
    return metathesis_list


metathesis(words_list)