import math
import time
import functools


# 1
def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


# Ex:
print(multiply_list([1, 2, 3, 4]))

# совсем без импорта не получится(((
# def multiply_list(numbers):
#     return functools.reduce(lambda x, y: x * y, numbers)

# # Ex:
# print(multiply_list([1, 2, 3, 4]))


# 2
def count_case(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return {"Uppercase": upper, "Lowercase": lower}


# Ex:
print(count_case("Hello World!"))


# 3
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


# Ex:
print(is_palindrome("MaDaM"))
print(is_palindrome("hello"))


# 4
def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


# Ex:
delayed_sqrt(25100, 2123)


# 5
def all_true(t):
    return all(t)


# Ex:
print(all_true((True, True, True)))
print(all_true((True, False, True)))
print(all_true((0, 1, 2)))
print(all_true((3, 1, 2)))
