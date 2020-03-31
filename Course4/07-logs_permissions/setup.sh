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

# We are going to generate some log entries using the apache benchmark
# tool
sudo apt install -y apache2-utils

# Add the example virtual host to the hosts file
if ! grep -q site.example.com /etc/hosts; then
    echo '127.0.2.1 site.example.com' | sudo tee -a /etc/hosts
fi

# Add the nginx configuration file for the example site
sudo cp site.example.com.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/site.example.com.conf /etc/nginx/sites-enabled/

# Create the root path for the example site
sudo mkdir -p /var/www/site.example.com

# Add the uwsgi configuration file for the example site
sudo cp site.example.com.ini /etc/uwsgi/apps-available/
sudo ln -s /etc/uwsgi/apps-available/site.example.com.conf /etc/uwsgi/apps-enabled/

# Add a user for the example site
sudo adduser --force-badname --system --home /srv/site.example.com --group --disabled-password site.example.com

# Add the uwsgi site to the site user home
sudo cp -r . /srv/site.example.com/

# Create the log file by hand:
sudo touch /var/log/site.example.com.log
sudo chown site.example.com:site.example.com /var/log/site.example.com.log
sudo chmod 640 site.example.com:site.example.com /var/log/site.example.com.log

sudo systemctl restart nginx
sudo systemctl restart uwsgi

# Generate some log entries, just to avoid dealing with an empty file
ab -n 1000 site.example.com/stats

# Add a logrotate file for the example site
sudo cp site.example.com.logrotate /etc/logrotate.d/

# do a useless rotation so the status is updated
sudo /usr/sbin/logrotate -v /etc/logrotate.conf

# Trick logrotate
DATE=$(date --date="2 days ago" "+%Y-%-m-%-d-0:0:0")
sudo sed -i '/.var.log.site\.example\.com\.log/s/ [^ ]*$/ '"$DATE"'/' /var/lib/logrotate/status

# do a rotation
sudo /usr/sbin/logrotate -v /etc/logrotate.conf

# Generate some log entries, just to avoid dealing with an empty file
ab -n 1000 site.example.com/stats

# Now accessing to site.example.com/logs should fail with an error 500
