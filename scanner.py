import socket

def main():
    ip_dominio = input("Introduce la IP o dominio que desea escanear: ")


    # Escaneamos la ip/dominio de forma qué prefiera el usuario.

    escaneoTerminado = False
    
    puertosComunes = [20,21,22,23,25,53,80,110,111,135,139,143,161,162,389,443,
        445,465,587,993,995,1025,1433,1434,1723,1900,3306,3389,5432,5900,8080]
    
    serviciosComunes = [
        "FTP data",        # 20
        "FTP",             # 21
        "SSH",             # 22
        "Telnet",          # 23
        "SMTP",            # 25
        "DNS",             # 53
        "HTTP",            # 80
        "POP3",            # 110
        "Portmap/RPC",     # 111
        "MS RPC",          # 135
        "NetBIOS-SSN",     # 139
        "IMAP",            # 143
        "SNMP",            # 161
        "SNMP Trap",       # 162
        "LDAP",            # 389
        "HTTPS",           # 443
        "SMB",             # 445
        "SMTPS",           # 465
        "SMTP submission", # 587
        "IMAP sobre SSL",  # 993
        "POP3 sobre SSL",  # 995
        "Puerto 1025",     # 1025 (genérico)
        "MS SQL Server",   # 1433
        "MS SQL Monitor",  # 1434
        "PPTP VPN",        # 1723
        "SSDP/UPnP",       # 1900
        "MySQL",           # 3306
        "RDP",             # 3389
        "PostgreSQL",      # 5432
        "VNC",             # 5900
        "HTTP alternativo" # 8080
    ]



    while escaneoTerminado == False:
        tipoDeEscaneo = input("\nSi desea un escaneo rápido (sólo los 30 puertos TCP más comunes) escriba 'Rapido'. Si desea uno de los puertos bien conocidos(rango del 1 al 1023) escriba 'Conocidos': ")
        tipoDeEscaneo = tipoDeEscaneo.lower()

        if tipoDeEscaneo == "rapido":
            for i in puertosComunes:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)

                errorSocket = sock.connect_ex((ip_dominio, i))
                sock.close()

                if errorSocket == 0:  
                    print(f"El puerto {i} ({serviciosComunes[puertosComunes.index(i)]}) está ABIERTO.")

            
            print("\nEscaneo completado con éxito.")
            escaneoTerminado = True 
                    

        elif tipoDeEscaneo == "conocidos":
            print("El escaneo puede tardar varios minutos según la red.")
            
            for i in range(1, 1024):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.3)

                ComprueboPuertoAbierto = sock.connect_ex((ip_dominio, i))
                sock.close()

                if ComprueboPuertoAbierto == 0:  
                    print(f"El puerto {i} está ABIERTO.")

            
            print("\nEscaneo completado con éxito.")
            escaneoTerminado = True

        else:
            print("\n   ERROR: Responda sólo con 'Rapido' o 'Conocidos' porfavor.")

if __name__ == "__main__":
    main()
