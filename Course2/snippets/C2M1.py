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

# These are the snippets shown during the demo videos in C2M1
# Each snippet is followed by the corresponding output when executed in the
# Python interpreter.

# >>> import requests
# 
# >>> response = requests.get("http://www.google.com")
# 
# >>> len(response.text)
# 12014
# 
# >>> import arrow
# 
# >>> date = arrow.get('2020-01-18', 'YYYY-MM-DD')
# 
# >>> date.shift(weeks=+6).format('MMM DD YYYY')
# 'Feb 29 2020'
# 
# >>> import PIL.Image
# 
# >>> image = PIL.Image.open("houses.jpg")
# 
# >>> print(image.size)
# (4032, 3024)
# >>> print(image.format)
# JPEG
# 
# >>> import pandas
# 
# >>> visitors = [ 1523, 2398, 1367, 4732, 3627 ]
# 
# >>> errors = [ 23, 43, 54, 13, 65 ]
# 
# >>> df = pandas.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon","Tue","Wed","Thu","Fri"])
# 
# >>> print(df)
#      visitors  errors
# Mon      1523      23
# Tue      2398      43
# Wed      1367      54
# Thu      4732      13
# Fri      3627      65
# 
# >>> df["errors"].mean()
# 39.6
# 
# >>> import shutil
# >>> du = shutil.disk_usage("/")
# >>> print(du)
# usage(total=108352618496, used=52618924032, free=50206023680)
# >>> du.free/du.total*100
# 46.33577330837965
# 
# >>> import psutil
# >>> psutil.cpu_percent(0.1)
# 9.0
# 
# >>> psutil.cpu_percent(0.1)
# 23.8
# >>> psutil.cpu_percent(0.1)
# 15.8
# >>> psutil.cpu_percent(0.1)
# 20.0
# >>> psutil.cpu_percent(0.1)
# 38.1
# 
# >>> psutil.cpu_percent(0.5)
# 7.3
# >>> psutil.cpu_percent(0.5)
# 4.2
# >>> psutil.cpu_percent(0.5)
# 8.0
# 
# 

