from socket import *
from _thread import *

import datetime
import random
import math

serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Serveri u startua ne localhost: '+str(serverPort))
print('-----------------------------------')

print('Serveri eshte i gatshem te pranoje kerkesa ')
print('------------------------------------------')




#Definimi i metodave
#Metoda Bashketingllore
def bashketingellore(fjalia):
    bashketingellore = ['B', 'C','C' 'D','DH','F','G','GJ','H', 'J','K','L','LL','M','N',
                        'NJ','P','Q', 'R','RR','S','SH','T','TH','V','X','XH','Z','ZH',
                        'b','c','c','d','dh','f','g','gj','h','j','k','l','ll','m','n',
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




def client_handler(data, addr):
    fjalia = data
        
    # Ruan ne nje variabel kerkesen me shkronja te medha
    FjaliaMeShkronjaTeMedha=fjalia.upper()
    
    rcvCMD = FjaliaMeShkronjaTeMedha.decode('UTF-8')
      
    if 'PRINTIMI' in rcvCMD:
        fjalia = fjalia.decode('UTF-8')
        n_arr = fjalia.split(' ')
        mesazhi = ''
        for i in range(1, len(n_arr)):
            mesazhi += n_arr[i] + ' '
        mesazhi = 'Fjalia e dhene eshte: ' + mesazhi
        serverSocket.sendto(mesazhi.encode('UTF-8'), addr)
    elif rcvCMD == 'EMRIIKOMPJUTERIT':
        serverSocket.sendto(Host().encode('UTF-8'), addr)
    elif rcvCMD == 'IPADRESA':
        serverSocket.sendto(str(addr[0]).encode('UTF-8'), addr)
    elif rcvCMD == 'NUMRIIPORTIT':
        serverSocket.sendto(str(addr[1]).encode('UTF-8'), addr)
    elif 'BASHKETINGLLORE' in rcvCMD:
        fjalia = fjalia.decode('UTF-8')
        n_arr = fjalia.split(' ')
        mesazhi = ''
        for i in range(1, len(n_arr)):
            mesazhi += n_arr[i] + ' '
        pergjigja = 'Numri i bashketinglloreve eshte: ' + str(bashketingellore(mesazhi))
        serverSocket.sendto(pergjigja.encode('UTF-8'), addr)
    elif rcvCMD == 'TIME':
        koha = 'Koha eshte: ' + str(timenow())
        serverSocket.sendto(koha.encode('UTF-8'), addr)
    elif rcvCMD == 'LOJA':
        serverSocket.sendto(loja().encode('UTF-8'), addr)
    elif rcvCMD == 'ZARI':
        serverSocket.sendto(str(random.randint(1, 6)).encode('UTF-8'), addr)
    elif 'FIBONACCI' in rcvCMD:
        nr = rcvCMD.split(' ')[1]
        num=int(nr)
        serverSocket.sendto(str('Zgjidhja eshte: ' + str(fibonacci(num))).encode('UTF-8'), addr)
    elif 'MADHESIA' in rcvCMD:
        fjalia = fjalia.decode('UTF-8')
        n_arr = fjalia.split(' ')
        mesazhi = ''
        for i in range(1, len(n_arr)):
            mesazhi += n_arr[i] + ' '
        mesazhi = 'Shkronja me e madhe e fjalise eshte: ' + madhesia(mesazhi)
        serverSocket.sendto(mesazhi.encode('UTF-8'), addr)
    elif 'FACTORIAL' in rcvCMD:
        nr = rcvCMD.split(' ')[1]
        nr=int(nr)
        serverSocket.sendto(str('Zgjidhja eshte: ' + str(factorial(nr))).encode('UTF-8'), addr)
    elif 'KONVERTIMI' in rcvCMD:
        command = fjalia.decode('UTF-8')
        opsioni = command.split(' ')[1]
        print('Zgjedhja e bere eshte: ' + opsioni)
        num = command.split(' ')[2]
        numri=int(num)
        serverSocket.sendto(str(konvertimi(opsioni,numri)).encode('UTF-8'), addr)
    elif rcvCMD == '0':
        pass
    else:
        serverSocket.sendto('Funksioni nuk ekziston'.encode('UTF-8'), addr)

while True:
    data,addr = serverSocket.recvfrom(128)
    print('Adresa ' + str(addr) + ' dergoi nje informacion')
    start_new_thread(client_handler, (data, addr))


