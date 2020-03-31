## Example 3: Slow Webserver

This example shows a webserver that becomes slow because it's under severe load.

The `setup.sh` script sets up the webserver. This is done by installing a bunch
of Debian packages. The exact list of packages might change depending on the
version of Debian or Ubuntu being used.  We don't recommend running this on a
local machine. Instead, if you want to try this example out, run this in a
virtual machine. Make sure you understand what the `setup.sh` script does
before running it.

To see how the load is generated, you'll need to download videos and put them
in the `static` folder.

Once the machine is setup, you can start encoding videos using `deploy.sh` and
then run the webserver and using `run.sh`.

To measure the latency, you can use:

``` ab -n 500 site.example.com/ ```

This command is part of the Apache Bentchmark tool.
