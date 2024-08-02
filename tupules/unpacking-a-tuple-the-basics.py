employee=("Bob", "Jhonsons","Manager",50)

firstname=employee[0]
lastname=employee[1]
position=employee[2]
age=employee[3]

firstname,lastname,position,age=employee
print(firstname,lastname,position,age)

subject,verb,adjective=["Python","is","fun"]
print(subject,verb,adjective)

# firstname,lastname,title=employee error
# firstname,lastname,position,age,salary=employee
a=5
b=10
b,a=a,b
print(a)
print(b)