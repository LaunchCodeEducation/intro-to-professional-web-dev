#! /bin/sh
rm -rf docs/*
sphinx-build -E -b html-a11y src docs
