#!/bin/sh
python generate-known-using.py
git add .
git commit -m "update"
git push --force
