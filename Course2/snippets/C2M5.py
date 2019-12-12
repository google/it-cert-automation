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

# These are the snippets shown during the demo videos in C2M5
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

# >>> from rearrange import rearrange_name
# 
# >>> rearrange_name("Lovelace, Ada")
# 'Ada Lovelace'
# 
# >>> from validations import validate_user
# >>> validate_user("", -1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/user/validations.py", line 5, in validate_user
#     raise ValueError("minlen must be at least 1")
# ValueError: minlen must be at least 1
# 
# >>> validate_user("", 1)
# False
# >>> validate_user("myuser", 1)
# True
# 
# >>> validate_user(88, 1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/user/validations.py", line 7, in validate_user
#     if len(username) < minlen:
# TypeError: object of type 'int' has no len()
# 
# >>> validate_user([], 1)
# False
# 
# >>> validate_user(["name"], 1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/marga/validations.py", line 9, in validate_user
#     if not username.isalnum():
# AttributeError: 'list' object has no attribute 'isalnum'
# 
# 
# >>> from validations import validate_user
# 
# >>> validate_user([3], 1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/home/marga/validations.py", line 4, in validate_user
#     assert type(username) == str, "username must be a string"
# AssertionError: username must be a string

