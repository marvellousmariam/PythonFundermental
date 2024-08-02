def check_vowel(target):
    if target == "a"or target=="A" or target =="e"or target=="E" or target=="i"or target=="I" or target == "o"or target=="O" or target=="u"or target=="U":
        return f"{target} is vowel"
    else:
        return f"{target} is consonant"

check_letter=input("Enter letter: ")    
print(check_vowel(check_letter))