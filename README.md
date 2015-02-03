SRcomp Development Script
=========================

This repository contains a script—`init.sh`—which builds an srcomp
development environment.

Specifically, when, run it:

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

