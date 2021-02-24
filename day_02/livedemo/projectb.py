# Project B
# Collect some numbers from the user
# Spearate the odd numbers ,even numbers and prime numbers from the data

import primes
print("projectb.py ", __name__)

# Input

numbers = []
while True:
    uin = input(" --> (q to quit) ")
    if(uin == 'q'):
        break
    else:
        if(uin.isdigit()):
            numbers.append(int(uin))

print(numbers)

# Process

odds = []
evens = []
prime = []

for n in numbers:
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)

    if(primes.checkprime(n)):
        prime.append(n)



# Output

print("-"*60)
print("ODDS: ", odds)
print("EVENS: ", evens)
print("PRIMES: ", prime)
