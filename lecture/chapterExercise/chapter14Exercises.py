import os
import chapter12Exercises
import shelve
import hashlib


# Exercise 14.0
def mywalk(mydir):
    for root, dirs, files in os.walk(mydir, topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
    print("")


direction = "D:\myCourse\geo1000\geo1000-assignment\lecture"
mywalk(direction)


# Exercise 14.1
def sed(pattern_str, replacement_str, filenm1, filenm2):
    with open(filenm1, "r+", encoding="utf-8") as file1:
        with open(filenm2, "w", encoding="utf-8") as file2:
            for line in file1.readlines():
                file2.write(line[:].replace(pattern_str, replacement_str))


file1 = "chapter14Exercises_14_1_file1.txt"
file2 = "chapter14Exercises_14_1_file2.txt"
sed("is my", "was his", file1, file2)


# Exercise 14.2
def store_anagrams(filenm):
    with shelve.open(filenm, "c") as shelf:
        for k, v in chapter12Exercises.anagram1(chapter12Exercises.words_list)[1].items():
            shelf[str(k)] = v  # The key value of shelve should only be str type


def read_anagrams(filenm, word):
    with shelve.open(filenm) as shelf:
        return shelf[str(tuple(sorted(word)))]


store_anagrams("myshelf")
print(read_anagrams("myshelf", "321"), "\n")


# Exercise 14.3
def duplicate(mydir, suffix):
    md5_dict = {}
    for root, dirs, files in os.walk(mydir, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            if suffix in name:
                with open(path, "r+", encoding="utf-8") as file:
                    md5obj = hashlib.md5()
                    md5obj.update(file.read().encode("utf-8"))
                    md5val = md5obj.hexdigest()
                    md5_dict.setdefault(md5val, [])
                    md5_dict[md5val].append(path)
    for md5 in md5_dict.keys():
        if len(md5_dict[md5]) == 1:
            print("{}:\n{}\n\tdoesn't have any duplicate.".format(md5, md5_dict[md5][0]))
        else:
            print(md5 + ":")
            for file in md5_dict[md5]:
                print("\tduplicate {}: {}".format(md5_dict[md5].index(file) + 1, file))
        print("")


duplicate(direction, ".xml")
