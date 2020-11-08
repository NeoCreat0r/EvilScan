# -*- coding: utf-8 -*-
import socket
from datetime import datetime
from colorama import Fore, init

init()

print(f'''{Fore.LIGHTRED_EX}
 |\                           /|
 |1\                         /0|
 |01\                       /10|
 |000\                     /010|
 |0101\                   /1101|
 |01000\                 /01011|
 |1EVIL1\               /1SCAN0|
 |0001010\	       /1010111|
 |10110101\  _______  /00101101|
  01001010              010010
   0111011               0110
    00010                 011
     101                   0
      1
''')
print(f"{Fore.LIGHTCYAN_EX} [#=>] Coded by NeoCreat0r")

start = datetime.now()
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993,
         995, 1080, 1194, 1433, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 8080, 10000, 20000]

print(f"{Fore.LIGHTYELLOW_EX}")
ip = input("Site Name / IP Address: ")
print(f"{Fore.LIGHTGREEN_EX}IP address:", socket.gethostbyname(ip))
print(f"{Fore.LIGHTRED_EX}<===============>")
print(f"{Fore.WHITE}Loading Ports...")
print(f"{Fore.LIGHTGREEN_EX}##################")
for port in ports:
    y = socket.socket()
    y.settimeout(1)
    try:
        y.connect((ip, port))
    except socket.error:
        pass
    else:
        y.close()

        if port == 20:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/FTP-DATA")
        elif port == 21:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/FTP")
        elif port == 22:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SSH")
        elif port == 23:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/Telnet")
        elif port == 25:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SMTP")
        elif port == 43:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/WHOIS")
        elif port == 53:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/DNS")
        elif port == 80:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/http")
        elif port == 115:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SFTP")
        elif port == 123:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/NTP")
        elif port == 143:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/IMAP")
        elif port == 161:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SNMP")
        elif port == 179:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/BGP")
        elif port == 443:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/HTTPS")
        elif port == 445:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/MICROSOFT-DS")
        elif port == 514:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SYSLOG")
        elif port == 515:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/PRINTER")
        elif port == 993:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/IMAPS")
        elif port == 995:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/POP3S")
        elif port == 1080:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SOCKS")
        elif port == 1194:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/OpenVPN")
        elif port == 1433:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SQL Server")
        elif port == 1723:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/PPTP")
        elif port == 3128:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/HTTP")
        elif port == 3268:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/LDAP")
        elif port == 3306:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/MySQL")
        elif port == 3389:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/RDP")
        elif port == 5432:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/PostgreSQL")
        elif port == 5060:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/SIP")
        elif port == 5900:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/VNC")
        elif port == 8080:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/Tomcat")
        elif port == 10000:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/Webmin")
        else:
            print(ip + ":" + str(port) + f" {Fore.LIGHTGREEN_EX}is open/unknown")

print(f"{Fore.LIGHTGREEN_EX}##################")
ends = datetime.now()
print(f"{Fore.LIGHTRED_EX}" + "<Time:{}>".format(ends - start))

print(f"{Fore.MAGENTA}Scan completed!")
input("Press Enter to the exit....")
