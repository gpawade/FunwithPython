import re

print(__name__)

def main():
	print("hello from main!")


# Match
phone = "123-345-6789"
groupsMatch = re.match(r"(\d{3})-\d{3}-\d{3}",phone)

print(groupsMatch.group(0))
print(groupsMatch.group(1))

# Search
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print (match.group())  ## 'alice-b@google.com'


# Group Extraction
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
	print( match.group())   ## 'alice-b@google.com' (the whole match)
	print (match.group(1))  ## 'alice-b' (the username, group 1)
	print( match.group(2))  ## 'google.com' (the host, group 2)


# Find All

# Suppose we have a text with many email addresses
str1 = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str1) ## ['alice@google.com', 'bob@abc.com']
print(emails)
for email in emails:
	# do something with each found email string
	print (email)


# findall With Files
# Open file
# f = open('test.txt', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
# strings = re.findall(r'some pattern', f.read())


# Substitution 

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
