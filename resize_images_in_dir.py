#!/usr/bin/python3

import os
import glob
import subprocess


if not os.path.exists('./conv'):
	os.makedirs('./conv')

for photo_path in (glob.glob('*.jpg') + glob.glob('*.jpeg') + glob.glob('*.JPG')):
	print('  ' + photo_path)
	conv_path = './conv/' + os.path.basename(photo_path)
	if not os.path.exists(conv_path):
		print('     run resize: ' + photo_path + ' -> ' + conv_path)
		process = subprocess.Popen(['convert', photo_path, '-resize', '1280x960', conv_path],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
		stdout, stderr = process.communicate()
		if len(stderr):
			print(stderr)

