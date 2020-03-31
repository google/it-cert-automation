## Example 2: Application that crashes only in some cases

This example shows a date formatting issue that causes an application to crash.

In order to trigger the issue, the `LANG` environment variable needs to be set
to `en_US.UTF-8`.

```
export LANG=en_US.UTF-8
./meeting_reminder.sh
```

The problem happens when sending a reminder for any day of the month larger
than 12.

The `orig` directory contains the initial code without any fixes.  The `fixed`
directory contains the code after applying the fixes shown in the videos.

