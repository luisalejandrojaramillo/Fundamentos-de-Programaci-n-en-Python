def capturar_moneda():
    cripto = input("Ingrese el nombre la moneda: ")
    cant = float(input("Ingrese la cantidad de la moneda: "))
    cotiz = float(input("Ingrese la cotización en USD de la moneda: "))
    return (cant*cotiz)

def main():
    valor,i=0,0
    while i < 5:
        valor = valor + capturar_moneda()
        i+=1
    print("Usted tiene",valor,"Dólares Americanos")        
main()
