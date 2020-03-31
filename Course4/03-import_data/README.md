## Example 3: A file with invalid data

This example shows a script that fails when one of the lines in the input file
contains invalid data. The `import.py` script receives the data to import using
standard input.  To trigger the error, run:

```
cat contacts.csv | ./import.py --server test
```

Using the `head` and `tail` commands, you can find the problematic line. Like this:

```
head -50 contacts.csv | tail -25 | ./import.py --server test
```

