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


# We are using the Open Images Dataset v5, test_challenge.zip file available:
# https://datasets.figure-eight.com/figure_eight_datasets/open-images/test_challenge.zip
# It's a 9.7 G file, with 99999 jpg files.

# The example scripts use pillow for the image processing and tqdm for the
# progress bar:
sudo apt install -y python3-pil python3-tqdm

