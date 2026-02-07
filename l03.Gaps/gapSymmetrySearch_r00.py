from sympy import isprime

def obtener_todos_los_segmentos_simetricos(lista):
    segmentos = []

    for pos in range(len(lista)):
        centro = lista[pos]
        izquierda = lista[:pos]
        derecha = lista[pos+1:]

        n = min(len(izquierda), len(derecha))

        # Probar todas las longitudes posibles
        for k in range(1, n+1):
            if izquierda[-k:] == derecha[:k][::-1]:
                segmento = izquierda[-k:] + [centro] + derecha[:k]
                segmentos.append((centro,segmento))

    return segmentos



nMax=1e5

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
    #line = f"{primes[index]}" + " -" * gap + f" {primes[index+1]}"
    #print("Gap: " + str(gap)+": " + line.center(80,' '))


print("\n\n####\nGaps: ")
#for index in range(len(gaps)):
    #print(f"{gaps[index]} . ", end='')

print("\n\n####\nSymmetric Gaps: ")
segmentos = obtener_todos_los_segmentos_simetricos(gaps)
for segmento in segmentos:
    print(f"Longitud: {len(segmento[1])} : (Centro, Segmento): {segmento}")


