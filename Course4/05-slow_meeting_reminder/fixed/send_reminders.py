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


import csv
import datetime
import email
import smtplib
import sys


def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("invocation:")
    print("    send_reminders 'date|Meeting Title|emails' ")
    return 1


def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")


def message_template(date, title, name):
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
Hi {name}!

This is a quick mail to remind you all that we have a meeting about:
 "{title}"
the {weekday} {date}.

See you there.
''')
    return message

def read_names(contacts):
    names = {}
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            names[row[0]] = row[1]
    return names


def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP('localhost')
    names = read_names(contacts)
    for email in emails.split(','):
        name = names[email]
        message = message_template(date, title, name)
        message['From'] = 'noreply@example.com'
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    # TODO: make this configurable
    contacts = "contacts.csv"
    try:
        date, title, emails = sys.argv[1].split('|')
        send_message(date, title, emails, contacts)
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email: {}".format(e), file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
