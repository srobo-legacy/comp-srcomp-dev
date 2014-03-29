sr-comp-dev
===========

Development wrapper to the SRComp suite of Competition software.

This is a wrapper which makes it easier to develop things.
No real code should be in here.

See https://www.studentrobotics.org/trac/wiki/Competition/Software for a
rough guide on the overall aims.

**Warning:** This repo has several (at least four) layers of submodules.
Be sure you've got all them all checked out -- you'll get import errors
from most things, but there are also some symlinks which cross module
boundaries which will likely give other errors.

## Run with
`./app.py`

Serves the competition API plus some related pages (so they don't need
to worry about having XSS issues) at http://localhost:5112.

If you want to develop the srweb competition mode stuff, you'll need to
arrange for http://localhost/comp-api to be routed to the above, which
whatever you're using to serve srweb will probably be able to do.

## Test with
`./run-all-tests`

Recursively looks for files called `run-tests`, and then tries to
run them in their own directories. Bails after the first failure.
