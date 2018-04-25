#! /bin/sh
python tools/prebuild.py
sphinx-build -a -b html src docs
python tools/postbuild.py