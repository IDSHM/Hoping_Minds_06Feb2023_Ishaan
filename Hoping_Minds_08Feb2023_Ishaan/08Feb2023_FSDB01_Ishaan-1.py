# inputs
arr = [5,4,3,2,1,6,7,8,9,10]

flag = False

# sorting
arr.sort()
print(arr)

# find element position
x = 11
for i in range(len(arr)):
    if arr[i]==x:
      flag = True
      break

if flag == 1:
    print('Element was found at index',i)
else:
    print('{} was not found.'.format(x))
 
