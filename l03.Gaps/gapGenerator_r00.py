from sympy import isprime

nMax=1e4

primes = []

for n in range(2,int(nMax+1)):
    if isprime(n):
        primes.append(n)

print(f"nMax : {int(nMax)}")
print(f"Found: {len(primes)} primes")

for index in range(len(primes)-1):
    spaces = primes[index+1] - primes[index] -1
    line = f"{primes[index]}" + " -" * spaces + f" {primes[index+1]}"
    print(line.center(80,' '))
