ipython-notebook-launcher
=========================

Launch multiple notebook instances for different users based on email addresses.

To create or launch a notebook for each email address found in a file emails.txt (one per line):
```bash
python3 launch-notebook.py init-all-users --emails-file emails.txt --notebooks-dir /path/to/notebooks
```
By default the first port starts at 9005 without retries, so if the port is busy the notebook is not launched. If the notebook profile is created then the password is set to a random value of 4 chars and emailed to the user if you select to.

To create or launch a notebook for a single user:
```bash
python3 launch-notebook.py init-user -e user@domain.ch -p 9005 --notebooks-dir /path/to/notebooks
```
If the notebook profile does not exist then it will be created with a random password to be emailed to the user.

To create or launch a notebook for a single user with a custom password:
```bash
python3 launch-notebook.py init-user -e user@domain.ch -p 9005 -pwd PASSWORD --notebooks-dir /path/to/notebooks
```
