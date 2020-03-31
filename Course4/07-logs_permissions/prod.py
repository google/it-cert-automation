#!/usr/bin/env python3
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


import bottle

LOGFILE = '/var/log/site.example.com.log'

@bottle.route('/')
def start():
    return f'<html>' \
            '<head><title>/</title></head>' \
            '<body>Hello /</body>' \
            '</html>'


@bottle.route('/<something>')
def something(something):
    return f'<html>' \
        f'<head><title>{something}</title></head>' \
        f'<body>Hello {something}</body>' \
        f'</html>'


@bottle.route('/logs')
def logs():
    with open(LOGFILE) as f:
        return f'<html>' \
            f'<head><title>Logs</title></head>' \
            f'<body><pre>{f.read()}</pre></body>' \
            f'</html>'


app = bottle.default_app()
