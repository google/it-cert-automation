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


import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)


# Run the tests
unittest.main()
