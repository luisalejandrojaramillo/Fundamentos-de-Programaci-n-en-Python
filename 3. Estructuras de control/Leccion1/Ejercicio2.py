def main():
    i=0
    valor=0
    while i < 5:
        i+=1
        cripto = input("ingrese el nombre la moneda: ")
        cant = float(input("Ingrese la cantidad de la moneda: "))
        cotiz = float(input("Ingrese la cotización en USD de la moneda: "))
        valor = valor + (cant*cotiz)
    print("Usted tiene "+str(valor)+" Dólares Americanos")
main()
