def count_occurance(values,target):
    total_occurance=0
    for value in values:
        if value==target:
            total_occurance=total_occurance+1    
    return f"{target} total occured {total_occurance} times"    
val=[1,2,3,4,5,4,6,4,7,4]
print(count_occurance(val,4))
      
        
            