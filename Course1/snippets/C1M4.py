#!/usr/bin/env python3
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# These are the snippets shown during the demo videos in C1M4
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

# Strings

# >>> name = "Sasha"
# >>> color = 'Gold'
#
# >>> place = "Cambridge'
#   File "<stdin>", line 1
#     place = "Cambridge'
#                       ^
# SyntaxError: EOL while scanning string literal
#
# '
#
# >>> pet = ""
#
# >>> pet = "loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong cat"
#
# >>> print("Name: " + name + ", Favorite color: " + color)
# Name: Sasha, Favorite color: Gold
#
# >>> "example " * 3
# 'example example example '
#
# >>> len(pet)
# 69
#
# >>> name = "Jaylen"
# >>> print(name[1])
# a
#
# >>> print(name[0])
# J
#
# >>> print(name[5])
# n
# >>> print(name[6])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range
#
# >>> text = "Random string with a lot of characters"
# >>> print(text[-1])
# s
# >>> print(text[-2])
# r
#
#
# >>> color = "Orange"
# >>> color[1:4]
# 'ran'
#
#
# >>> fruit = "Pineapple"
# >>> print(fruit[:4])
# Pine
# >>> print(fruit[4:])
# apple

message = "A kong string with a silly typo"

# >>> message = "A kong string with a silly typo"
# >>> message[2] = "l"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment
#
# >>> new_message = message[0:2] + "l" + message[3:]
# >>> print(new_message)
# A long string with a silly typo
#
# >>> message = "This is a new message"
# >>> print(message)
# This is a new message
# >>> message = "And another one"
# >>> print(message)
# And another one
#
# >>> pets="Cats & Dogs"
# >>> pets.index("&")
# 5
#
# >>> pets.index("C")
# 0
# >>> pets.index("Dog")
# 7
#
# >>> pets.index("s")
# 3
#
# >>> pets.index("x")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found
#
# >>> "Dragons" in pets
# False
# >>> "Cats" in pets
# True
#
# >>> "Mountains".upper()
# 'MOUNTAINS'
# >>> "Mountains".lower()
# 'mountains'
#
#
# >>> answer = "YES"
# >>> if answer.lower() == "yes":
# ...     print("User said yes")
# ...
# User said yes
#
# >>> " yes ".strip()
# 'yes'
#
#
# >>> " yes ".lstrip()
# 'yes '
# >>> " yes ".rstrip()
# ' yes'
#
#
# >>> "The number of times e occurs in this string is 4".count("e")
# 4
#
# >>> "Forest".endswith("rest")
# True
#
# >>> "Forest".isnumeric()
# False
# >>> "12345".isnumeric()
# True
#
# >>> int("12345") + int("54321")
# 66666
#
# >>> " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
# 'This is a phrase joined by spaces'
#
# >>> "...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
# 'This...is...a...phrase...joined...by...triple...dots'
#
# >>> "This is another example".split()
# ['This', 'is', 'another', 'example']
#
#
# >>> name = "Manny"
# >>> number = len(name) * 3
# >>> print("Hello {}, your lucky number is {}".format(name, number))
# Hello Manny, your lucky number is 15
#
# >>> print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
# Your lucky number is 15, Manny.
#
# >>> price = 7.5
# >>> with_tax = price * 1.09
# >>> print(price, with_tax)
# 7.5 8.175
#
# >>> print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
# Base price: $7.50. With Tax: $8.18

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# >>> def to_celsius(x):
# ...     return (x-32)*5/9
# ...
# >>> for x in range(0,101,10):
# ...     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
# ...
#   0 F | -17.78 C
#  10 F | -12.22 C
#  20 F |  -6.67 C
#  30 F |  -1.11 C
#  40 F |   4.44 C
#  50 F |  10.00 C
#  60 F |  15.56 C
#  70 F |  21.11 C
#  80 F |  26.67 C
#  90 F |  32.22 C
# 100 F |  37.78 C

# Lists
# -----

