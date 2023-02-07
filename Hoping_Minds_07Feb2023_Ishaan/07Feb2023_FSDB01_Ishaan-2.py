# function for recursion factorial
def rec_fac(n):
  if n==1:
    return n
  else:
    return n*rec_fac(n-1)

# take input from the user  
num = int(input("Enter a number: "))  

print(rec_fac(num))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", rec_fac(num))
