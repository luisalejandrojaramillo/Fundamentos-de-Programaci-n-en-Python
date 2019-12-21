import random
import requests
from datetime import datetime
#Para ejecutar se utiliza> python Final.py  (desde la consola)
def mosMon(mon,dMio,dPrecio):#para imprimir lo que se debe mostrar de las monedas
    print(mon.upper())
    print("Es este momento usted posee:",dMio[mon],mon.upper())
    print("Lo cual equivale a:",str(dMio[mon]*dPrecio[mon]),"USD")

def is_int(dat): #Para validar si es dato ingresado es un numero
    try:
        int(dat)
        return True
    except:
        print("Error: Tipo de dato INVALIDO")
        return False

def printMat(lis):
    for i in lis:
        for j in i:
            print(j,end='\t\t')
        print('')

def creaDictP():
    d = {}
    btcdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")).json()
    d['btc']=float(btcdata["price"])#Bitcoin
    ethdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")).json()
    d['eth']=float(ethdata["price"])#Ethereum
    xrpdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT")).json()
    d['xrp']=float(xrpdata["price"])#XRP
    bchdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=BCHUSDT")).json()
    d['bch']=float(bchdata["price"])#Bitcoin Cash
    ltcdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT")).json()
    d['ltc']=float(ltcdata["price"])#Litecoin
    eosdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=EOSUSDT")).json()
    d['eos']=float(eosdata["price"])#EOS
    bnbdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT")).json()
    d['bnb']=float(bnbdata["price"])#Binance Coin
    xtzdata = requests.get(("https://api.binance.com/api/v3/ticker/price?symbol=XTZUSDT")).json()
    d['xtz']=float(xtzdata["price"])#Tezos
    return d
    
def main():
    cond = "1"
    #Variables que se utilizan en toda la ejecicion
    miCode = random.randint(1000,5000) #Este es el codigo de Nuestro usuario
    historial = [['Fecha(D/M/A)','Moneda','Tipo Op','C Orig','C Dest','Monto(USD)']]
    dPrecio = creaDictP()
    dMio = {}
    #Fin Creacion.
    while cond in ['1','2','3','4','5','6']:
        print("-----------------------------------------------------")
        print("Ha ingresado con el CODIGO:",miCode)
        print("Bienvenido al Glosario de terminos de Criptomonedas.")
        print("Digite 1 para Recibir cantidad.")
        print("Digite 2 para Transferir monto.")
        print("Digite 3 para Mostrar balance de una moneda.")
        print("Digite 4 Mostrar balance general.")
        print("Digite 5 Mostrar histórico de transacciones.")
        print("Digite 6 para SALIR.")
        print("-----------------------------------------------------")
        print("Notas:")
        print("- El Dinero esta en USD")
        print("- Solo se aceptan las sigientes monedas (se pone la abreviatura, es decir lo que esta entre parentesis)")
        print("Bitcoin(BTC), Ethereum(ETH), XRP(XRP), Bitcoin Cash(BCH), Litecoin(LTC), EOS(EOS), Binance Coin(BNB)& Tezos(XTZ)")
        print("-----------------------------------------------------")
        cond = input("").strip()#Siguiente Menu
        #Aca van a estar las variables que vamos a utilizar en el programa 
        fecha = str(datetime.now().day)+' / '+str(datetime.now().month)+' / '+str(datetime.now().year)
        h = [0,0,0,0,0,0]
        #Fin Creacion.
        #Inicio del MENU        
        if cond == '1':
            print("1")
            cRem = random.randint(1000,5000) #Este es el codigo del que Manda, suponiendo que alguien manda
            crip = input("Que Criptomoneda va a recibir ?").lower().strip()
            if crip in dPrecio: #Las preguntas se que no tienen seguridad, pero son para fines didacticos 
                if cRem != miCode:      
                    cant = int(input("Que cantidad va a recibir ?"))
                    if crip in dMio:
                        dMio[crip]+=cant
                    else:
                        dMio[crip]=cant
                    h=[fecha,crip.upper(),'Recibir',str(cRem),str(miCode),str(cant*dPrecio[crip])]
                    historial.append(h)
                    print("Transacción EXITOSA !!")
                else:
                    print("ERROR: El codigo de Origen y Destino no puede ser el mismo.")
            else:
                print("ERROR: La Criptomoneda puesta no es aceptada en esta plataforma.")
        elif cond == '2':
            print("2")
            varC = False
            while not varC:
                cDes = input("Ingrese el codigo del Destino.")
                varC = is_int(cDes) #Verifica que lo ingresado sea un entero
                if (varC and not(1000<=int(cDes)<=5000)):
                    varC = False
                    print("ERROR: El codigo debe estar entre 1000 y 5000")
                if (varC and (int(cDes)==miCode)):
                    varC = False
                    print("ERROR: El codigo de Origen y Destino no puede ser el mismo.")
            crip = input("Que Criptomoneda va a enviar ?").lower().strip()
            if crip in dMio:
                cant = int(input("Que cantidad va a enviar?"))
                if dMio[crip] >= cant:
                    dMio[crip] -= cant
                    h=[fecha,crip.upper(),'Enviar',str(miCode),str(cDes),str(cant*dPrecio[crip])]
                    historial.append(h)
                    print("Transacción EXITOSA !!")
                else:
                    print("ERROR: Usted no posee SUFICIENTES",crip,"Para realizar esta transaccion.")
            else:
                print("ERROR: Usted no posee",crip+'.')    
        elif cond == '3':
            print("3")
            mon = input("Que moneda va a Buscar ?").lower().strip()
            if mon in dMio:
                mosMon(mon,dMio,dPrecio)
            else:
                print("ERROR: Usted no posee",mon+'.')   
        elif cond == '4':
            print("4")
            lisC = list(dMio.keys())
            for i in lisC:
                mosMon(i,dMio,dPrecio)    
        elif cond == '5':
            print("5. Historial")
            printMat(historial)#Funcion creada para imprimir matriz
        elif cond == '6':
            cond = '7' #Para que salga
            print("Hasta la proxima !!.")
        else:
            cond = '1' #Para que se repita
            print("Caracter INVALIDO, por favor digite nuevamnete.")
            
main()
