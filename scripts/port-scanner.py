import socket

target = input("Podaj IP lub domenę: ")
print(f"\nSkanowanie: {target}\n")

ports = [21, 22, 23, 25, 53, 80, 443, 3306, 3389, 8080]

for port in ports:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[OTWARTY]  Port {port}")
        s.close()
    except:
        print(f"[zamknięty] Port {port}")

print("\nGotowe.")