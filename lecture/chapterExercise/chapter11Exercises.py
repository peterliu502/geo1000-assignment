from time import time

# Exercise 11.0
def histogram(mystr):
    mydict = dict()
    for char in mystr:
        mydict[char] = mydict.get(char, 0) + 1
    return mydict


print(histogram("classroom"))


# Exercise 11.1
def read_words():
    mydict = {}
    with open("chapter10Exercises_10_9.txt", 'r+', encoding='utf-8') as file:
        for line in file.readlines():
            line_list = line[:-1].split()
            for word in line_list:
                mydict[word] = mydict.get(word, 0) + 1
    return mydict


print(read_words())


# Exercise 11.2
def invert_dict(mydict):
    invert = {}
    for key in mydict:
        val = mydict[key]
        invert.setdefault(val, [])
        invert[val].append(key)
    return invert


print(invert_dict(histogram("classroom")))


# Exercise 11.3
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


pre_calcu = {}


def ackermann_memo1(m, n):
    global pre_calcu
    if (m, n) in pre_calcu:
        return pre_calcu[(m, n)]
    elif m == 0:
        result = n + 1
        pre_calcu[(m, n)] = result
        return result
    elif m > 0 and n == 0:
        result = ackermann_memo1(m - 1, 1)
        pre_calcu[(m, n)] = result
        return result
    elif m > 0 and n > 0:
        result = ackermann_memo1(m - 1, ackermann_memo1(m, n - 1))
        pre_calcu[(m, n)] = result
        return result


start = time()
num = 100 # n = 0 - 498
for i in range(num)[1:]:
    print(ackermann_memo1(2, i))
    print("ack_memo " + str(i) + ": " + str(time() - start))

start = time()
for i in range(num)[1:]:
    print(ack(2, i))
    print("ack_1 " + str(i) + ": " + str(time() - start))


# Exercise 11.4
def has_duplicates(mylist):
    mydict = dict()
    for word in mylist:
        mydict[word] = mydict.setdefault(word, 0) + 1
        if mydict[word] > 1:
            return True
    return False


def has_duplicates1(mylist):
    if len(dict(zip(mylist, range(len(mylist)))).keys()) == len(mylist):
        return False
    else:
        return True


def has_duplicates2(mylist):
    temp = []
    for word in mylist:
        if word in temp:
            return True
        else:
            temp.append(word)
    return False


start = time()
print(has_duplicates(list(pre_calcu) * 1000))
print("has_duplicates " + str(time() - start))
start = time()
print(has_duplicates1(list(pre_calcu) * 1000))
print("has_duplicates1 " + str(time() - start))
start = time()
print(has_duplicates2(list(pre_calcu) * 1000))
print("has_duplicates2 " + str(time() - start))


# Exercise 11.5
# Exercise 8.5
def rotate_word(mystr, myint):
    final_str = ""
    for i in mystr:
        myord = ord(i) + myint
        if ord(i) >= 97:
            if myord > 122:
                myord = myord - 26
            elif myord < 97:
                myord = myord + 26
        else:
            if myord > 96:
                myord = myord - 26
            elif myord < 65:
                myord = myord + 26
        final_str = final_str + chr(myord)
    return final_str


def rotate_pair(mylist, myint):
    rotate_dict = {}
    result_list = []
    for elm in mylist:
        if elm in rotate_dict:
            result_list.append((elm, rotate_dict[elm]))
        else:
            rotate_dict[rotate_word(elm, myint)] = elm
    return result_list


rotate_int = -1
word_list = ["XYZ", "daddy", "today", "2020", "Friday",
             rotate_word("XYZ", rotate_int), rotate_word("Friday", rotate_int),
             rotate_word("daddy", rotate_int), rotate_word("1234", rotate_int), ]
print(rotate_pair(word_list, rotate_int))
