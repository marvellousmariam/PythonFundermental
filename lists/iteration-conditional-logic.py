# numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# total=0
# for number in numbers:
#     if number % 2 ==0:
#         continue
#     else:
#         total= total+number
# print(total)    

value=[3,6,9,12,15,18,21,24]
other_values=[5,10,15,20,25,30]

def odd_sum(numbers):
    total=0
    for number in numbers:
        if number %2==0:
            continue
        else:
            total=total+number
    return total        
    
    
print(odd_sum(value))
print(odd_sum(other_values))


def greatest_number(numbers):
    # return max(numbers)
    greatest=numbers[0]
    for number in numbers:
        if greatest < number:
            greatest=number
    return greatest        

print(greatest_number([1,2,3]))
print(greatest_number([3,2,1]))
print(greatest_number([4,5,5]))
print(greatest_number([-3,-2,-1]))