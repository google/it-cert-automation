## Example 1: An application that crashes silently

This example shows a very simple program that fails to start because of a
configuration problem.

To run it, you need to install the following packages:
`python3-pyside2.qtwidgets`, `python3-pyside2.qtgui` and `qt5-style-plugins`,
or their equivalents in your installation.

You can run the program with:
```
./purplebox
```

It should fail without any messages.

You can use `strace` to figure out what's wrong:
```
strace ./purplebox
```

