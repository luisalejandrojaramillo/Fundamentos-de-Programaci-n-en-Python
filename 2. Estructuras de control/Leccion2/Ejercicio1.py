def main():
    BTCUSD=8502.04
    DASHUSD=60.06
    LTCUSD=58.59
    moneda=input("Ingrese la moneda a utilizar(BTC, DASH o LTC): ").upper()
    if moneda=="BTC" or moneda=="DASH" or moneda=="LTC":
        cantidad=float(input("Ingrese la cantidad a utilizar: "));
        if moneda=="BTC":
            monto=cantidad * BTCUSD;
        elif moneda=="DASH":
            monto=cantidad * DASHUSD;
        else:
            monto=cantidad * LTCUSD;
        print("La cantidad de USD recargado fue de: "+str(monto));
    else:
        print("Error: Solo se permite utilizar BTC, DASH o LTC");
main()
