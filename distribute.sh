#!/usr/bin/sh
proj='dystic'
python3 setup.py bdist_wheel &&\
gpg2 --detach-sign -a dist/$proj-$1-py3-none-any.whl &&\
twine upload dist/$proj-$1-py3-none-any.whl dist/$proj-$1-py3-none-any.whl.asc &&\
mkdir dist/$1 &&\
mv dist/$proj-$1-* dist/$1 || "Failed"
