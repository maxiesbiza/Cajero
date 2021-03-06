# -*- coding: utf-8 -*-
"""Cajero.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GgV0ixyQY0_HnnYNq_nl5NbIcYaFB1lM
"""

from google.colab import files
import numpy as np

def generarMatriz(cola):
    A = np.matrix([["Mechanic", "Time Between Arrivals", "Arrival Time", "One-teller Election","C1 - Service Time", "C1 - Service Begins", "C1 - Time Service Ends", "C1 - Idle Time", "C2 - Service Time", "C2 - Service Begins", "C2 - Time Service Ends", "C2 - Idle Time", "Time in System", "Time in Queue"]])


    B = np.zeros((20,14))

    #1ra instancia
    B[0][0] = 1
    B[0][1] = 0
    B[0][2] = 0
    B[0][3] = np.random.randint(low=1, high=3)

    if (B[0][3] == 1):
        B[0][4] = np.random.randint(low=1, high=7)
        B[0][5] = 0
        B[0][6] = B[0][4] + B[0][5]
        B[0][7] = 0
        B[0][8] = 0
        B[0][9] = 0
        B[0][10] = B[0][8] + B[0][9]
        B[0][11] = 0
    else:
        B[0][4] = 0
        B[0][5] = 0
        B[0][6] = B[0][4] + B[0][5]
        B[0][7] = 0
        B[0][8] = np.random.randint(low=1, high=7)
        B[0][9] = 0
        B[0][10] = B[0][8] + B[0][9]
        B[0][11] = 0

    B[0][12] = np.maximum(B[0][6], B[0][10]) - B[0][2]
    B[0][13] = 0


    #Resto de instancias
    for i in range (1, 20):
        #Mechanic
        B[i][0] = i+1
        
        #Time Between Arivals
        B[i][1] = np.random.randint(low=1, high=7)
        
        #Arrival Time
        B[i][2] = B[i-1][2] + B[i][1]
        
        #One-teller Election
        if (cola == 2):
            B[i][3] = np.random.randint(low=1, high=3)
        else:
            if (B[i-1][6] < B[i-1][10]):
                B[i][3] = 1
            else:
                B[i][3] = 2
                
        if (B[i][3] == 1):
            #C1 - Service Time
            B[i][4] = np.random.randint(low=1, high=7)
            
            #C1 - Service Begins
            B[i][5] = np.maximum(B[i-1][6], B[i][2])
            
            #C1 - Time Service Ends
            B[i][6] = B[i][4] + B[i][5]
            

            #C2 - Service Time
            B[i][8] = 0
            
            #C2 - Service Begins
            B[i][9] = B[i-1][9]
            
            #C2 - Time Service Ends
            B[i][10] = B[i-1][10]

        else:
            #C1 - Service Time
            B[i][4] = 0
            
            #C1 - Service Begins
            B[i][5] = B[i-1][5]
            
            #C1 - Time Service Ends
            B[i][6] = B[i-1][6]

            
            #C2 - Service Time
            B[i][8] = np.random.randint(low=1, high=7)
            
            #C2 - Service Begins
            B[i][9] = np.maximum(B[i-1][10], B[i][2])
            
            #C2 - Time Service Ends
            B[i][10] = B[i][8] + B[i][9]

        #C1 - Idle Time
        if (B[i][2] > B[i-1][6]):
            B[i][7] = B[i][2] - B[i-1][6]
        else:
            B[i][7] = 0

        #C2 - Idle Time
        if (B[i][2] > B[i-1][10]):
            B[i][11] = B[i][2] - B[i-1][10]
        else:
            B[i][11] = 0

        #Time in System
        if (B[i][3] == 1):
            B[i][12] = B[i][6] - B[i][2]
        else:
            B[i][12] = B[i][10] - B[i][2]

        #Time in Queue
        if (B[i][3] == 1):
            B[i][13] = B[i][5] - B[i][2]
        else:
            B[i][13] = B[i][9] - B[i][2]

    AB=np.append(A,B,axis=0)
    if (cola == 1):
      print("Simulacion de dos cajeros para una cola",'\n')
    else:
      print("Simulacion de dos cajeros para dos colas", '\n')
    print(AB,'\n','\n','\n')
    return B


matrizUnaCola = generarMatriz(1)
matrizDosColas = generarMatriz(2)
encabezado = "Mechanic, Time Between Arrivals, Arrival Time, One-teller Election, C1 - Service Time, C1 - Service Begins, C1 - Time Service Ends, C1 - Idle Time, C2 - Service Time, C2 - Service Begins, C2 - Time Service Ends, C2 - Idle Time, Time in System, Time in Queue"

np.savetxt('SimulacionCajerosDosFilas.csv', matrizDosColas, delimiter=',', fmt='%d', header=encabezado, comments='')
np.savetxt('SimulacionCajerosUnaFila.csv', matrizUnaCola, delimiter=',', fmt='%d', header=encabezado, comments='')
files.download("SimulacionCajerosDosFilas.csv")
files.download("SimulacionCajerosUnaFila.csv")