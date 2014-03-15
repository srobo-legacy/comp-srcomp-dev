#!/usr/bin/env python

import os
import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH + "/http/")

from app import app

@app.route("/screen")
def screen():
    return open(PATH + '/screens/screen.html').read()

@app.route("/shepherding")
def shepherding():
    return open(PATH + '/shepherding/index.html').read()

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description = "SR Competition info Development API HTTP server")
    parser.add_argument("-c", "--compstate", default=PATH + '/compstate',
                        help = "Competition state git repository path")
    parser.add_argument("-p", "--port", type=int, default=5112,
                        help = "Port to listen on")
    args = parser.parse_args()

    app.config["COMPSTATE"] = args.compstate
    app.debug = True
    app.run(host='0.0.0.0', port=args.port)
