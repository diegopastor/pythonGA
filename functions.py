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
    return sorted(arrOfArrs, key=lambda x: x[3], reverse=True)[:k]

def crossElements(e1,e2):
    xe1 = e1[:15]+e2[15:30]+e1[30:45]+e2[45:60]
    xe2 = e2[:15]+e1[15:30]+e2[30:45]+e1[45:60]
    return xe1, xe2
    
def mutate(element):
    return [0 if i else 1 for i in element]

# ----------------------------------------

# Inputs ( Esto se va a cambiar de STDIN a lo que se reciba de un request HTTP)
poblacion, numKdeElitismo, cantidadGeneraciones = [int(x) for x in input().split(' ')]
umbral1, umbralX, umbralM = [float(x) for x in input().split(' ')]

sudoBinCode = genSudoBinaryCode(360)
print(sudoBinCode)
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

print("-"*50)
print("-> GENERACION #0")
for element in firstGeneration:
    print("X: ",element[1]," Y: ",element[2]," f(x,y): ", element[3])
bG = bestK(firstGeneration,1)
print("Best X: ",bG[0][1]," Best Y: ",bG[0][2]," Best f(x,y): ",bG[0][3])
# ----------------------------------------
# ----------------------------------------
# ----------------------------------------
# ------SUBSEQUENT GENERATIONS------------
# ----------------------------------------
# ----------------------------------------
previousGeneration = firstGeneration

for generacion in range(cantidadGeneraciones):
    # Obtener los mejores K elementos de la generacion anterior
    bestOfPreviousGeneration = (bestK(previousGeneration, numKdeElitismo))
    bestOfPreviousGeneration = [element[0] for element in bestOfPreviousGeneration]

    # Pasar esos K elementos a a la siguiente generación y el resto (N-K) Cruzar si pasan Umbral o no Cruzar si no pasan y Mutar si pasan
    nextGeneration = bestOfPreviousGeneration
    while len(nextGeneration) < poblacion:
        numeroAleatorio = random.uniform(0,.98)
        for element in previousGeneration:
            if element[5] >= numeroAleatorio:
                father = element[0]
            
        numeroAleatorio = random.uniform(0,.98)
        for element in previousGeneration:
            if element[5] >= numeroAleatorio:
                mother = element[0]

        # Si son el mismo escoger otro 
        numeroAleatorio = random.uniform(0,1)
        if numeroAleatorio > umbralX: 
            child1, child2 = crossElements(father,mother)
        else:
            child1, child2 = father, mother

        numeroAleatorio = random.uniform(0,1)
        if numeroAleatorio > umbralM:
            nextGeneration.append(mutate(child1))
            nextGeneration.append(mutate(child2))
        else:
            nextGeneration.append(child1)
            nextGeneration.append(child2)

    # Generar valores de X y Y para todos los elementos de la nueva generacion
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

    previousGeneration = nextGeneration

    print("-"*50)
    print("-> GENERACION #", generacion+1)
    for element in nextGeneration:
        print("X: ",element[1]," Y: ",element[2]," f(x,y): ", element[3])
    bG = bestK(nextGeneration,1)
    print("Best X: ",bG[0][1]," Best Y: ",bG[0][2]," Best f(x,y): ",bG[0][3])






