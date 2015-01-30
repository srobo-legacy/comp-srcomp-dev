#!/bin/bash
if [ -f ~/.ssh/config ]; then
    GERRIT=$(grep -m 1 -B 5 29418 ~/.ssh/config | grep -E '^Host ' | tail -1 | sed 's/Host //')
    GITHUB=$(grep -m 1 -B 5 'github.com' ~/.ssh/config | grep -E '^Host ' | tail -1 | sed 's/Host //')
fi

if [ -n "$GERRIT" ]; then
    echo "Detected GERRIT as $GERRIT"
    function clone_srobo {
        git clone $GERRIT:$1 $2
    }
else
    function clone_srobo {
        git clone ssh://studentrobotics.org:29418/$1 $2
    }
fi
if [ -n "$GITHUB" ]; then
    echo "Detected GITHUB as $GITHUB"
    function clone_gh {
        git clone $GITHUB:$1 $2
    }
else
    function clone_gh {
        git clone https://github.com/$1 $2
    }
fi

for POSSIBLE_PYTHON in python3 python;
do
    PYTHON=$(which $POSSIBLE_PYTHON)
    $POSSIBLE_PYTHONS --version 2>&1 | grep 'Python 3\.' >/dev/null
    if [ $? -ne 0 ]; then
        echo "Found Python: $PYTHON"
        break
    fi
done
if [ -z "$PYTHON" ]; then
    echo "No Python installation found."
    exit 1
fi

set -e
$PYTHON -m venv venv
source venv/bin/activate
set -v
pip install -r requirements.txt
clone_srobo comp/ranker.git ranker
clone_srobo comp/srcomp.git srcomp
clone_srobo comp/srcomp-http.git srcomp-http
clone_srobo comp/srcomp-screens.git srcomp-screens
clone_srobo comp/dummy-comp.git dummy-comp
clone_srobo comp/srcomp-scorer.git srcomp-scorer
clone_gh prophile/srcomp-stream.git srcomp-stream
cd ranker
    python setup.py develop
cd ..
cd srcomp
    python setup.py develop
cd ..
cd srcomp-http
    python setup.py develop
cd ..
cd srcomp-scorer
    python setup.py develop
cd ..
cd srcomp-screens
    git checkout rewrite
    bower install
cd ..
cd srcomp-stream
    sed 's_SRCOMP: .*_SRCOMP: "http://localhost:5112"_' <config.coffee.example >config.coffee
    npm install
cd ..
set +v
echo "-- DONE SETUP --"
echo "Usage: "
echo "  (1) Activate the virtualenv: source venv/bin/activate"
echo "  (2) Run things"

