arr =[1, 4, 9, 16]

print (arr)
print(arr[0])
print ( len(arr) )



# For 

sum = 0
for num in arr:
    sum += num
print (sum)  ## 30


# In
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print ('yay')


# Range
#for i in range(15):
#    print(i)


# List Method

# arr.append(elm)
# arr.insert(index, elm)
# arr.remove(elm)  # remove first instance of search elm
# arr.pop(index) -- removes and returns the element at the given index

# List Buildup
list1=[]          ## Start as the empty list
list1.append('a')   ## Use append() to add elements
list1.append('b')

# List slice
list2 = ['a', 'b', 'c', 'd']
print (list2[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print (list2)


# Manipulation

numList1 = [1, 2 , 3, 4]
numList2 = [10, 12, 13, 14]    


print(numList1 + numList2)  # concate two list
