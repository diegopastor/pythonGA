import random
from math import sin, cos

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

def genNArraysOf(x,y):
    arrs = []
    for i in range(x):
        arr = []
        for j in range(y):
            if random.uniform(0,1) > 0.5:
                arr.append(1)
            else:
                arr.append(0)

        arrs.append(arr)
    return arrs

def getValuesOfXandY(randVals, sudoBinaryCode): 
    valuesOfX = []
    valuesOfY = []
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

        valuesOfX.append(sum(xs))
        valuesOfY.append(sum(ys))
        
    return valuesOfX, valuesOfY

def f(x,y):
    return -(x * sin(x)**2 * cos(x)**3 + (y * sin(y)**2 * cos(y)**3))

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

def bestK(arr,k):
    return sorted(arr)[:k]

# TESTS
# -----------------------------
# 1. Generar Codificacion Pseudo Binaria
# -----------------------------
# print(genSudoBinaryCode(360))
# -----------------------------
# 2. Generar arreglo de 1's y 0's aleatorio si pasan cierto umbral
# -----------------------------
# a = genNArraysOf(5,60)
# for arr in a:
#     print(arr)
# -----------------------------
# 3. Obtener los valores de X y Y dados los arreglosd de 1's y 0's aleatorios y la codificacion
# -----------------------------
# print(getValuesOfXandY(genNArraysOf(5,60),genSudoBinaryCode(360)))
# -----------------------------
# xys = (getValuesOfXandY(genNArraysOf(5,60),genSudoBinaryCode(360)))
# xs = xys[0]
# ys = xys[1]
# ps = [f(x,y) for x,y in zip(xs, ys)] 
# print(getPofEach(ps))
# print(getPA(getPofEach(ps)))
# print(bestK(ps,3))



# Recordar en memoria a que arreglos de 1's y 0's apuntan las k mejores f(x,y)'s
