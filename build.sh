#! /bin/bash

builder=html

key="$1"

case $key in
    -h|--help)
    cat <<EOF
Usage: ./build [-c | -w]
  -c  : Clean build
  -w  : Watch (incremental build on change)
EOF
    ;;
    -c|--clean)
    rm -rf docs/*
    sphinx-build -E -b "$builder" src docs
    ;;
    -w|--watch)
    sphinx-build -b "$builder" src docs
    fswatch -o ./src/ | xargs -n1 -I{} sphinx-build -b "$builder" src docs
    ;;
    *)
    sphinx-build -b "$builder" src docs
    ;;
esac
