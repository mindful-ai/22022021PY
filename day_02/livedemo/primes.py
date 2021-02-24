def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

print("primes.py ", __name__)
if __name__ == "__main__":
    
    # Input
    n = int(input("Enter a number: "))

    # Output
    if(checkprime(n)):
        print("The number is prime")
    else:
        print("The number is not prime")

