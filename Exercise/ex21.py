def check_number(target):
    if target % 2 == 0:
        return f"{target} is an even number"
    else:
        return f"{target} is an odd number"    
    
number_to_check=int(input("Enter a number: "))
print(check_number(number_to_check))