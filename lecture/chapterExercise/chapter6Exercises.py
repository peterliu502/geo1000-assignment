# Exercise 6.0,1
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


# Exercise 6.0,2
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False


# Exercise 6.2
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))
print(ack(3, 6))


# Exercise 6.3
def first(word):
    return word[0]


def middle(word):
    return word[1:-1]


def last(word):
    return word[-1]


print(middle("123"),
      middle("12"),
      middle("1"),
      middle(""))


def reverse(word):
    if len(word) == 0:
        return ""
    elif len(word) == 1:
        return word
    else:
        return last(word) + reverse(middle(word)) + first(word)


def is_palindrome(word):
    if reverse(word) == word:
        return True
    else:
        return False


print("", "is is palindrome", is_palindrome(""),
      "\n1", "is is palindrome", is_palindrome("1"),
      "\n121", "is is palindrome", is_palindrome("121"),
      "\n1234", "is is palindrome", is_palindrome("1234"),
      "\n")


# Exercise 6.4
def is_power(a, b):
    if b == 0:
        return False
    elif b == 1 or a == 0:
        return True
    if a % b == 0 and is_power(a / b, b):
        return True
    else:
        return False


print("is_power(0, 0) is ", is_power(0, 0),
      "\nis_power(0, 2) is ", is_power(0, 2),
      "\nis_power(1, 0) is ", is_power(1, 0),
      "\nis_power(1, 1) is ", is_power(1, 1),
      "\nis_power(2, 1) is ", is_power(2, 1),
      "\nis_power(4, 2) is ", is_power(4, 2),
      "\nis_power(3, 2) is ", is_power(3, 2))


# Exercise 6.5
def gcd(a, b):
    if b == 0:
        return a
    elif a == 0:
        return 0
    else:
        return gcd(b, a % b)


print(gcd(1, 1),
      gcd(2, 2),
      gcd(4, 2),
      gcd(0, 1),
      gcd(1, 0),
      gcd(2, 3),
      gcd(10, 15))