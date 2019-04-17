import socket
serverName="localhost"
serverPort=12000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('FIEK Klienti: ')

while True:
    print('---------------------------->FUNKSIONET<----------------------------')
    print('->Shtypni NUMRIIPORTIT per te gjetur portin tuaj')
    print('->Shtypni IPADRESA per te gjetur ip addressen tuaj')
    print('->Shtypni PRINTIMI{hapesire}teksti per te printuar nje tekst')
    print('->Shtypni BASHKETINGLLORE{hapesire}fjalia ose fjala te ciles do ti numerohen bashketinglloret')
    print('->Shtypni EMRIIKOMPJUTERIT per te ditur emrin e klientit')
    print('->Shtypni TIME nese doni te dini oren dhe daten aktuale')
    print('->Shtypni LOJA nese doni te shihni numra te rendomte')
    print('->Shtypni FIBONACCI{hapesire}numrin per te cilin do te gjendet vargu i Fibonaccit')
    print('->Shtypni FACTORIAL{hapesire}numrin per te cilin do te gjendet vlera e Faktorielit')
    print('->Shtypni KONVERTIMI{hapesire}Opsioni{hapesire}Numri')
    print('\tOpsionet: KilowattToHorsepower,  \n\t\tHorsepowerToKilowatt,  \n\t\tDegreesToRadians, \n\t\tRadiansToDegrees,  \n\t\tGallonsToLiters,  \n\t\tLitersToGallons')
    print('->Shtypni ZARI per te hedhur zarin')
    print('->Shtypni MADHESIA{hapesire}fjala ose fjalia per te gjetur karakterin me te madh sipas ASCII kodit')
    var=input('->Shkruani kerkesen ose 0 per dalje: ')
    mesazhi = var
    s.sendto(str.encode(mesazhi), (serverName, serverPort))
    if mesazhi != '0':
        data=s.recv(128).decode('UTF-8')
        print(data)
    else:
        break

    print()
s.close()




