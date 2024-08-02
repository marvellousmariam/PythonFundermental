def check_is(word):
    if word[:2]=="is":
        return word
    else:
        return f"is{word}"
    
word=input("Enter the word: ")
print(check_is(word=word))   