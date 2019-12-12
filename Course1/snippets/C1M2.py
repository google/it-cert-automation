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


# These are the snippets shown during the demo videos in C1M2
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

print(7+8)

# >>> print(7+8)
# 15

print("hello "+ "world")

# >>> print("hello "+ "world")
# hello world

print(7+"8")

# >>> print(7+"8")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(type("a"))

# >>> print(type("a"))
# <class 'str'>

print(type(2))

# >>> print(type(2))
# <class 'int'>

print(type(2.5))

# >>> print(type(2.5))
# <class 'float'>

length = 10
width = 2
area = length * width
print(area)

# >>> length = 10
# >>> width = 2
# >>> area = length * width
# >>> print(area)
# 20

print(7+8.5)

# >>> print(7+8.5)
# 15.5

print("a"+"b"+"c")

# >>> print("a"+"b"+"c")
# abc

base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

# >>> base = 6
# >>> height = 3
# >>> area = (base*height)/2
# >>> print("The area of the triangle is: " + str(area))
# The area of the triangle is: 9.0

def greeting(name):
    print("Welcome, " + name)

# >>> def greeting(name):
# ...     print("Welcome, " + name)
# ...

greeting("Kay")

# >>> greeting("Kay")
# Welcome, Kay

greeting("Cameron")

# >>> greeting("Cameron")
# Welcome, Cameron

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

# >>> def greeting(name, department):
# ...     print("Welcome, " + name)
# ...     print("You are part of " + department)
# ...

greeting("Blake", "IT Support")

# >>> greeting("Blake", "IT Support")
# Welcome, Blake
# You are part of IT Support

greeting("Ellis", "Software engineering")

# >>> greeting("Ellis", "Software engineering")
# Welcome, Ellis
# You are part of Software engineering

def area_triangle(base, height):
    return base*height/2

# >>> def area_triangle(base, height):
# ...     return base*height/2
# ...

area_a = area_triangle(5,4)

# >>> area_a = area_triangle(5,4)

area_b = area_triangle(7,3)

# >>> area_b = area_triangle(7,3)

sum = area_a + area_b

# >>> sum = area_a + area_b

print("The sum of both areas is: " + str(sum))

# >>> print("The sum of both areas is: " + str(sum))
# The sum of both areas is: 20.5

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
# ...

hours, minutes, seconds = convert_seconds(5000)

# >>> hours, minutes, seconds = convert_seconds(5000)

print(hours, minutes, seconds)

# >>> print(hours, minutes, seconds)
# 1 23 20

def greeting(name):
    print("Welcome, " + name)

# >>> result = greeting("Jo")
# Welcome, Jo

print(result)

# >>> print(result)
# None

name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

# >>> name = "Kay"
# >>> number = len(name) * 9
# >>>
# >>> print("Hello " + name + ". Your lucky number is " + str(number))
# Hello Kay. Your lucky number is 27

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

# >>> name = "Cameron"
# >>> number = len(name) * 9
# >>>
# >>> print("Hello " + name + ". Your lucky number is " + str(number))
# Hello Cameron. Your lucky number is 63


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

# >>> def lucky_number(name):
# ...     number = len(name) * 9
# ...     print("Hello " + name + ". Your lucky number is " + str(number))
# ...
# >>> lucky_number("Kay")
# Hello Kay. Your lucky number is 27
# >>> lucky_number("Cameron")
# Hello Cameron. Your lucky number is 63

def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

# >>> def calculate(d):
# ...     q = 3.14
# ...     z = q * (d ** 2)
# ...     print(z)
# ...

calculate(5)

# >>> calculate(5)
# 78.5

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

# >>> def circle_area(radius):
# ...     pi = 3.14
# ...     area = pi * (radius ** 2)
# ...     print(area)
# ...

circle_area(5)

# >>> circle_area(5)
# 78.5

print(10>1)

# >>> print(10>1)
# True

print("cat" == "dog")

# >>> print("cat" == "dog")
# False

print (1 != 2)

# >>> print (1 != 2)
# True

print(1 < "1")

# >>> print(1 < "1")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '<' not supported between instances of 'int' and 'str'

print(1 == "1")

# >>> print(1 == "1")
# False

print("Yellow" > "Cyan" and "Brown" > "Magenta")

# >>> print("Yellow" > "Cyan" and "Brown" > "Magenta")
# False

print(25 > 50 or 1 != 2)

# >>> print(25 > 50 or 1 != 2)
# True

print(not 42 == "Answer")

# >>> print(not 42 == "Answer")
# True

