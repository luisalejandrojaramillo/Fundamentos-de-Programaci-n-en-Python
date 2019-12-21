from datetime import datetime
def main():
    nombreC=input("Nombre de la Criptomoneda: ")
    cantCripto=float(input("Cantidad acumulada de la Criptomoneda: "))
    cotizacion=float(input("Cotización por US$ del día de la Criptomoneda: "))
    fecha = datetime.now()
    print("La fecha completa y hora en la que obtuvo la información fue:"+fecha.strftime("%A, %d de %B de %Y a las %I:%M:%S%p"))
main()
