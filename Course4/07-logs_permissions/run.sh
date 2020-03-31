#!/bin/sh
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


uwsgi \
    --plugin python3 \
    --socket 127.0.0.1:3031 \
    --wsgi-file prod.py \
    --callable app \
    --processes 4 \
    --threads 2 \
    --stats 127.0.0.1:9191 \
    --logto site_app.log

