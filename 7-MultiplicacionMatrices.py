'''Programa 1: SUMA EREW
Estudiante: José Juan García Romero'''

import threading
import math
import time
import numpy as np

def MatMultCREW(A, B, C, i, j, k):
    C[i][j][k] = A[i][k] * B[k][j]

def suma(C, i, j, k, L):
    if ((2 * (k + 1)) % (2 ** L) == 0):
        C[i][j][2 * k] = C[i][j][2 * k] + C[i][j][2 * k - 2 ** (L)]

def MultiplicacionCREW(A, B, C, N):
    threads = []
    log = int(math.log(N, 2))

    for i in range(0, N):
        for j in range(0, N):
            for k in range(0, N):
                thread = threading.Thread(target=MatMultCREW, args=(A, B, C, i, j, k))
                threads.append(thread)
                thread.start()

            for hilo in threads:
                hilo.join()
            threads = []

    for L in range(0, log):
        for i in range(0, N):
            for j in range(0, N):
                for k in range(0, int(N / 2)):
                    thread = threading.Thread(target=suma, args=(C, i, j, k, L))
                    threads.append(thread)
                    thread.start()

                for hilo in threads:
                    hilo.join()
                threads = []

def Aux(N):
    C = []
    m_aux = 0
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []
            for k in range(0, N):
                aux1.append(m_aux)
                m_aux += 1
            aux0.append(aux1)
        C.append(aux0)
    return C

def Matriz(M):
    cad = ""
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []

            for k in range(0, N):
                cad += str(M[i][j][k]) + ', '

            cad += '\t'

        cad += '\n'
    print("\nMatriz:")
    print(cad)

def ResultadoDeMatriz(M):
    cad = ""
    for i in range(0, N):
        aux0 = []
        for j in range(0, N):
            aux1 = []
            for k in range(0, 1):
                cad += (' '+str(M[i][j][k])+' ')

            #cad += '\t'

        cad += '\n'

    print('Resultado:')
    print(cad)

A = np.array([[1,2],[3,4]])
B = np.array([[4,3],[2,1]])

N = 2

C = Aux(N)

print('\n--------------------------------------------\n')
print('Programa 7. MULTIPLICACIÓN DE MATRICES CREW\n')
print('--------------------------------------------\n')
time.sleep(2)
print("Matriz A:")
print(A)
time.sleep(2)
print('\n')
print("Matriz B:")
print(B)
time.sleep(2)
print('\n')

MultiplicacionCREW(A, B, C, N)

ResultadoDeMatriz(C)