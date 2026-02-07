import sympy as sp
import math
import random

def primorial(p):
    """Devuelve p# = producto de todos los primos ≤ p."""
    return sp.prod(sp.primerange(2, p+1))

def elegir_p_para_digitos(D):
    """
    Elige el mayor primo p tal que p# tenga menos de D dígitos.
    Esto aproxima bien el tamaño del centro.
    """
    for p in sp.primerange(2, 200):  # suficiente para primos enormes
        if len(str(primorial(p))) >= D:
            return sp.prevprime(p)
    return 13  # fallback

def offsets_admisibles(p, R):
    """
    Genera offsets k impares ≤ R tales que gcd(k, p#) = 1.
    """
    P = list(sp.primerange(2, p+1))
    for k in range(1, R+1, 2):
        if all(k % q != 0 for q in P):
            yield k

def generar_primo_por_primorial(D, R=200000):
    """
    Genera un primo de D dígitos usando un centro basado en primoriales.
    R es el radio máximo de búsqueda.
    """
    # 1. Elegir primorial adecuado
    p = elegir_p_para_digitos(D)
    base = primorial(p)

    # 2. Ajustar el centro multiplicando por un factor impar m
    #    para que tenga exactamente D dígitos
    m = 1
    while len(str(base * m)) < D:
        m += 2  # solo factores impares

    c = base * m

    # 3. Buscar primo alrededor del centro
    for k in offsets_admisibles(p, R):
        a = c - k
        b = c + k
        if len(str(a)) == D and sp.isprime(a):
            return a
        if len(str(b)) == D and sp.isprime(b):
            return b

    return None  # no encontrado en ese radio

# ------------------------------
# Ejemplo de uso:
# Generar un primo de 100 dígitos
# ------------------------------
if __name__ == "__main__":
    D = 100
    print(f"Generando primo de {D} digitos...")
    primo = generar_primo_por_primorial(D)
    if primo:
        print(f"Primo generado ({D} dígitos):")
        print(primo)
    else:
        print("No se encontró primo en el radio dado.")
