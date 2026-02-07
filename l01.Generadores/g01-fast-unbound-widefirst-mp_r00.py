# RosettaStone (2025)
# Keko
# Esquema de generacion de primos por reflexiones

# widefirst
# optimizada en velocidad
# multiprocessing
# Primos, bases, radios a disco

import time
import math
from sympy import isprime
from multiprocessing import cpu_count, Lock, Manager, Pool, Value

# Globals
a=3
b=3
maxN=0
iter=100


# Shared objects (need to be global for the Pool parallel processes)
nTasksTotal = None
nTasksDone = None
nTasksLock = None
nPrimesFound = None
gMax = None
gDigits = None

# Metrics
gStartTime = None


def comprobar_reflejo(args):
    global nTasksDone, nPrimesFound, gStartTime
    global nPrimesFound, gMax, gDigits

    (p1, a, p2, b, S, primeListCopy, primeList) = args

    #print(f"... Comprobando Reflejo sobre {S}")
    for p in primeListCopy:
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

        if q not in primeList:
            if isprime(q):

                ##############################################################
                # prime number found!
                ##############################################################

                #res.append((q, p, p1, a, p2, b, S))
                #print(f"Nuevo primo encontrado: {q}")

                with nTasksLock:
                    nPrimesFound.value += 1
                    if q > gMax.value:
                        gMax.value = q
                        gDigits.value = int(math.log10(q))

                primeList.append(q)
                #print(f"... total: {len(primeList)}")
                #############################################################

    with nTasksLock:
        nTasksDone.value +=1

    speed = nPrimesFound.value/(time.time() - gStartTime)
    print(f"\r... working {100*nTasksDone.value/nTasksTotal:.2f}% ({nTasksDone.value}/{nTasksTotal}) Count: {nPrimesFound.value} Max: {gDigits.value} digits Speed: {speed:.2f} primes/sec", end='')



def generador_iterativo(A=3, B=3, Qmax=200, max_iter=10):

    # Initializacion
    global gStartTime, nPrimesFound, gMax, gDigits

    gStartTime = time.time()
    nPrimesFound = Value('I',0)
    gMax = Value('I',1)
    gDigits = Value('I',1)


    # multiprocessing safe list
    primeList = Manager().list()
    primeList.append(2)
    primeList.append(3)

    for iter in range(max_iter):
        print("\n\n<-- Starting iter <%d> [Initial Prime count is: %d] [Max is %d digits] -->" % (iter,len(primeList), gDigits.value))

        # Generar todas S = p1^a + p2^b con p1,p2 ∈ P y 1 ≤ a,b ≤ A,B
        S_vals = []
        primeListCopy = sorted(primeList)
        print("... calculating S", end='')
        for p1 in primeListCopy:
            for a in range(1,A+1):
                s1 = p1**a
                for p2 in primeListCopy:
                    for b in range(1,B+1):
                        S_vals.append((p1, a, p2, b, s1 + p2**b))
        print("\r... calculating S [Done]")


        ##############################################################
        # Multiproceso
        #
        # Comprobar reflejos en sobre los ejes identificados

        # Indicadores de avance (multiprocessing safe)
        global nTasksDone, nTasksLock
        nTasksDone = Value('I',0)
        nTasksLock = Lock()

        global nTasksTotal
        nTasksTotal = len(S_vals)

        args = [(p1, a, p2, b, S, primeListCopy, primeList)
                for (p1, a, p2, b, S) in S_vals ]

        # pool.map devuelve un iterador que llama a la funcion
        # una vez por cada elemento del iterable args
        with Pool(cpu_count()) as pool:
            poolTareas = pool.map(comprobar_reflejo, args)

        for encontrarPrimos in poolTareas:
            pass

        #
        ###############################################################

    return sorted(primeList)


print(f"\n A={a} B={b} Qmax=N/A max_iter={iter}")

start = time.time()
primes = generador_iterativo(A=a, B=b, Qmax = maxN, max_iter=iter)
end = time.time()
print("\n\n Primos generados:", len(primes))
print(f" Tiempo de ejecución {end-start:.2f} seg Ratio {len(primes)/(end-start):.2f} primos/seg ")

