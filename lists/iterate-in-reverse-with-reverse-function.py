the_simpsons=["Homer","Marge","Bart","Lisa","Maggie"]
# print(the_simpsons[::-1]) reverse other

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters")

# print(reversed(the_simpsons))

for character in reversed(the_simpsons):
     print(f"{character} has a total of {len(character)} characters")