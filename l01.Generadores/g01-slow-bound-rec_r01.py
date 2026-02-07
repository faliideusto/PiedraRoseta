# r00
# + marcamos vueltas al 5

import time
import sympy as sp

# Ejecutar
a=3
b=3
maxN=1e4
iter=3


def generador_recursivo(seed=(2,3), A=3, B=3, Qmax = maxN):
    P = set(seed)
    # Generar todas S = p1^a + p2^b con p1,p2 ∈ P y 1≤a,b≤A,B
    nuevos = []
    S_vals = []
    P_list = sorted(P)
    #print("... calculating S", end='')
    for p1 in P_list:
        for a in range(1,A+1):
            s1 = p1**a
            for p2 in P_list:
                for b in range(1,B+1):
                    S_vals.append((p1, a, p2, b, s1 + p2**b))
    #print("\r... calculating S [Done]")

    # Reflejar sobre todas bases p ∈ P
    incr = 1
    total = len(S_vals)
    for (p1, a, p2, b, S) in S_vals:
        #print("\r... generating prime refections %d/%d (%2.2f%%)" % (incr,total, float(incr)/total*100), end='')
        for p in P_list:
            q = S - p
            if q <= 1 or q > Qmax:
                continue
            # Cribas rápidas
            if q != 3 and q % 3 == 0:
                continue
            if q != 5 and q % 5 == 0:
                continue
            if sp.isprime(q) and q not in P:
                data = {
                    "q": q, "p": p, "p1": p1, "a": a, "p2": p2, "b": b,
                    "E": S/2, "S": S
                }
                nuevos.append((q, p, p1, a, p2, b, S))
                #print(data)
        incr = incr+1

    if not nuevos:
        # TODO
        pass


    # extract the lowest prime of the set
    nuevos.sort(key=lambda r: (r[0], r[3]+r[5], r[6]))
    q = nuevos[0][0]

    # Marcamos vueltas a 5
    if nuevos[0][2] == 5 and nuevos[0][3] == 1:
        print("\n << Reinicio en 5>>")

    #print("Prime count is: ", len(P))
    print(f"q:{nuevos[0][0]} es simetria de p:{nuevos[0][1]} en e:{nuevos[0][6]/2} [ ({nuevos[0][2]:03d}^{nuevos[0][3]} + {nuevos[0][4]:03d}^{nuevos[0][5]})/2 ]")

    # Recursion
    if q < Qmax:
        P.add(q)
        generador_recursivo(P, A=3, B=3)


################################################################
# main program
################################################################

start = time.time()
print(f"\n A={a} B={b} Qmax={maxN:.2e} max_iter={iter}")
P_final, pasos = generador_recursivo(A=a, B=b, Qmax = maxN)
end = time.time()

# Descomenta las líneas debajo para obtener una lista
# de los primos generados

print("Primo generado (q): base (p), Eje (E), Suma (S)")
for s in pasos:
    print(s)

print("\n\nTotal Primos generados:", len(P_final))
print(f"\nTiempo de ejecucion: {end-start:.2f}s")

