def is_float(dat):
    try:
        float(dat)
        return True
    except:
        print("Error: Tipo de dato INVALIDO")
        return False

def main():
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    i=0
    total=0
    for i in range(3):
        cripto = input("Ingrese el nombre de la moneda: ").upper()
        if cripto in criptos:
            var = False
            while not var:
                cant = input("Indique la cantidad de "+cripto+":")
                var = is_float(cant)               
            var = False                
            while not var:
                cotiz = input("Indique la cotización en USD de "+cripto+":")
                var = is_float(cotiz)
            total = total + float(cant) * float(cotiz)
        else:
            print("Moneda invalida.")
    print("El tota en USD que tiene el usuario es de ",str(total))
main()
