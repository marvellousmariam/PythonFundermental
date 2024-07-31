# myfile=open("fruits.txt")
# content=myfile.read()
# print(content)
# print(content)
# myfile.close()
import time
import os
# while True:
#     with open("fruits.txt")as myfile:
#         content=myfile.read()
#         print(content)
#         time.sleep(10)x
if os.path.exists("files/veg.txt"):
    with open ("files/veg.txt") as myfile:
        print(myfile.read())
else:
    time.sleep(5)
    print("File not existed")
time.sleep(10)    