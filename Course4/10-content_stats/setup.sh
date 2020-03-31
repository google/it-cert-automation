#!/bin/bash
# Copyright 2020 Google LLC
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


# For this example we are using the zimply modules, which are available using
# pip, so we are going to install it in a virtual env:
sudo apt install -y python3-virtualenv

# Create the virtualenv and install zimply
virtualenv -p /usr/bin/python3 .

# Enable the virtualenv
. bin/activate

# install zimply
pip install zimply

# We are also using beautifulsoup to convert the html contents to text
pip install bs4

# Using tqdm we could make the output a bit more friendly
pip install tqdm

# The data file we are using is a zim file from the wikipedia computer articles, 
# without pictures. This file is about 300 megabytes of data.
wget http://download.kiwix.org/zim/wikipedia_en_computer_nopic.zim -O data.zim

