from Funciones import desordenar


def adivinar (L:list) ->int:
    L=desordenar.func(L)
    acertada=0
    for i in L:
        print(i[1]) #imprime la primera palabra desordenada
        palabra=i[0].replace("-","") #le quito los guiones a la palabra ordenada
        ok=input().upper()           #lo pongo todo en mayuscula
        print()
        if (ok==palabra):     #si la palabra es igual...
              print("Adivinaste\n")
              acertada+=1
        else:
            print(i[0],"\n")       #si no adivinas imprime la palabra correcta
    print()
    print("Cantidad de palabras acertadas:",acertada,"\n")
    return(acertada)        #retorna para usarla como libreria




if __name__=="__main__":
    print ("Adivina la palabra")
    L=["vaca","perro","gato","silla","mesa"]
    acertada=adivinar (L)