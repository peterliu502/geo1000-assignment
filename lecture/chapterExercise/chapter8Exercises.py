# Exercise 8.0.1
def print_letter(mystr):
    for letter in mystr:
        print(letter)


print_letter("Hello, world!")


# Exercise 8.0.2
prefixes = "JKLMNOPQ"
suffix = 'ack'

for letter in prefixes:
    if letter != "O" and letter != "Q":
        print(letter+suffix)
    else:
        print(letter+"u"+suffix)


# Exercise 8.0.3
def find(word, elm, start=0, end=-1):
    if end < 0:
        end = end + len(word)
    if 0 <= start < end <= len(word):
        for i in range(start, end):
            if word[i] == elm:
                return i
        return -1
    else:
        return "index error"


myword = "abc123abc"
print(find(myword, "c"))
print(find(myword, "c", 3))
print(find(myword, "c", 3, 8))
print(find(myword, "c", 3, 9))
print(find(myword, "c", 3, 3))
print(find(myword, "c", 3, -10))
print(find(myword, "c", 3, 1))

# Exercise 8.2
print("banana".count("a"))

# Exercise 8.3
print("12345"[::-1])


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


print(rotate_word("IBMABCabc", -1))