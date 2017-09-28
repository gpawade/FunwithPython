
# dict hash table

mDict = {}

mDict["a"] = "one"
mDict["b"] = "two"

print(mDict)
print(mDict.values())
print(mDict.keys())

print(mDict["a"])


# Exist condition
print("# Loop")
if "a" in mDict:
    print ("key exist")

if "one" in mDict.values():
    print( "value exist")

# for loop
print("# For Loop")

## note keys are in random order
for key in mDict:
    print(key + " " + mDict[key])

# Exactly same as above
for key in mDict.keys():
    print(key + " " + mDict[key])
    
## iteration
print("# item iteration")
for k,v in mDict.items():
    print(k + ": " + v)

## dict formatting

str = '%(a)s : %(b)s' % mDict
print(str)

## del
del mDict["a"]
print (mDict)