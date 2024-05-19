import socket



#Colors 
R = '\033[1;31m'
G = '\033[1;32m' 
B = '\x1b[1;34m'
M = '\x1b[38;5;8m'
J = '\x1b[1;33m'

print(f'{J}-----------------------PORT SCANNER----------------------------')
print()                                                                           


url = input('Enter The Target URL: ')
ports = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
ok = []

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
        sock.settimeout(1)
        sock.connect((url, port))
        ok.append(port)
        print(f"{B}+---------------------------")
        print(f"{B}�{G}THE PORT {port} IS OPEN ")
        print(f"{B}+---------------------------")
    except:
        print(f"{B}+-----------------------------")
        print(f"{B}�{R}THE PORT {port} IS CLOSED ")
        print(f"{B}+-----------------------------")

print(f"{J}-----------------------------")
print(f'{G}THE OPPENED PORTS WAS :')
for i in ok:
    print(f"{G}�PORT -> {i}")
print(f"{J}-----------------------------")
