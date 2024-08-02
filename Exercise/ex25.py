def check_in_list(values,target):
        if target in values :
            return f"{target} found in list"
        else:
            return f"{target} not found in list"
        
        
val=[1,2,3,4,5,6]
print(check_in_list(val,4))
             
            