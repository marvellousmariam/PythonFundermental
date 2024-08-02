def multi_sum(a,b,c):
    sum=a+b+c
    if a ==b==c:
        return (sum)*3
    else:
        return sum
    
    
f_number=int(input("Enter number: "))    
s_number=int(input("Enter number: "))  
l_number=int(input("Enter number: "))  

print(multi_sum(f_number,s_number,l_number))