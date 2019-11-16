def main():
    cripto = input("Cual es el nombre de su Criptomoneda?")
    cant = float(input("Que cantidad de Criptomonedas posee?"))
    dias = int(input("Cuantos dias negociara la criptomoneda?"))
    ganancia = float(input("Cuanta es la ganancia esperada por dia?"))
    ganancia_total = ((cant*ganancia)/100)*dias
    cant_total = cant + ganancia_total
    print("La ganancia de",cripto,"durante los ",str(dias),"dias es",str(ganancia_total))
    print("El monto total de",cripto,"a los",str(dias),"dias es de",str(cant_total))
main()
