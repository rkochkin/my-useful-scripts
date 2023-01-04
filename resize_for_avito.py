#!/usr/bin/python3

import os
import glob
import subprocess

for path in glob.glob('./*'):
	if not os.path.isdir(path):
		continue
	print(path)

	if not os.path.exists(path+'/conv'):
		os.makedirs(path+'/conv')

	for photo_path in (glob.glob(path+'/*.jpg') + glob.glob(path+'/*.jpeg')):
		#print('  ' + photo_path)
		conv_path = path + '/conv/' + os.path.basename(photo_path)
		if not os.path.exists(conv_path):
			print('     run resize: ' + photo_path + ' -> ' + conv_path)
			process = subprocess.Popen(['convert', photo_path, '-resize', '1280x960', conv_path],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
			stdout, stderr = process.communicate()
			if len(stderr):
				print(stderr)
