#THE IN OPERATOR
print("fast" in "breakfast")
print("fast" in "lunch")


meals=["breakfast", "lunch", "dinner"]

print("lunch" in meals)
print("dinner" in meals)
print("snack" in meals)
print("Breakfast" in meals)
print()

test_score=[99.0,35.0,23.5]

print(99.0 in test_score)
print(99 in test_score)
print(28 in test_score)
print(43.7 in test_score)

print()
# Not in operator opposite of the in operator
print("lunch" not in meals)
print("22" not in test_score)
print("Breakfast" not in meals)
print(35 not in test_score)

if 1000 not in test_score:
    print("value invalid !!")
