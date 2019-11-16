from datetime import datetime
def main():
    nombreCripto=input("Digite el Nombre de la Criptomoneda")
    cantC=float(input("Digite la cantidad acumulada de la Criptomoneda"))
    cotizacion=float(input("Digite la cotización por US$ del día de la Criptomoneda"))
    date = datetime.now()
    print("La fecha completa y hora en la que obtuvo la información fue:"+str(date))
    inicial= cantC * cotizacion
    print("Ud. Posee un total de US$ "+str(inicial))
    dia1=inicial*1.05
    dia2=dia1*1.05
    dia3=dia2*1.05
    dia4=dia3*1.05
    dia5=dia4*1.05
    dia6=dia5*1.05
    dia7=dia6*1.05
    ganancia= dia7-inicial
    print("Su ganancia luego de una semana es: "+str(ganancia)+" USD")
main()
