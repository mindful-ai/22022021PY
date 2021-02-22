# Program to print the difference of two numbers
# tell the sign of the outcome

# input

a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

# processing

res = a - b

# output

print("-"*30)

print("DIFFERENCE: ", abs(a - b))

if(res > 0):
    print("The difference is positive")
    if(res > 10):
        print("Result greater than 10")
elif(res < 0):
    print("The difference is negative")
else:
    print("The difference is zero")
print("Thank you!")
