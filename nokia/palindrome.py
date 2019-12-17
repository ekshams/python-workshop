# program to check word is palindrome or not.

lang = "malayalam"

print(":",lang[:])
print("::",lang[::])
print("::",lang[:-2])

# if lang == lang[::-1]:
    # print("palindrome")
# else:
    # print("not palindrome")
    
    
print("palindrome" if lang == lang[::-1] else "not palindrome")
    
    
    