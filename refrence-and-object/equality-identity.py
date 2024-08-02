# Equality test where two object are equal
#identity checkes where to names in the program are pointing to the same object e.g the "is" keyword

students=["Bob","Sally","Sue"]
athletes=students
nerds=["Bob","Sally","Sue"]
#Equality
print(students==athletes)
print(students==nerds)
#Identity
print(students is athletes)
print(students is nerds)

a=1
b=1
print(a==b)
print(a is b)

c=3.14
d=3.14
print(c==d)
print(c is d)

e="hello"
f="hello"
print(e==f)
print(e is f)