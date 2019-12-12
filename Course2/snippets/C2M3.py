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

# These are the snippets shown during the demo videos in C2M3
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

# >>> log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# >>> index = log.index("[")
# >>> print(log[index+1:index+6])
# 12345
 
import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])
 
# >>> import re
# >>> log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# >>> regex = r"\[(\d+)\]"
# >>> result = re.search(regex, log)
# >>> print(result[1])
# 12345
# 
# >>> import re
# >>> result = re.search(r"aza", "plaza")
# 
# >>> print(result)
# <re.Match object; span=(2, 5), match='aza'>
# 
# >>> result = re.search(r"aza", "bazaar")
# >>> print(result)
# <re.Match object; span=(1, 4), match='aza'>
# 
# >>> result = re.search(r"aza", "maze")
# >>> print(result)
# None
# 
# >>> print(re.search(r"^x", "xenon"))
# <re.Match object; span=(0, 1), match='x'>
# 
# >>> print(re.search(r"p.ng", "penguin"))
# <re.Match object; span=(0, 4), match='peng'>
# 
# >>> print(re.search(r"p.ng", "clapping"))
# <re.Match object; span=(4, 8), match='ping'>
# >>> print(re.search(r"p.ng", "sponge"))
# <re.Match object; span=(1, 5), match='pong'>
# 
# >>> print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
# <re.Match object; span=(0, 4), match='Pang'>
# 
# >>> print(re.search(r"[Pp]ython", "Python"))
# <re.Match object; span=(0, 6), match='Python'>
# 
# >>> print(re.search(r"[a-z]way", "The end of the highway"))
# <re.Match object; span=(18, 22), match='hway'>
# 
# >>> print(re.search(r"[a-z]way", "What a way to go"))
# None
# 
# >>> print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
# <re.Match object; span=(0, 6), match='cloudy'>
# >>> print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
# <re.Match object; span=(0, 6), match='cloud9'>
# 
# >>> print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
# <re.Match object; span=(4, 5), match=' '>
# 
# >>> print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# <re.Match object; span=(30, 31), match='.'>
# 
# >>> print(re.search(r"cat|dog", "I like cats."))
# <re.Match object; span=(7, 10), match='cat'>
# 
# >>> print(re.search(r"cat|dog", "I love dogs!"))
# <re.Match object; span=(7, 10), match='dog'>
# 
# >>> print(re.search(r"cat|dog", "I like both dogs and cats."))
# <re.Match object; span=(12, 15), match='dog'>
# 
# >>> print(re.findall(r"cat|dog", "I like both dogs and cats."))
# ['dog', 'cat']
# 
# >>> print(re.search(r"Py.*n", "Pygmalion"))
# <re.Match object; span=(0, 9), match='Pygmalion'>
# 
# >>> print(re.search(r"Py.*n", "Python Programming"))
# <re.Match object; span=(0, 17), match='Python Programmin'>
# 
# >>> print(re.search(r"Py[a-z]*n", "Python Programming"))
# <re.Match object; span=(0, 6), match='Python'>
# 
# >>> print(re.search(r"Py[a-z]*n", "Pyn"))
# <re.Match object; span=(0, 3), match='Pyn'>
# 
# >>> print(re.search(r"o+l+", "goldfish"))
# <re.Match object; span=(1, 3), match='ol'>
# 
# >>> print(re.search(r"o+l+", "woolly"))
# <re.Match object; span=(1, 5), match='ooll'>
# 
# >>> print(re.search(r"o+l+", "boil"))
# None
# 
# >>> print(re.search(r"p?each", "To each their own"))
# <re.Match object; span=(3, 7), match='each'>
# 
# >>> print(re.search(r"p?each", "I like peaches"))
# <re.Match object; span=(7, 12), match='peach'>
# 
# 
# >>> print(re.search(r".com", "welcome"))
# <re.Match object; span=(2, 6), match='lcom'>
# 
# >>> print(re.search(r"\.com", "welcome"))
# None
# 
# >>> print(re.search(r"\.com", "mydomain.com"))
# <re.Match object; span=(8, 12), match='.com'>
# 
# >>> print(re.search(r"\w*", "This is an example"))
# <re.Match object; span=(0, 4), match='This'>
# 
# >>> print(re.search(r"\w*", "And_this_is_another"))
# <re.Match object; span=(0, 19), match='And_this_is_another'>
# 
# >>> print(re.search(r"A.*a", "Argentina"))
# <re.Match object; span=(0, 9), match='Argentina'>
# 
# >>> print(re.search(r"A.*a", "Azerbaijan"))
# <re.Match object; span=(0, 9), match='Azerbaija'>
# 
# >>> print(re.search(r"^A.*a$", "Azerbaijan"))
# None
# 
# >>> print(re.search(r"^A.*a$", "Australia"))
# <re.Match object; span=(0, 9), match='Australia'>
# 
# >>> pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# 
# >>> print(re.search(pattern, "_this_is_a_valid_variable_name"))
# <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
# 
# >>> print(re.search(pattern, "this isn't a valid variable"))
# None
# 
# >>> print(re.search(pattern, "my_variable1"))
# <re.Match object; span=(0, 12), match='my_variable1'>
# 
# >>> print(re.search(pattern, "2my_variable1"))
# None
# 
# >>> result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
# >>> print(result)
# <re.Match object; span=(0, 13), match='Lovelace, Ada'>
# 
# >>> print(result.groups())
# ('Lovelace', 'Ada')
# 
# >>> print(result[0])
# Lovelace, Ada
# 
# >>> print(result[1])
# Lovelace
# >>> print(result[2])
# Ada
# 
# >>> "{} {}".format(result[2], result[1])
# 'Ada Lovelace'
# 
# >>> def rearrange_name(name):
# ...     result = re.search(r"^(\w*), (\w*)$", name)
# ...     if result == None:
# ...         return name
# ...     return "{} {}".format(result[2], result[1])
# ... 
# 
# >>> rearrange_name("Lovelace, Ada")
# 'Ada Lovelace'
# 
# >>> rearrange_name("Richie, Dennis")
# 'Dennis Richie'
# 
# >>> rearrange_name("Hopper, Grace M.")
# 'Hopper, Grace M.'
 
