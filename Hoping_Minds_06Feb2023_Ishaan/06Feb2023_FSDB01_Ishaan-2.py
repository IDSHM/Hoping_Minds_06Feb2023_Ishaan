# insertion function
def insertion(a):
    for i in range(1,len(a)):
        value=a[i]
        j = i - 1  
        while j >= 0 and value < a[j]:  
          a[j + 1] = a[j]  
          j -= 1  
          a[j + 1] = value  
          print(a)  

# inputs
a = [10, 5, 13, 8, 2] 

# unsorted
print("The unsorted list is:", a)  

# sorted
print("The sorted a is:", insertion(a))  
