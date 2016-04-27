SRcomp Development Script
=========================

This repository contains a script - `init.sh` - which builds an srcomp
development environment.

Specifically, when, run (via `python run.py $COMPSTATE`) it:

 * creates a virtualenv and configures it with external dependencies,
 * clones and configures the following repositories:
   * `ranker`, the game-points-to-league-points system;
   * `srcomp`, the core srcomp library;
   * `srcomp-http`, the srcomp REST API;
   * `srcomp-scorer`, the srcomp score entry system,
   * `srcomp-screens`, the repository containing the arena display HTML,
   * `srcomp-stream`, the system that streams events live,
   * `dummy-comp`, the standard testing compstate repository

It then emits instructions on how to use the virtualenv.

The HTTP API is exposed via <http://localhost:5112/comp-api/>, while the
screen pages are at:

 * <http://localhost:5112/arena.html>
 * <http://localhost:5112/outside.html>
 * <http://localhost:5112/shepherding.html>
 * <http://localhost:5112/staging.html>
