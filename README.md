**Lineas de Investigación activas**

- **L00 Cribas modulares**
- **L01 Generadores de primos por simetría**


**L00 Cribas Modulares**
  La criba de Eratóstenes es la más famosa, pero no es la única forma de “tamizar” números. Existen cribas modulares o cribas complementarias, que consisten en aplicar filtros basados en congruencias para descartar números según patrones aritméticos específicos.

**L01 Generadorse de primos por simetría** 
Es posible definir un algoritmo que genere primos a partir de:
    - un cojunto inicial de primos "semilla" k0 = {2,3}
    - vamos descubriendo primos simétricos a los existentes, a partir posibles eje de simetría
    - cada primo obtenido, pasa a formar parte del conjunto y permite generar nuevos primos
    - El conjunto así definido se va ampliando, de forma iterativa.
    - El generador define una formula para calcular -a priori, a partir de primos conocidos- nuevos primos

 
            G01 (Ejes de simetría): 
            E = (p1^a + p2^b)/2
            q (nuevo primo) = p (primo existente) + 2r = p + 2(E-p)
            q = p + (p1^a + p2^b) -2p = (p1^a + p2^b) - p

    
    - El generador así definido entrega una gran cantidad de primos, con exponentes relativamente bajos para a y b.
    - Si la distribución de primos es aleatoria, la distribución de estos ejes de simetría también debería serlo.

    - Para considerar el algoritmo valioso, deberá satisfacer un criterio de "bondad".
        - Porcentaje de primos vs compuestos en cada nueva iteración.
        - Porcentaje de primos cubiertos tras cada iteración (para busqueda en anchura)
            - (100% implicaría la existencia de una "estructura")
        - Coste computacional de la iteracion vs metodo aleatorio.         

    - Hay que tener MUCHO CUIDADO porque:
        - Dos primos cualesquiera siempre son simétricos respecto al centro del intervalo que definen. Además, dos primos impares 
          siempre definen un intervalo con centro en un numero par. 
        - Todo numero par puede ser expresado como la suma de dos primos (goldbach). Esto nos da ya una solución con a y b iguales a 1.
        - Esto implica que SIEMPRE vamos a poder encontrar un eje, como suma de dos primos conocidos, porque el eje es PAR.
        - Si tengo un conjunto de n numeros primos (que incluye todos los primos menores que D). El menor numero primo fuera de ese
          conjunto, forma n posibles simetrías con cada uno de los primos conocidos. -> Todo primo es simétrico respecto a TODOS los que le preceden.

    - Es posible modificarlo de varias formas:    
            - busqueda en profundidad... generar los primos más grandes posible
            - búsqueda en anchura... generar el máximo numero de primos 
            - busqueda incremental. Ir añadiendo un solo primo al conjunto, y comenzar.
            - Se puede obtener el conjunto completo de primos como simetría respecto a uno sólo de ellos, por ejemplo, a partir de p=3
            - Cambiar conjunto de partida por otro.
    
    - No estamos por el momento "prediciendo" primos... solo constatando que son muy frecuentes en determinadas zonas (heurística)

    - Para considerar el algoritmo valioso, deberá satisfacer un criterio de "bondad".
        - Porcentaje de primos vs compuestos en cada nueva iteración (100% implicaría la existencia de una "estructura").
        - Porcentaje de primos cubiertos tras cada iteración (para busqueda en anchura)
        - Coste computacional de la iteracion vs metodo aleatorio.         
          
    - patron de escaleras a partir de p=5
    
    - Cuestiones interesantes:
        - ¿Genera todos los primos menores que un nMax?
        - ¿En qué orden los genera?
        - ¿Es posible modificarlo para generar primos cada vez más grandes aunque el conjunto sea incompleto?
        - ¿Podemos partir de otro conjunto inicial (por ejemplo 2 primos de 20 digitos)... cual sería el resultado?
    
    
    q = 2E - p -> formula para generar el candidato q, simétrico a p respecto al eje E.

            Ejemplo Numérico
            q = p1^a + p2^b - p
    
            E-p es el radio
            q = E + radio = E + E - p = 2E - p
            
            {'q': 5, 'p': 2, 'p1': 2, 'a': 2, 'p2': 3, 'b': 1, 'E': 3.5, 'S': 7}
            {'q': 7, 'p': 3, 'p1': 2, 'a': 0, 'p2': 3, 'b': 2, 'E': 5.0, 'S': 10}
            {'q': 11, 'p': 2, 'p1': 2, 'a': 2, 'p2': 3, 'b': 2, 'E': 6.5, 'S': 13}
            {'q': 13, 'p': 3, 'p1': 2, 'a': 3, 'p2': 2, 'b': 3, 'E': 8.0, 'S': 16}
            {'q': 29, 'p': 2, 'p1': 2, 'a': 2, 'p2': 3, 'b': 3, 'E': 15.5, 'S': 31}
            {'q': 17, 'p': 13, 'p1': 2, 'a': 0, 'p2': 29, 'b': 1, 'E': 15.0, 'S': 30}

