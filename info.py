import socket
import uuid 
x=socket.gethostname()
y=socket.gethostbyname(x)
print("Your Host is= "+x)
print("Your IP is= "+y)
print ("Your Mac Adress is= "+':'.join(['{:02x}'.format((uuid.getnode() >> dali) & 0xff) for dali in range(0,8*6,8)][::-1])) 
