def copy_string(word,num):
    final_lenght=2
    
    if len(word)< final_lenght:
        final_lenght=len(word)
    substr = word[:final_lenght]
    result=""    
    for i in range(num):
        result = result + substr
    return result        


print(copy_string('abcdef', 2))  # Output: "abab" (substring "ab" repeated 2 times)
print(copy_string('p', 3))  # Output: "pp" (substring "p" repeated 3 times)