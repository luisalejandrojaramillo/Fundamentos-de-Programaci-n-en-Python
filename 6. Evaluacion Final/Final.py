import random
from datetime import datetime

def printMat(lis):
    for i in lis:
        for j in i:
            print(j,end='\t\t')
        print('')

def creaDictP():
    d = {}
    d['btc']=7210.98#Bitcoin
    d['eth']=129.47#Ethereum
    d['xrp']=0.189885#XRP
    d['usdt']=1.01#Tether
    d['bch']=187.50#Bitcoin Cash
    d['ltc']=40.06#Litecoin
    d['eos']=2.47#EOS
    d['bnb']=13.37#Binance Coin
    d['bsv']=85.36#Bitcoin SV
    d['xtz']=1.54#Tezos
    d['xlm']=0.045117#Stellar
    return d

def main():
    cond = "1"
    #Variables que se utilizan en toda la ejecicion
    miCode = random.randint(1000,5000) #Este es el codigo de Nuestro usuario
    historial = [['Fecha(D/M/A)','Moneda','Tipo Op','C Orig','C Dest','Monto']]
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
        print("Bitcoin(BTC), Ethereum(ETH), XRP(XRP), Tether(ETH), Bitcoin Cash(BCH), Litecoin(LTC), EOS(EOS), Binance Coin(BNB), Bitcoin SV(BSV), Stellar(XLM) & Tezos(XTZ)")
        print("-----------------------------------------------------")
        cond = input("").strip()#Siguiente Menu
        #Aca van a estar las variables que vamos a utilizar en el programa
        
        fecha = str(datetime.now().day)+' / '+str(datetime.now().month)+' / '+str(datetime.now().year)
        h = [0,0,0,0,0,0]
        #Fin Creacion.
        

        #Inicio del MENU        
        if cond == '1':
            print("1")
            cRem = random.randint(1000,5000) #Este es el codigo del que Manda
            crip = input("Que Criptomoneda va a recibir ?").lower().strip()
            if crip in dPrecio:
                if cRem != miCode:      
                    cant = int(input("Que cantidad va a recibir ?"))
                    if crip in dMio:
                        dMio[crip]+=cant
                    else:
                        dMio[crip]=cant
                    h=[fecha,crip,'Recibir',str(miCode),str(cRem),str(cant*dPrecio[crip])]
                    historial.append(h)
                else:
                    print("ERROR: El codigo de Origen y Destino no puede ser el mismo.")
            else:
                print("ERROR: La Criptomoneda puesta no es aceptada en esta plataforma.")
            
        elif cond == '2':
            print("2")
            
        elif cond == '3':
            print("3")
            
        elif cond == '4':
            print("4")
            
        elif cond == '5':
            print("5. Historial")
            printMat(historial)#Funcion creada para imprimir matriz
        elif cond == '6':
            cond = '7'
            print("Hasta la proxima !!.")
        else:
            cond = '1' #Para que se repita
            print("Caracter INVALIDO, por favor digite nuevamnete.")

main()
