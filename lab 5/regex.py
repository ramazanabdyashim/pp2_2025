import re


# Task1
def abstr(string):
    pattern = r"ab*"
    match = re.fullmatch(pattern, string)
    return bool(match)


# Eaxmple:
print(abstr("a"))
print(abstr("ab"))
print(abstr("abb"))
print(abstr("b"))
print(abstr("abc"))


print("-----------------\n")


# Task2
def abb(string):
    pattern = r"ab{2,3}$"
    match = re.fullmatch(pattern, string)
    return bool(match)


# Example:
print(abb("abb"))
print(abb("abbb"))
print(abb("a"))
print(abb("ab"))
print(abb("abbbb"))

print("-----------------\n")


# Task 3
def seqlow(string):
    pattern = r"[a-z]+_[a-z]+"
    lowe = re.findall(pattern, string)
    return lowe


# Example:
print(seqlow("abc_def"))
print(seqlow("a_b"))
print(seqlow("abc_def_ghi"))
print(seqlow("a1_b2"))
print(seqlow("abcDef"))

print("-----------------\n")


# Task4
def uplow(string):
    pattern = r"[A-Z][a-z]+"
    uplow = re.findall(pattern, string)
    return uplow


# Example:
print(uplow("Hello"))
print(uplow("HelloWorld"))
print(uplow("helloWorld"))
print(uplow("HELLOworld"))
print(uplow("AaaBbb"))

print("-----------------\n")


# task5
def a_b(string):
    pattern = r"a.*b$"
    match = re.fullmatch(pattern, string)
    return bool(match)


# Example:
print(a_b("ab"))
print(a_b("acb"))
print(a_b("a123b"))
print(a_b("aXb"))
print(a_b("b"))
print(a_b("abX"))

print("-----------------\n")


# Task6
def rep(string):
    return re.sub(r"[ ,.]", ":", string)


# Exmaple:
print(rep("hello world, this is a test."))
print(rep("no,spaces.or,commas"))

print("-----------------\n")


# Task7
def snake_camel(string):
    word = string.split("_")
    camel = word[0] + "".join(w.capitalize() for w in word[1:])
    return camel


# Example:
print(snake_camel("snake_case_example"))
print(snake_camel("longer_snake_case_string"))

print("-----------------\n")


# Task8
def spli(string):
    return re.split(r"(?=[A-Z])", string)[1:]


# Exmaple:
print(spli("CamelCaseString"))
print(spli("AnotherExampleString"))

print("-----------------\n")


# Task9
def ins(string):
    result = re.split(r"(?=[A-Z])", string)[1:]
    result2 = " ".join(result)
    return result2


# Example:
print(ins("CamelCaseString"))
print(ins("ThisIsATest"))

print("-----------------\n")


# Task10
def camel_snake(string):
    result = []
    for char in string:
        if char.isupper():
            if result:
                result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


# ex:
print(camel_snake("CamelCaseString"))
print(camel_snake("AnotherExampleString"))
