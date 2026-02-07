from sympy import isprime

nMax=1e5

primes = []
gaps = []

for n in range(2,int(nMax+1)):
    if isprime(n):
        primes.append(n)

print(primes)
