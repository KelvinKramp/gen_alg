#!/bin/sh
pip freeze > requirements.txt
git rm -r --cached .
git add .
git commit -am "update"
git push origin master