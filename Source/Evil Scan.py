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

try:
    start = datetime.now()
    ports = {20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
             115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP", 179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
             514: "SYSLOG", 515: "PRINTER", 993: "IMAPS", 995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
             1433: "SQL Server", 1723: "PPTP", 3128: "HTTP", 3268: "LDAP", 3306: "MySQL", 3389: "RDP",
             5432: "PostgreSQL", 5060: "SIP", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"}

    print(f"{Fore.LIGHTYELLOW_EX}")
    ip = input("Site Name / IP Address: ")
    print(f"{Fore.LIGHTGREEN_EX}IP address:", socket.gethostbyname(ip))
    print(f"{Fore.LIGHTRED_EX}<===============>")
    print(f"{Fore.WHITE}Loading Ports...")
    print(f"{Fore.LIGHTGREEN_EX}##################")
    for port in ports:
        cont = socket.socket()
        cont.settimeout(1)
        try:
            cont.connect((ip, port))
        except socket.error:
            pass
        else:
            print(f"{socket.gethostbyname(ip)}:{str(port)} {Fore.LIGHTGREEN_EX}is open/{ports[port]}")
            cont.close()

    print(f"{Fore.LIGHTGREEN_EX}##################")
    ends = datetime.now()
    print(f"{Fore.LIGHTRED_EX}" + "<Time:{}>".format(ends - start))

    print(f"{Fore.MAGENTA}Scan completed!")
    input("Press Enter to the exit....")
except socket.gaierror:
    print(f"{Fore.LIGHTRED_EX}[!] Invalid input")
    input()
