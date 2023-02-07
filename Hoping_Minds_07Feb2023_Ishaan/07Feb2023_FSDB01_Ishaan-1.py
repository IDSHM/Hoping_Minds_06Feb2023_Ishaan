# function for merge subarray
def merge(left, right):

# result stored in this 
    result = []
    print(result)
    
# create two indices  
    i,j = 0, 0 
    while i < len(left) and j < len(right):
        
# if this condition true then left elements will append in result
        if left[i] <= right[j]:  
            result.append(left[i])
            i+=1
            
# else this condition true then right elements will append in result
        else:  
            result.append(right[j])
            j+=1
    
# append remaining elements in the array       
    result += left[i:]
    result += right[j:]
    return result

# function for mergesort 
def mergesort(a):

    if(len(a) <= 1): 
        return a
    
# if the list is not sorted then this below code executed
    mid = int(len(a)/2)
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    return merge(left, right)

# inputs
arr = [5,8,9,4,3,6,77,22,6,1]
print(mergesort(arr))

