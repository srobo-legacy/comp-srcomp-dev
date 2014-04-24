#!/usr/bin/env python

import cgi
from flask import url_for, request, redirect, jsonify, send_from_directory
import os
import sys
from time import time

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH + "/http/")

from app import app

def tweak_api_root(page):
    page = page.replace("var API_ROOT = '/comp-api';",
                        "var API_ROOT = '';")
    return page

#@app.route("/state")
def state_label():
    return jsonify(state=time())

# Directly setting it seems to be the only way to override it
for rule in app.url_map.iter_rules():
    if rule.rule == "/state":
        app.view_functions[rule.endpoint] = state_label

@app.route("/screens")
def screen():
    """An arena screen (dev only)"""
    return redirect("/screens/arena.html")

@app.route("/screens/<path:filename>")
def screens(filename):
    return send_from_directory("{}/screens".format(PATH), filename)

@app.route("/shepherding")
def shepherding():
    """A shepherding view (dev only)"""
    page = open(PATH + '/shepherding/index.html').read()
    page = tweak_api_root(page)
    return page

@app.route("/")
def site_map():
    """Print available functions (dev only)"""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__

    page = """<html><head><title>Comp API</title></head><body>
    <h2>Comp API</h2>
    <ul>"""
    for endpoint, description in func_list.items():
        endpoint = str(endpoint)
        escaped = cgi.escape(endpoint)
        if escaped == endpoint:
            # link it
            item = '<a href=".{0}">{0}</a>'.format(endpoint)
        else:
            item = escaped
        if description is not None:
            item += ": " + description
        page += "<li>{0}</li>".format(item)
    page += "</ul></body></html>"
    return page

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
