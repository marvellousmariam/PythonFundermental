errands=["Sweep","Cooking","Mop","Clean"]
print(enumerate(errands))

for index,errand in enumerate(errands,1):
    print(f"{errand} is a number {index} on my list of things to do today!")