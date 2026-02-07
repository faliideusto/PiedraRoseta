# RosettaStone (2025)
# Keko

# versión optimizada en velocidad de esquema de generación de primos por reflexiones
# widefirst

import time
import sympy as sp

def generador_iterativo(P_inicial=(2,3), A=3, B=3, Qmax=200, max_iter=10):
    P = set(P_inicial)

    for iter in range(max_iter):
        print("\n\n<-- Starting iter <%d> [Initial Prime count is: %d] -->" % (iter,len(P)))
        nuevos = []

        # Generar todas S = p1^a + p2^b con p1,p2 ∈ P y 1 ≤ a,b ≤ A,B
        S_vals = []
        P_list = sorted(P)
        print("... calculating S", end='')
        for p1 in P_list:
            for a in range(1,A+1):
                s1 = p1**a
                for p2 in P_list:
                    for b in range(1,B+1):
                        S_vals.append((p1, a, p2, b, s1 + p2**b))
        print("\r... calculating S [Done]")

        # Reflejar sobre todas bases p ∈ P
        total = len(S_vals)
        incr = 1
        found = 0
        start = time.time()
        for (p1, a, p2, b, S) in S_vals:
            speed = found/(time.time() - start)
            print("\r... generating and checking prime refections (%2.2f%%) - Speed: %4.2f primes/sec" % (float(incr)/total*100, speed), end='')
            for p in P_list:
                q = S - p
                if q <= 1:
                    continue
                # Cribas rápidas
                if q != 3 and q % 3 == 0:
                    continue
                if q != 5 and q % 5 == 0:
                    continue
                if q != 7 and q % 7 == 0:
                    continue
                if q not in P:
                    if sp.isprime(q):
                        #data = {
                        #    "q": q, "p": p, "p1": p1, "a": a, "p2": p2, "b": b,
                        #    "E": S/2, "S": S
                        #}
                        #print(data)
                        found = found + 1
                        P.add(q)

            incr = incr+1

    return sorted(P)

# Ejecutar
a=4
b=4
maxN=0
iter=3

print(f"\n A={a} B={b} Qmax=N/A max_iter={iter}")

start = time.time()
P_final = generador_iterativo(A=a, B=b, Qmax = maxN, max_iter=iter)
end = time.time()
print("\n\n Primos generados:", len(P_final))
print(f" Tiempo de ejecución {end-start:.2f} seg Ratio {len(P_final)/(end-start):.2f} primos/seg ")

# Descomenta las líneas debajo para obtener una lista
# de los primos generados

#print("Primos generados (q): base (p), Eje (E), Suma (S)")
#for s in pasos:
    #print(s)
