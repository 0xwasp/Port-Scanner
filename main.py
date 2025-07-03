import sys 
import socket as s

argv=sys.argv

if len(argv)<2:
    print("Not enough parameters, define Address ")
    sys.exit()

target = s.gethostbyname(argv[1])

try:
    for i in range(60,1023):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, int(i)))
        if result == 0:
            print("PORT", i, "IS OPEN LOL")

        else:
            print("PORT", i, "IS CLOSED")

            sock.close()

except KeyboardInterrupt:
    print("Scan interrupted")
    sys.exit()

    




