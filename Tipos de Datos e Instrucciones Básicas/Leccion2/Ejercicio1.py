def main():
    
    nombreC = input("Digite el nombre de la Criptomoneda: ")
    cantidadC = float(input("Cantidad que tiene de la Criptomoneda: "))
    calorC = float(input("A cuanto equivalr en US$ la Criptomoneda: "))
    res= cantidadC * calorC
    print("Ud. Posee un total de US$ "+str(res))

main()