# >>> x = ["Now", "we", "are", "cooking!"]
#
# >>> type(x)
# <class 'list'>
#
# >>> print(x)
# ['Now', 'we', 'are', 'cooking!']
#
# >>> len(x)
# 4
#
# >>> "are" in x
# True
# >>> "Today" in x
# False
#
# >>> print(x[0])
# Now
# >>> print(x[3])
# cooking!
#
# >>> print(x[4])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
#
# >>> x[1:3]
# ['we', 'are']
#
#
# >>> x[:2]
# ['Now', 'we']
# >>> x[2:]
# ['are', 'cooking!']
#
#
# >>> fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# >>> fruits.append("Kiwi")
# >>> print(fruits)
# ['Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
#
# >>> fruits.insert(0, "Orange")
# >>> print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi']
#
# >>> fruits.insert(25, "Peach")
# >>> print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Melon', 'Kiwi', 'Peach']
#
# >>> fruits.remove("Melon")
# >>> print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Apple', 'Kiwi', 'Peach']
#
# >>> fruits.remove("Pear")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
#
# >>> fruits.pop(3)
# 'Apple'
# >>> print(fruits)
# ['Orange', 'Pineapple', 'Banana', 'Kiwi', 'Peach']
#
# >>> fruits[2] = "Strawberry"
# >>> print(fruits)
# ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

# >>> def convert_seconds(seconds):
# ...     hours = seconds // 3600
# ...     minutes = (seconds - hours * 3600) // 60
# ...     remaining_seconds = seconds - hours * 3600 - minutes * 60
# ...     return hours, minutes, remaining_seconds
# >>> result = convert_seconds(5000)
# >>> type(result)
# <class 'tuple'>
#
# >>> print(result)
# (1, 23, 20)
#
# >>> hours, minutes, seconds = result
# >>> print(hours, minutes, seconds)
# 1 23 20
#
# >>> hours, minutes, seconds = convert_seconds(1000)
# >>> print(hours, minutes, seconds)
# 0 16 40
#
#
# >>> animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# >>> chars = 0
# >>> for animal in animals:
# ...     chars += len(animal)
# ...
# >>> print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
# Total characters: 22, Average length: 5.5
#
# >>> winners = ["Ashley", "Dylan", "Reese"]
# >>> for index, person in enumerate(winners):
# ...     print("{} - {}".format(index + 1, person))
# ...
# 1 - Ashley
# 2 - Dylan
# 3 - Reese
#
#
# >>> def full_emails(people):
# ...     result = []
# ...     for email, name in people:
# ...         result.append("{} <{}>".format(name, email))
# ...     return result
# ...
# >>> print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']
#
#
# >>> multiples = []
# >>> for x in range(1,11):
# ...   multiples.append(x*7)
# ...
# >>> print(multiples)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
#
#
# >>> multiples = [ x*7 for x in range(1,11) ]
# >>> print(multiples)
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]

# >>> languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# >>> lengths = [len(language) for language in languages]
# >>> print(lengths)
# [6, 4, 4, 2, 4, 1]
#
# >>> z = [ x for x in range(0,101) if x % 3 == 0]
# >>> print(z)
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
#

# Dictionaries
# ------------

# >>> x = {}
# >>> type(x)
# <class 'dict'>
#
# >>> file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
# >>> print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23}
#
# >>> file_counts["txt"]
# 14
#
# >>> "jpg" in file_counts
# True
# >>> "html" in file_counts
# False
#
# >>> file_counts["cfg"] = 8
# >>> print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
#
# >>> file_counts["csv"] = 17
# >>> print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
#
# >>> del file_counts["cfg"]
# >>> print(file_counts)
# {'jpg': 10, 'txt': 14, 'csv': 17, 'py': 23}
#
# >>> file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
#
# >>> for extension in file_counts:
# ...     print(extension)
# ...
# jpg
# txt
# csv
# py
#
# >>> for ext, amount in file_counts.items():
# ...     print("There are {} files with the .{} extension".format(amount, ext))
# ...
# There are 10 files with the .jpg extension
# There are 14 files with the .txt extension
# There are 2 files with the .csv extension
# There are 23 files with the .py extension
#
# >>> file_counts.keys()
# dict_keys(['jpg', 'txt', 'csv', 'py'])
# >>> file_counts.values()
# dict_values([10, 14, 17, 23])
#
# >>> for value in file_counts.values():
# ...     print(value)
# ...
# 10
# 14
# 2
# 23

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

# >>> def count_letters(text):
# ...     result = {}
# ...     for letter in text:
# ...         if letter not in result:
# ...             result[letter] = 0
# ...         result[letter] += 1
# ...     return result
# ...
# >>> count_letters("aaaaa")
# {'a': 5}
# >>> count_letters("tenant")
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}
# >>> count_letters("a long string with a lot of letters")
# {'a': 2, ' ': 7, 'l': 3, 'o': 3, 'n': 2, 'g': 2, 's': 2, 't': 5, 'r': 2, 'i': 2, 'w': 1, 'h': 1, 'f': 1, 'e': 2}


