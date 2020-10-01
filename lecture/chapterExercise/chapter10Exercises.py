from time import time


# Exercise 10.1
def nested_sum(mylist):
    sum = 0
    for i in mylist:
        if type(i) == int:
            sum += i
        else:
            sum += nested_sum(i)
    return sum


print(nested_sum([[1, 2], [3], [4, 5, 6]]))


# Exercise 10.2
def cumsum(mylist):
    sum = 0
    sum_list = []
    for i in range(len(mylist)):
        sum += mylist[i]
        sum_list.append(sum)
    return sum_list


print(cumsum([1, 2, 3]))


# Exercise 10.3
def middle(mylist):
    return mylist[1:-1]


print(middle([1, 2, 3, 4]))


# Exercise 10.4
def chop(mylist):
    mylist.pop(0)
    mylist.pop(-1)
    return None


t = [1, 2, 3, 4]
print(chop(t), t)


# Exercise 10.5
def is_sorted(mylist):
    list_copy = sorted(mylist[:])
    if list_copy == mylist:
        return True
    else:
        return False


print(is_sorted([1, 2, 2]), is_sorted(["b", "a"]))


# Exercise 10.6
def is_anagam(str1, str2):
    if sorted(list(str1)) == sorted(list(str2)):
        return True
    else:
        return False


print(is_anagam("l1isa", "sia1l"), is_anagam("123a", "1234"))


# Exercise 10.7
def has_duplicates(mylist):
    if len(dict(zip(mylist, range(len(mylist)))).keys()) == len(mylist):
        return False
    else:
        return True


print(has_duplicates([1, 2, 3]), has_duplicates([1, 2, 1]))


# Exercise 10.8
def read_words1():
    start = time()
    article = []
    with open("chapter10Exercises_10_9.txt", 'r+', encoding='utf-8') as file:
        for line in file.readlines():
            line_list = line[:-1].split()
            for word in line_list:
                article.append(word)
    print("time rw1: " + str(time() - start))
    return article


def read_words2():
    start = time()
    article = []
    with open("chapter10Exercises_10_9.txt", 'r+', encoding='utf-8') as file:
        for line in file.readlines():
            line_list = line[:-1].split()
            for word in line_list:
                article = article + [word]
    print("time rw2: " + str(time() - start))
    return article


read_words1()
read_words2()


# Exercise 10.10

def pure_words(pw_list):
    pure_word = []
    for word in pw_list:
        if word.isalpha():
            pure_word.append(word)
    return sorted(pure_word)


def in_bisect(mylist, target):
    start = 0
    end = len(mylist) - 1
    middle = int((start + end) / 2)
    if mylist[start] == target or mylist[end] == target or mylist[middle] == target:
        return True
    elif start == middle:
        return False
    elif mylist[middle] < target:
        return in_bisect(mylist[middle:], target)
    else:
        return in_bisect(mylist[:middle], target)


def ten_thousand_times(read_word, target):
    time_sum1 = 0
    time_sum2 = 0
    for i in range(10000):
        start1 = time()
        in_bisect(read_word, target)
        time_sum1 += float(time() - start1)
        start2 = time()
        target in read_word
        time_sum2 += float(time() - start2)
    return time_sum1, time_sum2


read_word = pure_words(read_words1())
time1, time2 = ten_thousand_times(read_word, "Wageningen")
print(time1, time2)


# Exercise 10.11
def reverse_pairs(mylist):
    new_list = mylist[:]
    reverse_list = []
    for word in new_list:
        if word[::-1] in new_list:
            reverse_list.append((word, word[::-1]))
            while word[::-1] in new_list:
                new_list.remove(word[::-1])
    return reverse_list


print(reverse_pairs(["123", "321", "213", "acx",
                     "xac", "1s1", "211", "112",
                     "1s1", "211", "112", "211",
                     "112", "1s1", "211", "112"]))


