## Example 9: File stored with strange encoding

This example shows a program that crashes when the input file is stored with an
encoding different than the one originally expected.

To trigger the failure, run:

```
./update_products.py new_products.csv
```

To debug, you can add a `print()` line, or use the Python debugger:

```
pdb3 update_products.py new_products.csv
```

The `orig` directory contains the initial code without any fixes.  The `fixed`
directory contains the code after applying the fixes shown in the video.

