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


# The wsgi site uses python bottle
sudo apt install -y python3-bottle

# The webserver is nginx, and uses uwsgi to communicate with the python
# workers
sudo apt install -y nginx uwsgi uwsgi-plugin-python3

# We are going to obtain the state of our site using the apache benchmark
# tool
sudo apt install -y apache2-utils

# The deploy uses ffmpeg to transcode the videos to webm
sudo apt install -y ffmpeg

# Add the example virtual host to the hosts file
echo '127.0.2.1 site.example.com' | sudo tee -a /etc/hosts

# Add the nginx configuration file for the example site
sudo cp site.example.com.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/site.example.com.conf /etc/nginx/sites-enabled/

# Reload nginx
sudo systemctl reload nginx

# Create the root path for the example site
sudo mkdir -p /var/www/site.example.com

# We need to obtain a number of videos, for example:
# cd static
# lftp https://meetings-archive.debian.net/pub/debian-meetings/2019/DebConf19/
# mget *.webm

# And to make the video names more generic we could use:
# i=0
# for name in *.webm; do
#     let i+=1
#     new_name="$(printf "%03d.webm\n" $i)"
#     mv "$name" "$new_name";
# done

# A real wsgi site would use emperor, in this example we can launch it by
# calling uwsgi
echo 'Run using ./run.sh'

# To measure the slowness in the site while the deploy is running we use:
echo 'Measure with: ab -n 500 site.example.com/ '

# The kernel fairness will take care of multiplying the time needed to serve
# the pages by the amount of ffmpegs running
