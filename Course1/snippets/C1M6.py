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

# Sorting
# -------

# Interactive code snippet
# >>> numbers = [ 4, 6, 2, 7, 1 ]
# >>> numbers.sort()
# >>> print(numbers)
# [1, 2, 4, 6, 7]
#
# >>> names = ["Carlos", "Ray", "Alex", "Kelly"]
#
# >>> print(sorted(names))
# ['Alex', 'Carlos', 'Kelly', 'Ray']
#
# >>> print(names)
# ['Carlos', 'Ray', 'Alex', 'Kelly']
#
# >>> print(sorted(names, key=len))
# ['Ray', 'Alex', 'Kelly', 'Carlos']

# Code for the example project
# ----------------------------

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

