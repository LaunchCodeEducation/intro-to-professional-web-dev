#! /bin/sh
rm -rf docs/*
sphinx-build -E -b html src docs
