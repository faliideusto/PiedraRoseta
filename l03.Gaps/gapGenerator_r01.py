from sympy import isprime

nMax=1e6

primes = []
gaps = []

for n in range(2,int(nMax+1)):
    if isprime(n):
        primes.append(n)

print(f"nMax : {int(nMax)}")
print(f"Found: {len(primes)} primes")

for index in range(len(primes)-1):
    gap = primes[index+1] - primes[index] -1
    gaps.append(gap)
    line = f"{primes[index]}" + " -" * gap + f" {primes[index+1]}"
    print("Gap: " + str(gap)+": " + line.center(80,' '))


print("\n\n####\nGaps: ")
for index in range(len(gaps)):
    print(f"{gaps[index]} . ", end='')

print("")
