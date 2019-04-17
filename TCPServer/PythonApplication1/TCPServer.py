# Importimi i librarise socket per krijimin e socketave per lidhje
from socket import *
from _thread import * 
import datetime
import random
import math

# Porti i serverit, ne te cilin do te pritet per komunikim

serverPort=12000 
serverSocket=socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('', serverPort)) 
print('Serveri u startua ne localhost: '+str(serverPort))
print('-----------------------------------')
# Maksimumi i klientave qe mund te lidhen me server
serverSocket.listen(5) 
print('Serveri eshte i gatshem te pranoje kerkese ') 
print('------------------------------------------')



#Metoda Bashketingllore
def bashketingellore(fjalia):
    bashketingellore = ['B', 'C','Ç' 'D','DH','F','G','GJ','H', 'J','K','L','LL','M','N',
                        'NJ','P','Q', 'R','RR','S','SH','T','TH','V','X','XH','Z','ZH',
                        'b','c','ç','d','dh','f','g','gj','h','j','k','l','ll','m','n',
                        'nj','p','q','r','rr','s','sh','t','th','v','x','xh','z','zh']
    count=0
    for shkronja in fjalia:
        if(shkronja in bashketingellore):
            count=count+1
    return count

 #Metoda EMRIIKOMPJUTERIT
def Host():
       try:
           host=gethostname()
           return host
       except socket.error:
           return "Emri i hostit nuk mund te gjendet!"


 #Metoda Koha
def timenow():
    time=datetime.datetime.now()           
    return time.strftime("%d-%m-%Y %I:%M:%S %p")

   #Metoda Loja     
def loja():
    listaNumrave=""
    for number in range(0,7): 
        numriRandom=random.randint(1,49)
        listaNumrave+=str(numriRandom)
        if number!=6:
           listaNumrave+=", "
    return listaNumrave

  #Metoda Fibonacci
def fibonacci(num):
    if num==0:
        return 0;
    elif num == 1:
        return 1;
    elif num < 0:
         return "Numri eshte me i vogel se zero!"
    else:
        return fibonacci(num-1)+fibonacci(num-2);


   #Metoda Konvertimi
def konvertimi(opsioni, vlera):
    if opsioni=="KilowattToHorsepower":
        rezultati=vlera*1.34

    elif opsioni=="HorsepowerToKilowatt":
        rezultati=vlera/1.34 

    elif opsioni=="DegreesToRadians":
        rezultati = (vlera * (math.pi/ 180))


    elif opsioni=="RadiansToDegrees":
        rezultati = (vlera * (180/math.pi))

    elif opsioni=="GallonsToLiters":
         rezultati = vlera * 3.785

    elif opsioni=="LitersToGallons":
        rezultati = vlera/3.785
    else:
        rezultati="Gabim"
    return '%.2f' %(rezultati)

#Metoda Faktorieli
def factorial(nr):
    if nr<=1:
        return 1
    else:
        return nr*factorial(nr-1)

#Metoda Madhesia
def madhesia(fjalia):
    shkronja = 'A'
    fjalia=fjalia.upper()
    for S in fjalia:
        if ord(S) > ord(shkronja):
            shkronja = S
    return shkronja



