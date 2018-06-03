# 04-yield_example2


#Print all server log entries containing 'python'

def grep(pattern,lines):
 	for line in lines:
 	if pattern in line:
 		yield line
# Set up a processing pipe : tail -f | grep python
logfile = open("access-log")
loglines = follow(logfile)
pylines = grep("python",loglines)
# Pull results out of the processing pipeline
for line in pylines:
 	print line,