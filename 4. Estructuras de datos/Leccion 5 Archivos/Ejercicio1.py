from sys import stdin
import sys
import fileinput
#Para ejecutar se debe hacer desde consola lo siguente:
#python3 nombre.py
def main():
    cond = "1"
    while (cond=="1" or cond=="2"):
        print("-----------------------------------------------------")
        print("Bienvenido al Glosario de terminos de Criptomonedas.")
        print("Digite 1 para buscar una palabra.")
        print("Digite 2 para añadir una parabla.")
        print("Digite otro valor para salir.")
        print("-----------------------------------------------------")
        cond = stdin.readline().strip()#Siguiente Menu
        d = {}#Nuestro diccionario
        name = 'glos.txt'·#Nombre del archivo que vamos a abir
        file = open(name,"r")#Modo lectura
        text = file.read()
        file.close()
        lines = text.strip().splitlines()
        for line in lines:
            l = line.strip().split("=")
            d[l[0][:-1]]=l[1][1:]#Añadimos a nuestro diciconario todo lo que este en nuestro txt
        if cond == "1":
            print("Modo Busqueda")
            pal = input("Ingrese la palabra a buscar")
            if pal in d:
                print(d[pal])
            else:
                print("La palabra no se encuentra en el Diccionario")           
        elif cond == "2":
            print("Modo Añadir")
            npal = input("Digite la palabra que va a añadir (Recuerde que las mayuculas son importantes)").strip()
            if npal in d:
                print("La palabra es INVALIDA ya que actualmente se encuentra en el diccionario.")
            else:
                ndef = input("Escriba de forma clara el significado").strip()
                tex = "\n" + npal + ' = ' + ndef
                file = open(name,"a")#Modo para añadir en la ultima linea
                file.writelines(tex)
                file.close()           
        else:
            print("Adios !!")
main()
