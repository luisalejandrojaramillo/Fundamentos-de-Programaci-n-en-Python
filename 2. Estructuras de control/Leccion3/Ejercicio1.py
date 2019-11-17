import random

def main():
    moneda=input("Ingrese la moneda: ")
    cantidad=float(input("Ingrese la cantidad de "+moneda+": "))
    count=0
    for count in range(7):
        profit=random.uniform(-0.03,0.03)
        cantidad=cantidad+(cantidad*profit)
        print("Saldo de",moneda,"el dia",count+1,"es de: %6.7f"%cantidad+". Ganacia de %6.2f"%(profit*100),"%")
main()
