import socket

x=socket.gethostname();
y=socket.gethostbyname(x)
print("Your Host is= "+x)
print("Your IP is= "+y)
