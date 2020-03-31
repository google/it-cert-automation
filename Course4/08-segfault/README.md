## Example 8: Code that crashes with a segmentation fault

The code in this directory is a very simple C program.  This program crashes
with a segmentation fault when executed.

You can build and run the program with:

```
make
./example 
```

To get a coredump, run:
```
ulimit -c unlimited
./example 
```

Then debug the failure with:
```
gdb -c core example
```

