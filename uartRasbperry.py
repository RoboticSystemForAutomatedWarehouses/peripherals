import serial
import time
serialport = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)

while True:
    s = input("task ;")
    rcv = ""
    for i in range(len(s)):
        serialport.write(s[i].encode())
        print(serialport.read(1).decode())
    
    rcv = serialport.readline(len(s))
    while len(rcv) == 0:
        rcv = serialport.readline(len(s))

    print(rcv.decode())
    
