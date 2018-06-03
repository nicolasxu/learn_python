03-yield_example

# A Python version of Unix 'tail -f'

import time
def follow(thefile):
	thefile.seek(0,2) # Go to the end of the file
 	while True:
 	line = thefile.readline()
 	if not line:
 		time.sleep(0.1) # Sleep briefly
 		continue
 	yield line

# Example use : Watch a web-server log file
logfile = open("access-log")
for line in follow(logfile):
 	print line,