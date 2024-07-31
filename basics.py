# import datetime

# date=datetime.datetime.now()
# print(date)
# nynumber=10
# mytext="Hello"
# print(nynumber,mytext)


# x=10
# y="10"
# sumx=x+x
# sumy=y+y
# print(sumx,sumy)





# student_grade=[9.1,8.8,7.5]
# mysum=sum(student_grade)
# mean = mysum/len(student_grade)
# print(f"The mean is {mean}")



# monda_temp=[9.1,8.8,6.5,7.4,8.1]
# print(monda_temp[1:4])
# print(monda_temp[-5])
# print(monda_temp[-2:])


def mean(value):
    if type(value)== dict:
        value_sum= sum(value.values())
        value_len=len(value)
        mean=value_sum/value_len
    else:    
        value_sum= sum(value)
        value_len=len(value)
        mean=value_sum/value_len
    return f"The mean is {mean}"

print(mean({"Mariam":34,"Mary":76,"Sam":87,"Eve":32}))
print(mean([1,2,3,4,56,6]))