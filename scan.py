# -*- coding: utf-8 -*-
import socket

print("Scan your occupied port")
print("-----------------------")
print("[1] - tcp")
print("[2] - udp")
print("-----------------------")
tcpnpt = input("Select the scan mode [1/2] : ")

if tcpnpt == "1":
    prtc_name = 'tcp'
    i = 0
    while i < 65535:
        try:
            print(str(i) + ":" + socket.getservbyport(i,prtc_name))
        except OSError:
            pass
        i = i + 1
elif tcpnpt == "2":
    prtc_name = 'udp'
    i = 0
    while i < 65535:
        try:
            print(str(i) + ":" + socket.getservbyport(i,prtc_name))
        except OSError:
            pass
        i = i + 1
else:
    print("Choose a number between 1 and 2")
