import os

base_dir = '/var/imi/prog/notebooks'
# inside de base_dir
target_dir = 'all'
# open target dir
os.chdir('/'.join([base_dir, target_dir]))

for nbdir in os.listdir(base_dir):
	# Read each subdir except for the target_dir
	if nbdir == target_dir: continue
	print(nbdir)
	for f in os.listdir('/'.join([base_dir, nbdir])):
		if f.endswith('.ipynb'):
			link, target = '_'.join([nbdir, f]), '/'.join(['..', nbdir, f])
			if not os.path.isfile(link): 
				print("create symlink {} to {}".format(link, target))
				os.symlink(target, link)
# Remove invalid symlinks
for f in os.listdir('.'):
	if not os.path.isfile(f): 
		print("removing {}".format(f))
		os.remove(f)
