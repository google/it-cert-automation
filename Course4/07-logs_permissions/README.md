## Example 7: Crashing Webserver

This example shows a webserver that's generating an Internal Server Error.

The `setup.sh` script sets up the webserver. This is done by installing a bunch
of Debian packages. The exact list of packages might change depending on the
version of Debian or Ubuntu being used. We don't recommend running this on a
local machine. Instead, if you want to try this example out, run this in a
virtual machine. **Make sure you understand what the `setup.sh` script does
before running it**.

Once you have the webserver running, you can connect to it with a browser and
try to access the `/logs` URL to see the error message.

