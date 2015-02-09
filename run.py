try:
    import sr.comp
except ImportError:
    print("No srcomp detected. Did you activate the virtualenv?")
    print("$ source venv/bin/activate")
    exit(1)

import cherrypy
import argparse
import os.path
import threading
import subprocess
import time
from sr.comp.http import app

parser = argparse.ArgumentParser()
parser.add_argument('compstate', help='path to compstate repo')
args = parser.parse_args()

app.config['COMPSTATE'] = args.compstate

# Run streams thread
def run_streams():
    # Hack, pending a better solution to determining whether
    # cherrypy has actually started yet.
    time.sleep(3)
    subprocess.check_call(('node', 'main.js'),
                          cwd='srcomp-stream')
thr = threading.Thread(name='streams', target=run_streams)
thr.daemon = True
thr.start()

cherrypy.tree.graft(app, '/comp-api')

config={
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.realpath('srcomp-screens')
    },
    'global': {
        'server.socket_host': '::',
        'server.socket_port': 5112,
        'server.thread_pool': 8
    }
}
cherrypy.quickstart(config=config)

