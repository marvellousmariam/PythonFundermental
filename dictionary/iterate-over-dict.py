chinese_food={
    "Sesame Chicken":9.99,
    "Boneless Spare Ribs":7.99,
    "Fried Rice":1.99
}
# Anti-Pattern : A solution to a programming problem that is considered ineffective and counter-productive
for food in chinese_food:
    print(f"The food if {food} is price is {chinese_food[food]}")


pounds_to_kilograms={
    5:2.26796,
    10:4.53592,
    25:11.3398
}

for pound in pounds_to_kilograms:
    print(f"{pound} is equal to {pounds_to_kilograms[pound]} kilograms")