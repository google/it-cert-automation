#!/usr/bin/env python3
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

