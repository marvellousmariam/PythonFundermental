#  Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

filename=input("Enter file name with extention: ").split(".")
print (filename[1])