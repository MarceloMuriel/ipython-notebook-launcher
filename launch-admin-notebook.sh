#!/bin/bash
ipython3 notebook --profile=nbprog --port=8999 --no-mathjax --no-browser --port-retries=0 --notebook-dir=/var/imi/prog/notebooks/nbprog --ipython-dir=/var/imi/prog/.ipython --ip=130.125.78.14 &
ipython3 notebook --profile=nbprog --port=8998 --no-mathjax --no-browser --port-retries=0 --notebook-dir=/var/imi/prog/notebooks/all --ipython-dir=/var/imi/prog/.ipython --ip=130.125.78.14 &
# Launch it with a user who only has read permissions.
#ipython3 notebook --profile=nbprog_read --port=9000 --no-mathjax --no-browser --port-retries=0 --notebook-dir=/var/imi/prog/notebooks/nbprog --ipython-dir=/var/imi/prog/.ipython --ip=130.125.78.14 &
