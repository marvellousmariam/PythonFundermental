# Write a Python program to calculate the
# difference between a given number and 17. 
# If the number is greater than 17,
# return twice the absolute difference.

number=int(input("Enter number: "))
if number <= 17:
     print(17-number)
else:
    print(2*(number-17))
       