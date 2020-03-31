#!/bin/bash

meeting_info=$(zenity --forms \
    --title 'Meeting' --text 'Reminder information' \
    --add-calendar 'Date' --add-entry 'Title' \
    --add-entry 'Emails' \
    2>/dev/null)
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "$meeting_info"
fi
