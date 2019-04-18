import socket
serverName="localhost"
serverPort=12000
# Krijohet nje socket te cilin e perdorim per lidhje me server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
# Bejme kerkesen per lidhje ne serverin me emrin serverName dhe portin serverPort
s.connect((serverName,serverPort)) 
print('FIEK Klienti: ')

while True:
    
    s.sendall(str.encode('komandat'))
    komandat = s.recv(1024).decode('UTF-8')
    print(komandat)

    var=input('->Shkruani kerkesen ose numrin 0 per dalje: ')
    mesazhi = var.upper()
    s.sendall(str.encode(mesazhi))
    if mesazhi == 'PRINTIMI' or mesazhi == 'BASHKETINGLLORE' or mesazhi == 'MADHESIA':
        # Jepet nje fjali tjeter
        fjalia = input('Shkruani nje fjali: ')
        s.sendall(str.encode(fjalia))
        data=s.recv(128).decode('UTF-8')
        print(data)
    elif mesazhi == 'FIBONACCI':
        nr = input('Shkruani nje numer: ')
        s.sendall(str.encode(nr))
        data=s.recv(128).decode('UTF-8')
        print('Fibonacci : '+data)
    elif mesazhi=='FACTORIAL':
        nr=input('Shkruani nje numer pozitiv:')
        s.sendall(str.encode(nr))
        data=s.recv(128).decode('UTF-8')
        print('Factorial : '+data)
    elif mesazhi == 'KONVERTIMI':
        print('\t->KilowattToHorsepower')
        print('\t->HorsepowerToKilowatt')
        print('\t->DegreesToRadians')
        print('\t->RadiansToDegrees')
        print('\t->GallonsToLiters')
        print('\t->LitersToGallons')
        opsioni = input('Zgjedh konvertimin ne njeren nga format me siper: ')
        s.sendall(str.encode(opsioni))
        numri = input('Shkruaj numrin qe doni ta konvertoni: ')
        s.sendall(str.encode(numri))
        data=s.recv(128).decode('UTF-8')
        print('Numri i konvertuar eshte: '+data)
    elif mesazhi == '0':
        break
    else: 
        data=s.recv(128).decode('UTF-8')
        print(data)

    print()
s.close()



