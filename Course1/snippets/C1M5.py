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

#
# These are the snippets shown during the demo videos in C1M5
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

# >>> type(0)
# <class 'int'>
#
# >>> type("")
# <class 'str'>
#
# >>> dir("")
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#
# >>> help("")
#
# >>> class Apple:
# ...     pass
# ...
# >>> class Apple:
# ...     color = ""
# ...     flavor = ""
#
# >>> jonagold = Apple()
#
# >>> jonagold.color = "red"
# >>> jonagold.flavor = "sweet"
#
# >>> print(jonagold.color)
# red
# >>> print(jonagold.flavor)
# sweet
#
# >>> print(jonagold.color.upper())
# RED
#
# >>> golden = Apple()
# >>> golden.color = "Yellow"
# >>> golden.flavor = "Soft"

class Piglet:
    pass

hamlet = Piglet()


class Piglet:
    def speak(self):
        print("oink oink")

# >>> class Piglet:
# ...     def speak(self):
# ...         print("oink oink")
# ...
# >>> hamlet = Piglet()
# >>> hamlet.speak()
# oink oink

class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

# >>> class Piglet:
# ...     name = "piglet"
# ...     def speak(self):
# ...         print("Oink! I'm {}! Oink!".format(self.name))
# >>> hamlet = Piglet()
# >>> hamlet.name = "Hamlet"
# >>> hamlet.speak()
# Oink! I'm Hamlet! Oink!
#
# >>> petunia = Piglet()
# >>> petunia.name = "Petunia"
# >>> petunia.speak()
# Oink! I'm Petunia! Oink!

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18

# >>> class Piglet:
# ...     years = 0
# ...     def pig_years(self):
# ...         return self.years * 18
# ...
# >>> piggy = Piglet()
# >>> print(piggy.pig_years())
# 0
# >>> piggy.years = 2
# >>> print(piggy.pig_years())
# 36

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# >>> class Apple:
# ...     def __init__(self, color, flavor):
# ...         self.color = color
# ...         self.flavor = flavor
# ...
#
# >>> jonagold = Apple("red", "sweet")

# >>> print(jonagold.color)
# red
#
# >>> print(jonagold)
# <__main__.Apple object at 0x7f5861147860>

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# >>> class Apple:
# ...     def __init__(self, color, flavor):
# ...         self.color = color
# ...         self.flavor = flavor
# ...     def __str__(self):
# ...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
# ...
#
# >>> jonagold = Apple("red", "sweet")
# >>> print(jonagold)
# This apple is red and its flavor is sweet

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# help(Apple)
# Help on class Apple in module __main__:
# class Apple(builtins.object)
#  |  Methods defined here:
#  |
#  |  __init__(self, color, flavor)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  __str__(self)
#  |      Return str(self).
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#
#
# >>> def to_seconds(hours, minutes, seconds):
# ...     """Returns the amount of seconds in the given hours, minutes and seconds."""
# ...     return hours*3600+minutes*60+seconds
# ...
#
# help(to_seconds)
# Help on function to_seconds in module __main__:
# to_seconds(hours, minutes, seconds)
#     Returns the amount of seconds in the given hours, minutes and seconds.

class Piglet:
    """Represents a piglet that can say their name."""
    years = 0
    name = ""
    def speak(self):
        """Outputs a message including the name of the piglet."""
        print("Oink! I'm {}! Oink!".format(self.name))
    def pig_years(self):
        """Converts the current age to equivalent pig years."""
        return self.years * 18

# Inheritance
# -----------

class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# >>> class Fruit:
# ...     def __init__(self, color, flavor):
# ...         self.color = color
# ...         self.flavor = flavor
# ...
#
# >>> class Apple(Fruit):
# ...     pass
# ...
# >>> class Grape(Fruit):
# ...     pass
# ...
#
# >>> granny_smith = Apple("green", "tart")
#
# >>> carnelian = Grape("purple", "sweet")
#
# >>> print(granny_smith.flavor)
# tart
# >>> print(carnelian.color)
# purple

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(
            name=self.name, sound=self.sound))

class Piglet(Animal):
    sound = "Oink!"

# >>> class Animal:
# ...     sound = ""
# ...     def __init__(self, name):
# ...         self.name = name
# ...     def speak(self):
# ...         print("{sound} I'm {name}! {sound}".format(
# ...             name=self.name, sound=self.sound))
# ...
# >>> class Piglet(Animal):
# ...     sound = "Oink!"
#
# >>> hamlet = Piglet("Hamlet")
# >>> hamlet.speak()
# Oink! I'm Hamlet! Oink!
#
# >>> class Cow(Animal):
# ...     sound = "Moooo"
# ...
#
# >>> milky = Cow("Milky White")
# >>> milky.speak()
# Moooo I'm Milky White! Moooo

# Composition
# -----------

# >>> class Repository:
# ...     def __init__(self):
# ...         self.packages = {}
# ...     def add_package(self, package):
# ...         self.packages[package.name] = package
# ...     def total_size(self):
# ...         result = 0
# ...         for package in self.package.values():
# ...             result += package.size
# ...         return result

# Modules
# -------

# >>> import random
#
# >>> random.randint(1,10)
# 8
# >>> random.randint(1,10)
# 7
# >>> random.randint(1,10)
# 1
#
# >>> import datetime
#
# >>> now = datetime.datetime.now()
# >>> type(now)
# <class 'datetime.datetime'>
#
# >>> print(now)
# 2019-04-24 16:54:55.155199
#
# >>> now.year
# 2019
#
# >>> print(now + datetime.timedelta(days=28))
# 2019-05-22 16:54:55.155199


