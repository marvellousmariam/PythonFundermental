
def found_number(values,target):
    for value in values:
        if target ==  value:
            return f"{target} found"
            break
        else:
            return f"{target} not found"
val=[1,2,3,4,5,6,7]
print(found_number(val,8))