'''
    Funksioni client_handler ka 2 parametra, i pari eshte socketi i lidhjes me nje client i dyti esht adresa e klientit,
'''
def client_handler(connectionSocket, addr):
    while 1:

        fjalia = connectionSocket.recv(128)

        if fjalia.decode('UTF-8').upper() == 'KOMANDAT':
            komandat = ''
            komandat += '---------------------------->FUNKSIONET<----------------------------\n'
            komandat += '->Shtypni IPADRESA per te gjetur ip addressen tuaj\n'
            komandat += '->Shtypni NUMRIIPORTIT per te gjetur portin tuaj\n'
            komandat += '->Shtypni BASHKETINGLLORE per te numruar numrin e bashketinglloreve ne nje fjale ose fjali\n'
            komandat += '->Shtypni PRINTIMI per te printuar ate qe keni shenuar\n'
            komandat += '->Shtypni EMRIIKOMPJUTERIT per te ditur emrin e klientit\n'
            komandat += '->Shtypni TIME nese doni te dini oren dhe daten aktuale\n'
            komandat += '->Shtypni LOJA nese doni te shihni numra te rendomte\n'
            komandat += '->Shtypni FIBONACCI pastaj numrin per te cilin gjendet vargu i Fibonaccit\n'
            komandat += '->Shtypni KONVERTIMI per te bere konvertimin e numrave\n'
            komandat += '->Shtypni ZARI per te hedhur zarin\n'
            komandat += '->Shtypni FACTORIAL per te gjetur faktorielin e nje numri \n'
            komandat += '->Shtypni MADHESIA per te gjetur karakterin me te madh sipas ASCII kodit\n'

            connectionSocket.send(komandat.encode('UTF-8'))
            fjalia = connectionSocket.recv(1024)

        # Ruan ne nje variabel kerkesen me shkronja te medha
        FjaliaMeShkronjaTeMedha=fjalia.upper()
    
        rcvCMD = FjaliaMeShkronjaTeMedha.decode('UTF-8')

        if rcvCMD == 'PRINTIMI':
            # Pas pranimit te fjales PRINTO, pret per nje fjale tjeter nga klienti
            mesazhi = connectionSocket.recv(128).decode('UTF-8')
            mesazhi = 'Fjalia e dhene eshte: ' + mesazhi
            connectionSocket.send(mesazhi.encode('UTF-8'))
        elif rcvCMD == 'EMRIIKOMPJUTERIT':
            response = 'Emri i klientit eshte: ' + Host()
            connectionSocket.send(response.encode('UTF-8'))
        elif rcvCMD == 'IPADRESA':
            connectionSocket.send(str.encode(addr[0]))
        elif rcvCMD == 'NUMRIIPORTIT':
            response = 'Porti i serverit eshte ' + str(addr[1])
            connectionSocket.send(str.encode(response))
        elif rcvCMD == 'BASHKETINGLLORE':
            fjalia = connectionSocket.recv(128).decode('UTF-8')
            pergjigja = 'Numri i bashketingllore eshte: ' + str(bashketingellore(fjalia))
            connectionSocket.send(pergjigja.encode('UTF-8'))
        elif rcvCMD == 'TIME':
            koha = 'Koha eshte: ' + str(timenow())
            connectionSocket.send(koha.encode('UTF-8'))
        elif rcvCMD == 'LOJA':
            response = 'Numrat e shtypur nga intervali [1,49] jane: ( ' + loja() + ' )'
            connectionSocket.send(response.encode('UTF-8'))
        elif rcvCMD == 'ZARI':
            response = 'Zari i hedhur ka vleren: ' + str(random.randint(1, 6))
            connectionSocket.send(response.encode('UTF-8'))
        elif rcvCMD == 'FIBONACCI':
            nr = connectionSocket.recv(128).decode('UTF-8')
            print('FIBONACCI')
            print('Numri i dhene eshte: ' + nr)
            num=int(nr)
            connectionSocket.send(str(fibonacci(num)).encode('UTF-8'))
        elif rcvCMD == 'FACTORIAL':
            nr = connectionSocket.recv(128).decode('UTF-8')
            print('FACTORIAL')
            print('Numri i dhene eshte: ' + nr)
            nr=int(nr)
            connectionSocket.send(str(factorial(nr)).encode('UTF-8'))
        elif rcvCMD == 'MADHESIA':
            mesazhi = connectionSocket.recv(128).decode('UTF-8')
            mesazhi = 'Shkronja me e madhe e fjalise eshte: ' + madhesia(mesazhi)
            connectionSocket.send(mesazhi.encode('UTF-8'))
        elif rcvCMD == 'KONVERTIMI':
            opsioni = connectionSocket.recv(128).decode('UTF-8')
            print('Zgjedhja e bere eshte: ' +opsioni)
            num = connectionSocket.recv(128).decode('UTF-8')
            numri=int(num)
            connectionSocket.send(str(konvertimi(opsioni,numri)).encode('UTF-8'))
        elif rcvCMD == '0':
            break
        else:
            connectionSocket.send('Funksioni nuk ekziston'.encode('UTF-8'))
    print('Klienti ' + str(addr) + ' mbylli lidhjen.')
    connectionSocket.close()

while True:
    connectionSocket,addr=serverSocket.accept() 
    print('Klienti me ip ' + str(addr[0]) + ' dhe port ' + str(addr[1]) + ' krijoi nje lidhje')
    start_new_thread(client_handler, (connectionSocket, addr))



connectionSocket.close()


