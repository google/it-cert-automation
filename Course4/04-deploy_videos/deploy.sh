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


# The videos need to be in the mp4 format in order to serve them
# in the website.
#
# This scripts runs ffmpeg in parallel to convert all of the webm files to mp4.
echo "Starting video conversion"
for video in static/*.webm; do
    mp4_video="$(echo "$video" | sed 's/\.webm$/.mp4/')"
    daemonize -c $PWD /usr/bin/ffmpeg -nostats -nostdin -i "$video" "$mp4_video" #</dev/null &>/dev/null
done

