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


# These are the snippets shown during the demo videos in C1M3
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1

# >>> x = 0
# >>> while x < 5:
# ...     print("Not there yet, x=" + str(x))
# ...     x = x + 1
# ...
# Not there yet, x=0
# Not there yet, x=1
# Not there yet, x=2
# Not there yet, x=3
# Not there yet, x=4
# >>> print("x=" + str(x))
# x=5

def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

# >>> def attempts(n):
# ...     x = 1
# ...     while x <= n:
# ...         print("Attempt " + str(x))
# ...         x += 1
# ...     print("Done")
# ...
# >>> attempts(5)
# Attempt 1
# Attempt 2
# Attempt 3
# Attempt 4
# Attempt 5
# Done

# >>> while my_variable < 10:
# ...     print("Hello")
# ...     my_variable += 1
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'my_variable' is not defined

# >>> my_variable = 5
# >>> while my_variable < 10:
# ...     print("Hello")
# ...     my_variable += 1
# ...
# Hello
# Hello
# Hello
# Hello
# Hello

x = 1
sum = 0
while x < 10:
  sum += x
  x += 1

product = 1
while x < 10:
  product = product * x
  x += 1

# >>> x = 1
# >>> sum = 0
# >>> while x < 10:
# ...     sum = sum + x
# ...     x = x + 1
# ...
# >>> product = 1
# >>> while x < 10:
# ...     product = product * x
# ...     x = x + 1
# ...
# >>> print(sum, product)
# 45 1

# >>> for x in range(5):
# ...     print(x)
# ...
# 0
# 1
# 2
# 3
# 4

# >>> product = 1
# >>> for n in range(1,10):
# ...     product = product * n
# ...
# >>> print(product)
# 362880

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

# >>> def to_celsius(x):
# ...     return (x-32)*5/9
# ...
# >>> for x in range(0,101,10):
# ...     print(x, to_celsius(x))
# ...
# 0 -17.77777777777778
# 10 -12.222222222222221
# 20 -6.666666666666667
# 30 -1.1111111111111112
# 40 4.444444444444445
# 50 10.0
# 60 15.555555555555555
# 70 21.11111111111111
# 80 26.666666666666668
# 90 32.22222222222222
# 100 37.77777777777778

# >>> for left in range(7):
# ...     for right in range(left, 7):
# ...         print("[" + str(left) + "|" + str(right) + "]", end=" ")
# ...     print()
# ...
# [0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6]
# [1|1] [1|2] [1|3] [1|4] [1|5] [1|6]
# [2|2] [2|3] [2|4] [2|5] [2|6]
# [3|3] [3|4] [3|5] [3|6]
# [4|4] [4|5] [4|6]
# [5|5] [5|6]
# [6|6]

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']

# Interactive code snippet
# >>> teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
# >>> for home_team in teams:
# ...     for away_team in teams:
# ...         if home_team != away_team:
# ...             print(home_team + " vs " + away_team)
# ...
# Dragons vs Wolves
# Dragons vs Pandas
# Dragons vs Unicorns
# Wolves vs Dragons
# Wolves vs Pandas
# Wolves vs Squirrels
# Pandas vs Dragons
# Pandas vs Wolves
# Pandas vs Squirrels
# Unicorns vs Dragons
# Unicorns vs Wolves
# Unicorns vs Pandas

# >>> for x in 25:
# ...     print(x)
# ...
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not iterable
#
# >>> for x in range(25):
# ...     print(x)
# ...
#
# >>> for x in [25]:
# ...     print(x)
# ...
# 25

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

# >>> def greet_friends(friends):
# ...     for friend in friends:
# ...         print("Hi " + friend)
# ...
# >>> greet_friends("Berry")
# Hi B
# Hi e
# Hi r
# Hi r
# Hi y


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

# >>> def factorial(n):
# ...     print("Factorial called with " + str(n))
# ...     if n < 2:
# ...         print("Returning 1")
# ...         return 1
# ...     result = n * factorial(n-1)
# ...     print("Returning " + str(result) + " for factorial of " + str(n))
# ...     return result
# ...
# >>> print(factorial(4))
# Factorial called with 4
# Factorial called with 3
# Factorial called with 2
# Factorial called with 1
# Returning 1
# Returning 2 for factorial of 2
# Returning 6 for factorial of 3
# Returning 24 for factorial of 4
# 24

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

# >>> def factorial(n):
# ...     if n < 2:
# ...         return 1
# ...     return n * factorial(n-1)
# ...
# >>> factorial(1000)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in factorial
#   File "<stdin>", line 4, in factorial
#   File "<stdin>", line 4, in factorial
#   [Previous line repeated 994 more times]
#   File "<stdin>", line 2, in factorial
# RecursionError: maximum recursion depth exceeded in comparison

