import copy
p = [2, 3, 5, 7]
x = list(range(1,100))
candidatos=[]
candidatos3=[]
candidatos5=[]

#p*x+-(p−1)
i=0
#criba de los multiplos de 2
for x in range (51):
    i=0
    resultadonegativo= p[i]*x-(p[i]-1)
    if resultadonegativo not in candidatos and resultadonegativo>0:
        candidatos.append(resultadonegativo)

for x in range (33):
    i=1
    resultadopositivo=p[i]*x+(p[i]-1)
    resultadonegativo=p[i]*x-(p[i]-1)
    if resultadopositivo not in candidatos3 and resultadopositivo>0:
        candidatos3.append(resultadopositivo)
    if resultadonegativo not in candidatos3 and resultadonegativo>0:
        candidatos3.append(resultadonegativo)  
candidatos3.sort()
#print("P3:",candidatos3)

copia=copy.deepcopy(candidatos)
#criba de los multiplos de 3
for c in copia:
    if c not in candidatos3:
        candidatos.remove(c) 
#print(candidatos)

for x in range (20):
    i=2
    resultadopositivo=p[i]*x+(p[i]-1)
    resultadonegativo=p[i]*x-(p[i]-1)
    if resultadopositivo not in candidatos5 and resultadopositivo>0:
        candidatos5.append(resultadopositivo)
    if resultadonegativo not in candidatos5 and resultadonegativo>0:
        candidatos5.append(resultadonegativo)  
candidatos5.sort()
#print("P5:", candidatos5)

#criba de los multiplos de 5
print(candidatos)
copia2=copy.deepcopy(candidatos)
for c1 in copia2:
    #print(c1)
    if c1 not in candidatos5: 
        #("ELIMINANDO: ",c)  
        candidatos.remove(c1) 
#print("Final",candidatos)