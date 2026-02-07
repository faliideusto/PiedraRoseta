import sympy as sp

def generar_iterativo(P_inicial=(2,3), A=3, B=3, Qmax=100, max_iter=10):

    # contador para numero de primos encontrados
    count=len(P_inicial)

    P = set(P_inicial)

    # Array para registros de q, eje y primo generador
    construcciones = []

    for iter in range(max_iter):

        print("\n\n")
        print("#######################################")
        print("# Iteracion: %d (Empieza con %d primos)" % (iter, len(P)))
        print("#######################################")

        # Array para almacenar los nuevos primos en cada iteracion
        nuevos = []

        # Generar todas S = p1^a + p2^b con p1,p2 ∈ P y 1≤ a, b ≤3
        S_vals = []
        P_list = sorted(P)
        for p1 in P_list:
            for a in range(1, A+1):
                s1 = p1**a
                for p2 in P_list:
                    for b in range(1, B+1):
                        S_vals.append((p1, a, p2, b, s1 + p2**b))

        # Reflejar sobre todas bases p ∈ P
        iter2 = 1
        total = len(S_vals)*len(P_list)/5
        for (p1, a, p2, b, S) in S_vals:
            for p in P_list:
                # Track Progress
                print("\r %d of %d (%2.2f%%) Candidatos: [%d]" % (iter2, total, float(iter2)/total, len(nuevos)), end="")
                # Obtenemos q como reflejo de p respecto del eje E
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

            iter2 = iter2 + 1

        if not nuevos:
            break

        # Añadir y registrar construcciones mínimas para los primos encontrados
        nuevos.sort(key=lambda r: (r[0], r[3]+r[5], r[6]))
        seen_q = set()
        print("\n")
        for rec in nuevos:
            q, p, p1, a, p2, b, S = rec
            if q not in seen_q:
                count = count +1
                data = {"#":count,
                    "q": q, "p": p, "p1": p1, "a": a, "p2": p2, "b": b,
                    "E": S/2, "S": S
                }
                print(data)
		#construcciones.append({data})
                P.add(q)
                seen_q.add(q)


    return sorted(P), construcciones


# main
P_final, pasos = generar_iterativo(P_inicial=(2,3), A=3, B=3, Qmax=1000, max_iter=10)
print('Generados {} primos < {}'.format(len(P_final), max))
#print("Semillas finales:", P_final)
#print("Ejes y Construcciones añadidas:")
#for s in pasos:
    #print(s)