def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])
 
# >>> def rearrange_name(name):
# ...     result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
# ...     if result == None:
# ...         return name
# ...     return "{} {}".format(result[2], result[1])
# 
# >>> rearrange_name("Hopper, Grace M.")
# 'Grace M. Hopper'
# 
# >>> print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# <re.Match object; span=(2, 7), match='ghost'>
# 
# >>> print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# <re.Match object; span=(2, 7), match='scary'>
# 
# >>> print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']
# 
# >>> print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
# ['scary', 'ghost']
# 
# >>> print(re.findall(r"\w{5,10}", "I really like strawberries"))
# ['really', 'strawberri']
# 
# >>> print(re.findall(r"\w{5,}", "I really like strawberries"))
# ['really', 'strawberries']
# 
# >>> print(re.search(r"s\w{,20}", "I really like strawberries"))
# <re.Match object; span=(14, 26), match='strawberries'>
 
import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

# >>> import re
# >>> log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# >>> regex = r"\[(\d+)\]"
# >>> result = re.search(regex, log)
# >>> print(result[1])
# 12345
# 
# >>> result = re.search(regex, "A completely different string that also has numbers [34567]")
# >>> print(result[1])
# 34567
# 
# >>> result = re.search(regex, "99 elephants in a [cage]")
# >>> print(result[1])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'NoneType' object is not subscriptable
# 
# >>> def extract_pid(log_line):
# ...     regex = r"\[(\d+)\]"
# ...     result = re.search(regex, log_line)
# ...     if result is None:
# ...         return None
# ...     return result[1]
# ...
# 
# >>> print(extract_pid(log))
# 12345
# 
# >>> print(extract_pid("99 elephants in a [cage]"))
# 
# >>> re.split(r"[.?!]", "One sentence. Another one? And the last one!")
# ['One sentence', ' Another one', ' And the last one', '']
# 
# >>> re.split(r"([.?!])", "One sentence. Another one? And the last one!")
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
# 
# >>> re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
# 'Received an email for [REDACTED]'
# 
# >>> re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# 'Ada Lovelace'

