
#import os
# Get execution directory
#print(os.getcwd())
# Get complete file path
#print( os.path.abspath(__file__))

# get current folder path 
#import pathlib
#filepath = pathlib.Path(__file__).resolve().parent

print(filepath);

filename = "classSample.py"

file = open(filename)

# read entire file
print (file.read())

# read line
#print( file.readline())
#print( file.readline())

# iterate through line
#for line in file:
#	print (line)


file.close()