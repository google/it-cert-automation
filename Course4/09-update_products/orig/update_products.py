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

import argparse
import csv
import sqlite3
import sys

def process_options():

    arg_parser = argparse.ArgumentParser(
        description='Update products CSV into the specified database')
    arg_parser.add_argument('--server', default='products')
    arg_parser.add_argument('filename', default='products.csv')
    args = arg_parser.parse_args()
    return args


def database_connection(name):

    db = sqlite3.connect(f'{name}.db', isolation_level='DEFERRED')
    cursor = db.cursor()

    # Check if the table is already present
    cursor.execute('''
        SELECT name FROM sqlite_master WHERE type='table' AND
            name='products'
    ''')
    if cursor.fetchone() is None:
        cursor.execute('''
            CREATE TABLE products
                (product_code, description)
        ''')

    return db

def update_data(database, options):

    with open(options.filename, 'r') as products:
        reader = csv.DictReader(products)
        cursor = database.cursor()
        for row in reader:
            print('Updating {} with value: {}'.format(
                row['product_code'], row['description']))
            cursor.execute('''
            INSERT OR REPLACE INTO products VALUES
                (:product_code, :description)
            ''', row)
        database.commit()
        print("Update successful")


def main():
    options = process_options()
    database = database_connection(options.server)
    update_data(database, options)

    return 0

if __name__ == "__main__":
    sys.exit(main())

