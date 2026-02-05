import time
inicio = time.perf_counter()

LIMITE = 1000000


def generar_Cp(p, limite):
    Cp = set()
    max_k = (p - 1) // 2

    for k in range(1, max_k + 1):
        max_x = (limite - k) // p

        for x in range(max_x + 1):
            n1 = p * x + k
            if n1 < limite and (n1 & 1):
                Cp.add(n1)

            n2 = p * x - k
            if n2 > 0 and n2 < limite and (n2 & 1):
                Cp.add(n2)

    return Cp


#impares iniciales
I = set(range(1, LIMITE, 2))

p = 3
primos = {3}

print("Calculando primos...")

while p * p <= LIMITE:
    Cp = generar_Cp(p, LIMITE)

    I &= Cp
    I |= primos

    # siguiente primo
    p = min(n for n in I if n > p)
    primos.add(p)

primos = sorted(n for n in I if n > 1)

print(f"Primos impares menores de {LIMITE}: {len(primos)} encontrados")
fin = time.perf_counter()
print(f"Tiempo total: {fin - inicio:.6f} segundos")
