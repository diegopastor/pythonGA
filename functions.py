# ------------- IMPORTS ------------------
import random
from math import sin, cos
# ----------------------------------------

# ------------- FUNCTIONS ----------------
def genSudoBinaryCode(n):
        n = int(n)
        intSquares = [2**i for i in range(-20,100) if 2**i < n]
        for i in range(len(intSquares)):
            if sum(intSquares[0:i+1]) > n:
                intSquares.pop(i)

        sobrante = n - (intSquares[len(intSquares)-1] + intSquares[len(intSquares)-1]-1)
        intSquares.append(sobrante)
        intSquares = sorted(intSquares)

        intSquares.append('+/-')

        return intSquares[::-1]

def genNArraysOf(x,y,u1):
    arrs = []
    for i in range(x):
        arr = []
        for j in range(y):
            if random.uniform(0,1) > u1:
                arr.append(1)
            else:
                arr.append(0)

        arrs.append(arr)
    return arrs

def getValuesOfXandY(randVals, sudoBinaryCode): 
    values = []
    for randVal in randVals:
        xs = []
        ys = []
        for i, j in zip(randVal[:len(randVal)//2], sudoBinaryCode[:15]):
            if j == '+/-':
                xs.append(i)
            else:
                xs.append(i*j)

        for i, j in zip(randVal[len(randVal)//2:], sudoBinaryCode[:15]):
            if j == '+/-':
                ys.append(i)
            else:
                ys.append(i*j)

        values.append([randVal, sum(xs), sum(ys)])
        
    return values

def f(x,y):
    return -(x * sin(x)**2 * cos(x)**3 + (y * sin(y)**2 * cos(y)**3))

def f(x,y):
    return x + y

def getPofEach(arr):
    arr = [abs(i) for i in arr]
    total = sum(arr)
    ps = []
    for element in arr:
        ps.append(element/total)
    return ps

def getPA(arr):
    pa = []
    s = 0
    for element in arr:
        s += element
        pa.append(s)
    return pa

def bestK(arrOfArrs,k):
    return sorted(arrOfArrs, key=lambda x: x[3])[:k]

def crossElements(e1,e2):
    xe1 = e1[:15]+e2[15:30]+e1[30:45]+e2[45:60]
    xe2 = e2[:15]+e1[15:30]+e2[30:45]+e1[45:60]
    return xe1, xe2
    
def mutate(element,uM):
    if random.uniform(0,1) > uM:
        return [0 if i else 1 for i in element]
    else:
        return element

# ----------------------------------------

# Inputs ( Esto se va a cambiar de STDIN a lo que se reciba de un request HTTP)
poblacion, numKdeElitismo, cantidadGeneraciones = [int(x) for x in input().split(' ')]
umbral1, umbralX, umbralM = [float(x) for x in input().split(' ')]

sudoBinCode = genSudoBinaryCode(360)
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# -----------FIRST GENERATION-------------
# ----------------------------------------
# ----------------------------------------
# Generar los N arreglos de 1's y 0's y su valor de X y Y dado el umbral1
firstGeneration = (
        getValuesOfXandY(
                genNArraysOf(poblacion,60,umbral1),
                sudoBinCode
        )
    )
# Generar Valores de f(x,y) para cada uno de los arreglos de 1's y 0's
for element in firstGeneration:
    element.append(f(element[1],element[2]))
# Agregar P(f(x,y)) y PA(f(x,y)) a cada Arreglo de 1's y 0's
probabilidades = getPofEach([element[3] for element in firstGeneration])
probabilidadesAcumuladas = getPA(probabilidades)

for element, i in zip(firstGeneration, range(len(probabilidades))):
    element.append(probabilidades[i])
    element.append(probabilidadesAcumuladas[i])

# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# ------SUBSEQUENT GENERATIONS------------
# ----------------------------------------
# ----------------------------------------
previousGeneration = sorted(firstGeneration, key=lambda x: x[5])
print(previousGeneration)
for generacion in range(cantidadGeneraciones):
    # Obtener los mejores K elementos de la generacion anterior
    bestOfPreviousGeneration = (bestK([element[0] for element in previousGeneration], numKdeElitismo))

    # Pasar esos K elementos a a la siguiente generación y el resto (N-K) Cruzar si pasan Umbral o no Cruzar si no pasan y Mutar si pasan
    nextGeneration = bestOfPreviousGeneration
    while len(nextGeneration) < poblacion:
        numeroAleatorio = random.uniform(0,1)
        for element in previousGeneration:
            if numeroAleatorio >= element[5]:
                father = element[0]
            
        numeroAleatorio = random.uniform(0,1)
        for element in previousGeneration:
            if numeroAleatorio >= element[5]:
                mother = element[0]
         
        if numeroAleatorio > umbralX: 
            child1, child2 = crossElements(father,mother)
        else:
            child1, child2 = father, mother

        nextGeneration.append(mutate(child1,umbralM))
        nextGeneration.append(mutate(child2,umbralM))

    # Generar valor de X y Y 
    nextGeneration = (
            getValuesOfXandY(
                    nextGeneration,
                    sudoBinCode
            )
        )
    # Generar Valores de f(x,y) para cada uno de los arreglos de 1's y 0's de siguiente generación
    for element in nextGeneration:
        element.append(f(element[1],element[2]))

    # Agregar P(f(x,y)) y PA(f(x,y)) a cada Arreglo de 1's y 0's a siguiente generacion
    probabilidades = getPofEach([element[3] for element in nextGeneration])
    probabilidadesAcumuladas = getPA(probabilidades)

    for element, i in zip(nextGeneration, range(len(probabilidades))):
        element.append(probabilidades[i])
        element.append(probabilidadesAcumuladas[i])

    previousGeneration = sorted(nextGeneration, key=lambda x: x[5])


# print("-"*50)
# print("f(x,y)s of firstGen")
# for element in sorted(firstGeneration, key=lambda x: x[5]):
#     print("f(x,y)", element[3])
# print("-"*50)
# print("f(x,y)s of lastGen")
# for element in sorted(nextGeneration, key=lambda x: x[5]):
#     print("f(x,y)", element[3])
# print("-"*50)
# print("LastGen Best X: ",sorted(nextGeneration, key=lambda x: x[5])[0][1])
# print("LastGen Best Y: ",sorted(nextGeneration, key=lambda x: x[5])[0][2])
# print("LastGen Best f(x,y): ",sorted(nextGeneration, key=lambda x: x[5])[-1][3])
