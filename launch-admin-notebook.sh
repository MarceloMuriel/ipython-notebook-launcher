#!/bin/bash
/usr/bin/python3 /usr/local/bin/ipython3 notebook --profile=nbprog --port=8999 --no-browser --notebook-dir=/var/imi/prog/notebooks/nbprog --ip=130.125.78.14 &
/usr/bin/python3 /usr/local/bin/ipython3 notebook --profile=nbprog --port=8998 --no-browser --notebook-dir=/var/imi/prog/notebooks/all --ip=130.125.78.14 &
# Launch it with a user who only has read permissions.
#/usr/bin/python3 /usr/local/bin/ipython3 notebook --profile=nbprog_read --port=9000 --no-browser --notebook-dir=/var/imi/prog/notebooks/nbprog --ip=130.125.78.14 &
