import sympy as sp

def generar_iterativo(P_inicial=(2,3), A=3, B=3, Qmax=200, max_iter=10):
    P = set(P_inicial)
    construcciones = []  # registros de q y su construcción
    for iter in range(max_iter):
        print("\n\n<-- Starting iter <%d> [Initial Prime count is: %d] -->" % (iter,len(P)))
        nuevos = []
        # Generar todas S = p1^a + p2^b con p1,p2 ∈ P y 1≤a,b≤A,B
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
        for (p1, a, p2, b, S) in S_vals:
            print("\r... generating prime refections %d/%d (%2.2f%%)" % (incr,total, float(incr)/total*100), end='')
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
                    nuevos.append((q, p, p1, a, p2, b, S))
            incr = incr+1

        if not nuevos:
            break
        # Añadir y registrar construcciones mínimas por q
        total = len(nuevos)
        incr = 1
        nuevos.sort(key=lambda r: (r[0], r[3]+r[5], r[6]))
        seen_q = set()
        print("")
        for rec in nuevos:
            print("\r... filtering new primes %d/%d (%2.2f%%)" % (incr, total, float(incr)/total*100), end='')
            q, p, p1, a, p2, b, S = rec
            if q not in seen_q:
                data = {
                    "q": q, "p": p, "p1": p1, "a": a, "p2": p2, "b": b,
                    "E": S/2, "S": S
                }
                #print(data)
                construcciones.append(data)
                P.add(q)
                seen_q.add(q)
            incr = incr + 1
    return sorted(P), construcciones

# Ejecutar
P_final, pasos = generar_iterativo(P_inicial=(2,3), A=3, B=3, Qmax=100000, max_iter=3)
print("\n\nPrimos generados:", len(P_final))
print("Secuencia de generacion:")
for s in pasos:
    print(s)
