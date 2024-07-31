# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

def compute_value(n):
    # Compute the value of n+nn+nnn
    value = n + int(str(n) * 2) + int(str(n) *3)  # Convert n to string, multiply by 2 and 3, then
    return value


number=int(input("Enter number: "))
print(compute_value(number))   