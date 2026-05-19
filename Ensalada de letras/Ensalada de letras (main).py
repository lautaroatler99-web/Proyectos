from Funciones import adivinar
import json
import time
from pathlib import Path
import os
import sys

BASE_DIR = Path(__file__).resolve().parent #constante de la ruta principal

def reglas() ->None:
    dir_reglas=BASE_DIR / ("Resources") / ("reglas_ensalada_de_letras.txt")
    try:
        with open (dir_reglas,"r") as reglas:
            print(reglas.read())
    except:
        print("Archivo no encontrado")

def menu() ->None:
    print("""Ensalada de letras.
       1. Jugar
       2. Puntaje
       3. Reglas
       4. salir\n""")

def Imprimir_Puntaje() ->None:
    dir_puntaje=BASE_DIR / ("Resources") / ("puntaje.json")
    try:
        with open (dir_puntaje,"rt") as archivo:
            data=json.load(archivo)
            data=list(data.items())     #me quedo con los objetos del diccionario transformado
                                        #en tuplas y convertido en lista
                                        #[(clave,valor)] por lo tanto clave=i[0]
            print()
            print("NOMBRE          PUNTAJE")
            for i in data:
                time.sleep(1)
                nombre=i[0]
                if (len (nombre)<18): #18 es el rango que quiero que tenga de separacion
                    h=18-len(nombre)  #me quedo con la diferencia entre el nombre y el espacio que quiero
                    for j in range(h):
                        nombre=(nombre+" ") #le agrego espacio hasta alcanzar los 18 caracteres
                print(nombre.upper(),end="") #lo pongo en mayuscula
                print(i[1])                  #imprimo el puntaje
            print()
    except:
        print("Los puntajes no estan\n")
    time.sleep(1)

def Guardar (user:str,acertadas:int) ->None:
    puntaje=acertadas*200
    dir_puntaje=BASE_DIR / ("Resources") / ("puntaje.json")
    try:
        with open (dir_puntaje,"rt") as archivo:        #intento abrir el archivo
            data=json.load(archivo)
    except:
            with open (dir_puntaje,"wt") as archivo:   #si no existe lo creo
                data={}
    finally:
        if (user in data):                     #si el elemento existe..
            if(data[user]<puntaje):            #si el puntaje almacenado es menor al sacado recientemente..
                data[user]=puntaje             #reemplazo por el nuevo puntaje
        else:
            data[user]=puntaje                 #si no existe lo agrego
        with open (dir_puntaje,"wt") as archivo:   #abro archivo y agrego la informacion al .json
            json.dump(data,archivo)
            
def Jugar(palabras) ->None:
    acertadas=0
    while (True):
        print("""Elige categoria:
         1. Colores
         2. Animales
         3. Frutas
         4. Paises
         5. volver""")
        op=input()
        if (op>="1") and (op<="4"):         #si no es ninguna de las opciones tira ELSE
            user=input("Ingrese su usuario\n")
        if (op=="1"):
            acertadas=adivinar.adivinar(palabras["colores"])    #libreria
            Guardar(user,acertadas)
        elif (op=="2"):
            acertadas=adivinar.adivinar(palabras["animales"])   #libreria
            Guardar(user,acertadas)
        elif (op=="3"):
            acertadas=adivinar.adivinar(palabras["frutas"])     #libreria
            Guardar(user,acertadas)
        elif (op=="4"):
            acertadas=adivinar.adivinar(palabras["paises"])     #libreria
            Guardar(user,acertadas)
        elif (op=="5"):
            break
        else:
            print("Opcion invalida")

def inicio (palabras):
    menu()
    opcion=input()
    while (True):
        if (opcion=="1"):
            Jugar(palabras)
        elif (opcion=="2"):
            Imprimir_Puntaje()
        elif (opcion=="3"):
            reglas()
        elif (opcion=="4"):
            print("Adios")
            break
        menu()
        opcion=input()

dir_palabras=BASE_DIR / ("Resources") / ("palabras.json")
try:
    with open (dir_palabras,"r") as archivo: #leo el json con las palabras
        palabras=json.load(archivo)
        inicio(palabras)
except Exception as e:
    print ("No se pudo abrir el json de las palabras.")
    print(f"Error {e}")





