color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(f"Original list : \n {color_list_1}\n {color_list_2}")

print(f"Difference between 1 and 2 {color_list_1.difference(color_list_2)}")
print(f"Difference between 2 and 1 {color_list_2.difference(color_list_1)}")