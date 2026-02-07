import time

def criba_eratostenes(limite):
    inicio = time.perf_counter()

    if limite < 2:
        return []

    # Solo impares: índice i representa el número 2*i+1
    size = (limite // 2)
    es_primo = [True] * size
    es_primo[0] = False  # el número 1 no es primo

    p = 3
    while p * p <= limite:
        if es_primo[p // 2]:
            # Empezamos a tachar desde p*p, solo impares
            inicio_tachado = (p * p) // 2
            paso = p
            for i in range(inicio_tachado, size, paso):
                es_primo[i] = False
        p += 2

    # Reconstruimos la lista de primos
    primos = [2] + [2*i + 1 for i in range(size) if es_primo[i]]

    fin = time.perf_counter()
    print(f"Tiempo criba Eratóstenes: {fin - inicio:.6f} segundos")

    return primos


# ------------------------------
# EJEMPLO DE USO
# ------------------------------

LIMITE = 1000000  # cámbialo para probar rendimiento

primos = criba_eratostenes(LIMITE)
print(f"Primos menores de {LIMITE}:")
print(primos)
print(f"Primos encontrados hasta {LIMITE}: {len(primos)}")
