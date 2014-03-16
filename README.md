sr-comp-dev
===========

Development wrapper to the SRComp suite of Competition software.

This is a wrapper which makes it easier to develop things.
No real code should be in here.

See https://www.studentrobotics.org/trac/wiki/Competition/Software for a
rough guide on the overall aims.

## Run with
`./app.py`

Serves the competition API plus some related pages (so they don't need
to worry about having XSS issues) at http://localhost:5112.

## Test with
`./run-all-tests`

Recursively looks for files called `run-tests`, and then tries to
run them in their own directories. Bails after the first failure.
