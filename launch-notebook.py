#!/usr/bin/env python

import argparse
from subprocess import Popen
import os
import hashlib
import codecs
from shutil import copyfile
from getpass import getpass

port_pids = {}
script_dir = os.path.dirname(os.path.realpath(__file__))
notebooks_dir = os.path.expanduser('~')
ipython_dir = os.path.expanduser('~') + '/.ipython'
email_prompt = True

def init_notebook(user):
	fprof = '{}/profile_{}/ipython_notebook_config.py'.format(ipython_dir, user)
	if not os.path.isfile(fprof):
		os.makedirs('{}/profile_{}'.format(ipython_dir, user), mode=0o777, exist_ok=True)
		copyfile('ipython_notebook_config_template.py', fprof)
		return True
	else: print('profile for {} already exists.'.format(user))
	return False
def write_pwd(user, password):
	h = hashlib.sha1()
	h.update(password.encode())
	salt = codecs.encode(os.urandom(10), 'hex_codec')
	h.update(salt)
	enc_pwd = h.hexdigest()
	
	fprof = '{}/profile_{}/ipython_notebook_config.py'.format(ipython_dir, user)
	prof = [l for l in open(fprof, 'r+')]
	with open(fprof, 'w') as f:
		for l in prof:
			if 'c.NotebookApp.password' in l:
				l = ''.join(["c.NotebookApp.password = u'sha1:",  salt.decode(), ':', enc_pwd, "'"])
				pass_set = True
			f.write(l)
def init_all(emails=[], port=9005, pwd='random'):
	# Initialize vars for email sending
	sender, smtp_user, smtp_pwd = '', '', ''
	if email_prompt and input("Do you wish to send conf. emails? [y/n]: ") == 'y':
		sender = input("sender address (default hugo.muriel@unine.ch): ") or 'hugo.muriel@unine.ch'
		smtp_user = input("smtp username (default murielh): ") or 'murielh'
		smtp_pwd = getpass("smtp password: ")
	# Create a notebook for each user
	for email in emails:
		u = email.split('@').pop(0)
		init = init_notebook(u)
		if pwd != 'random': 
			# set the password
			write_pwd(u, pwd)
		if pwd == 'random' and init:
			# new notebook, set random pwd
			pwd = codecs.encode(os.urandom(2), 'hex_codec').decode()
			write_pwd(u, pwd)
		if port in port_pids: 
			Popen(["kill", str(port_pids[port])])
			print("Freeing port {}, killing process {}".format(port, port_pids[port]))
			del port_pids[port]
		process = Popen(["ipython3", "notebook", "--profile={}".format(u), "--port={}".format(port), "--no-mathjax", "--no-browser", "--port-retries=0", "--notebook-dir={}/{}".format(notebooks_dir, u), "--ip=130.125.78.14"])
		if process.pid:
			port_pids[port] = process.pid
			if pwd != 'random' and sender and smtp_user and smtp_pwd:
				# send conf. email for new notebooks or for password changes.
				sendemail_conf('http://eduinfo.unine.ch:{}/'.format(port), pwd, sender, email, smtp_user, smtp_pwd)
			print('process', process.pid)
		port += 1
	with open(script_dir + '/ipython-process.data', 'w+') as f:
		for p, pid in port_pids.items(): f.write('{},{}\n'.format(p, pid))
def kill_all():
	for p, pid in port_pids.items():
		Popen(["kill", str(port_pids[p])])
		print("Freeing port {}, killin process {}".format(p, port_pids[p]))
	open(script_dir + '/ipython-process.data', 'w').close()
def sendemail_conf(nb_url, nb_pwd, sender, to, smtp_user, smtp_pwd):
	import smtplib
	from email.mime.text import MIMEText
	msg = MIMEText('''
	Bonjour,
	
	Un notebook pour le cours de programmation a été créé pour vous, les détails ci-dessous.

	url: {}
	mot de passe: {}
	'''.format(nb_url, nb_pwd), 'plain')
	msg['Subject'] = 'Création notebook'
	msg['From'] = sender
	msg['To'] = to
	# use unine's smtp with starttls
	s = smtplib.SMTP('smtp.unine.ch')
	# s.set_debuglevel(True)
	s.starttls()
	s.login(smtp_user, smtp_pwd)
	s.sendmail(sender, to, msg.as_string())
	s.quit()
if __name__ == '__main__':
	open(script_dir + '/ipython-process.data', 'a').close()
	port_pids = {int(p.split(',').pop(0)):int(p.split(',').pop(1).strip()) for p in open(script_dir + '/ipython-process.data')} 
	
	parser = argparse.ArgumentParser(description='Notebook Launcher.')
	sparser = parser.add_subparsers(help='Commands', dest='command')
	parserInit = sparser.add_parser('init-user', help='It launches a notebook for a user with initialization if necessary.')
	parserInit.add_argument('-e', '--user-email', type=str, required=True, help='user email')
	parserInit.add_argument('-p', '--port', type=int, required=True, help='local port for the notebook')
	parserInit.add_argument('--notebooks-dir', type=str, required=True, help='notebooks directory, defaults to user\'s home dir.')
	parserInit.add_argument('--ipython-dir', type=str, required=False, help='ipython directory, defaults to user\'s home dir.')
	parserInit.add_argument('-pwd', '--password', type=str, required=False, help='password')
	parserInit.add_argument('--no-email', action='store_true', help='do not prompt to send conf. email')
	parserInitAll = sparser.add_parser('init-all-users', help='It launches notebooks for all users from a list of email addresses.')
	parserInitAll.add_argument('--notebooks-dir', type=str, required=True, help='notebooks directory, defaults to user\'s home dir.')
	parserInitAll.add_argument('--ipython-dir', type=str, required=False, help='ipython directory, defaults to user\'s home dir.')
	parserInitAll.add_argument('--emails-file', type=str, required=True, help='file with email adresses, one per line')
	parserInitAll.add_argument('--no-email', action='store_true', help='do not prompt to send conf. email')
	parser.add_argument('--stop-all', action='store_true', help='stop all running notebooks')
	args = parser.parse_args()
	if args.command == 'init-all-users': 
		notebooks_dir = args.notebooks_dir
		if args.ipython_dir: ipython_dir = args.ipython_dir
		# Read text file with email addresses
		init_all([e.strip() for e in open(args.emails_file)])
	if args.stop_all: 
		kill_all()
	if args.no_email: email_prompt = False
	if args.command == 'init-user':
		notebooks_dir = args.notebooks_dir
		if args.ipython_dir: ipython_dir = args.ipython_dir
		init_all([args.user_email], args.port, args.password if args.password else 'random')
