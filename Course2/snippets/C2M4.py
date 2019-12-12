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

# These are the snippets shown during the demo videos in C2M4
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

# >>> import subprocess
# >>> subprocess.run(["date"])
# Wed 05 Jun 2019 03:23:36 PM CEST
# CompletedProcess(args=['date'], returncode=0)
# 
# >>> subprocess.run(["sleep", "2"])
# CompletedProcess(args=['sleep', '2'], returncode=0)
# 
# >>> result = subprocess.run(["ls", "this_file_does_not_exist"])
# ls: cannot access 'this_file_does_not_exist': No such file or directory
# >>> print(result.returncode)
# 2
# 
# >>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# 
# >>> print(result.returncode)
# 0
# 
# >>> print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer google-public-dns-a.google.com.\n'
# 
# 
# >>> print(result.stdout.decode().split())
# ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'google-public-dns-a.google.com.']
# 
# 
# >>> result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
# 
# >>> print(result.returncode)
# 1
# 
# >>> print(result.stdout)
# b''
# >>> print(result.stderr)
# b"rm: cannot remove 'does_not_exist': No such file or directory\n"
# 

# Log file processing
# -------------------
# 
# >>> import re
# >>> pattern = r"USER \((\w+)\)$"
# 
# line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
# 
# >>> result = re.search(pattern, line)
# >>> print(result[1])
# naughty_user
# 
# >>> usernames = {}
# 
# >>> name = "good_user"
# 
# >>> usernames[name] = usernames.get(name, 0) + 1
# 
# >>> print(usernames)
# {'good_user': 1}
# 
# >>> usernames[name] = usernames.get(name, 0) + 1
# >>> print(usernames)
# {'good_user': 2}
# 
