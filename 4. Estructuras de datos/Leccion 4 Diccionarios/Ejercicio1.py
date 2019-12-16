import requests
def esmoneda(cripto):
    return cripto in monedas
def main():
    monedas=()
    monedas_dict={}
    data=requests.get("https://api.coinmarketcap.com/v2/listings/").json()
    for cripto in data["data"]:
        monedas_dict[cripto["symbol"]]=cripto["name"]
    monedas = monedas_dict.keys()
    moneda=input("Indique el nombre de la moneda a verificar: ")
    while not esmoneda(moneda):
            print("Moneda Invalida.")
            moneda=input("Ingrese el nombre de la moneda: ")
    else:
        print("La moneda con symbol:,",moneda,"y nombre:",monedas_dict.get(moneda),
              "es valida porque existe en coimnmarketcap.com")
main()
