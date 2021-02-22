# Write a program to check if a string is a palindrome or not

# input < madam, 110011
# output > The string is a palindrome

# if ():
#   print()
# else:
#   print()

# input
text = input("Enter some text: ")
words = text.split()

# process
# output

print("---------------------------------------")
for word in words:
    nword = word.lower()
    if(nword == nword[::-1]):
        print(word)
    
