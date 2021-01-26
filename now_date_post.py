#!/usr/bin/env python3
# Update to `now` the date of a post
# sintax: ./now_date_post.sh "post_filename"

from sys import argv
import os.path
import subprocess

if len(argv) == 1:
	print("""Update to `now` the date of a post\n\
 sintax: ./now_date_post.sh "post_filename""")
	exit(0)

filename=argv[1]

# file exists?
if not os.path.isfile(filename):
	print("File",filename,"does not exists.")
	exit(1)

name=os.path.basename(filename)
if name[4] != '-' or name[7] != '-' or name[10] != '-':
	print("File",filename,"does not seem a valid post.")
	exit(1)
def get_date():
	res=subprocess.run(["date","+%F"],capture_output=True).stdout.decode()[:-1]
	return res
def get_timedate():
	res=get_date()
	res=res+" "+subprocess.run(["date","+%X"],capture_output=True).stdout.decode()[:-1]
	res=res+" "+subprocess.run(["date","+%z"],capture_output=True).stdout.decode()[:-1]
	return res
new_filename=os.path.dirname(filename)+"/"+get_date()+name[10:]

with open(filename,"r") as f:
	lines=f.readlines()
if len(lines)<6 or lines[3][:5] != "date:":
	print("File",filename,"does not seem a valid post.")
	exit(1)

lines[3]="date:   "+get_timedate()+"\n"


with open(new_filename,"w") as f:
	f.writelines(lines)

if filename != new_filename:
	subprocess.run(["rm",filename])

	

