# Author: Gil Cukierman
# gil.cukierman (at) gmail.com
# Creation Date: 5/18/15
# (c) All Rights Reserved

import os
import sys
import shutil
from sets import Set

def IsolateUnique(filename):
	part1 = filename.split('[')[1]
	part2 = part1.split(']')[0]

	return part2 

# Grab the path to our top level directory
base_dir = sys.argv[1]

parent_dir = os.path.join(os.path.dirname(base_dir), os.pardir)
print parent_dir

all_files = os.listdir(base_dir)

# a set of all unique filenames
file_set = Set()

print "isolating batches..."
# Get all unique batch names
for filename in all_files:
	if filename.endswith('.tif') or filename.endswith('.tiff'):
		isolated = IsolateUnique(filename)
		file_set.add(isolated)

if base_dir[-1] == os.sep:
	base_dir = base_dir[:-1]
new_dir = os.path.join(parent_dir,os.path.basename(base_dir) + ' Batches')
print base_dir
print new_dir
os.makedirs(new_dir)

print "making batch folders..."
# Create a folder for each unique batch name
for filename in file_set:
	os.makedirs(os.path.join(new_dir,filename))

print "copying images into batch folders..."
# Now iterate through the top level directory again, copying to respective files
count = 1
for filename in all_files:
	sys.stdout.write("\r Percent Completed: %f" % (float(count)/len(all_files) * 100))
	sys.stdout.flush()
	count+=1
	if filename.endswith('.tif') or filename.endswith('.tiff'):
		isolated = IsolateUnique(filename)
		# status update
		# we don't want to copy the im3 files...
		shutil.copy(os.path.join(base_dir,filename), os.path.join(new_dir,isolated,filename))

print "Success! Batches Made."