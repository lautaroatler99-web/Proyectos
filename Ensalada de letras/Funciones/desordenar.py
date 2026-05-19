
import random

def func (L:list)-> list:
    assert (len(L)>=5),"Hay menos de 5 elementos"
    NuevaLista=[]       #creo una nueva lista
    for i in (L):
        assert (type(i)==str),"Un e lemento de la lista no es string"
        palabra=i.upper() #lo pongo en mayuscula
        desordenada="".join(random.sample(palabra,len(palabra))) #la desordena
        while (palabra==desordenada): #comprueba que el desordenamiento no sea igual a la palabra original
            desordenada=(random.sample(palabra,len(palabra))) #si es igual la vuelve a desordenar hasta que no coincida con la original
        desordenada="-".join(random.sample(palabra,len(palabra))) #le pone un guion entre cada caracter
        tupla=(palabra,desordenada) #la guardo en una tupla
        NuevaLista.append(tupla) #agrego la tupla a la lista
    NuevaLista=(random.sample(NuevaLista,5)) #la lista se desordena con solo 5 elementos
    return(NuevaLista)


if __name__=="__main__":            #si ejecuto el archivo, esto se ejecuta. si lo uso como libreria, no se ejecuta
    L=["vaca","perro","gato","silla","mesa","pajaro"]

    try:
        print(func(L))
    except AssertionError as M:
        print(M)

