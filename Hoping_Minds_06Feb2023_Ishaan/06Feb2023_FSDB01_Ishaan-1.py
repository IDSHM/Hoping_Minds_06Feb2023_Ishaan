# bubblesort function
def bubble(l):

# Outer loop for traverse the entire list  
 for i in range(0, len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
        print(l)
#  return l
 
# inputs

l = [5,4,8,9,7,2]
#l = [10,9,8,7,6,5,4,3,2,1]
#l = [1,2,3,4,5,6,7,8,9,10]

# unsorted list
print("Unsorted")
print(l)
# sorted list
print("Sorted")
bubble(l)
