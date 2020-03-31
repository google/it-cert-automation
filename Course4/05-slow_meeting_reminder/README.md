## Example 5: Slow Meeting Reminder

This example shows a program that contains an expensive loop, making it take
quite long when the input CSV file is long and the list of receivers of the
reminder is also long.

You can trigger the issue by calling:

```
./send_reminders.py "2020-01-13|Example|test1,test2,test3,test4,test5"
```

The `orig` directory contains the initial code without any fixes.  The `fixed`
directory contains the code after applying the fixes shown in the video.

