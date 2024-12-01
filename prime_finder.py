m, n = int(input("First number... ")), int(input("Second number... "))
myInterval = range(m, n + 1)
primeNumbers = []
def isCertainlyPrime():
    for i in myInterval:
        isPrime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeNumbers.append(i)
isCertainlyPrime()
print(primeNumbers)
