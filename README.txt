
# Network TCP Port Scanner

    Pequeño escáner de puertos TCP escrito en Python que permite analizar una IP o dominio con dos modos de escaneo: rápido (puertos más comunes) 
    y puertos bien conocidos (1–1023).

    ## Características

        - Escaneo de **puertos TCP más comunes** (modo rápido).
        - Escaneo de **puertos bien conocidos** (rango 1–1023).
        - Detección de puertos abiertos mediante conexiones TCP.
        - Identificación del servicio típico asociado a los 30 puertos más usados (HTTP, SSH, RDP, etc.) en el modo rápido.
        - Interfaz sencilla por consola.

    ## Requisitos

        - Python 3.x
        - Librería estándar de Python (`socket`)

        No requiere dependencias externas.

    ## Instalación

        1. Clona este repositorio o descarga el archivo:
            
            git clone https://github.com/tu-usuario/network-tcp-port-scanner.git
            cd network-tcp-port-scanner


        2. Asegúrate de tener Python 3 instalado:

            python --version

        o
            python3 --version


    ## Uso

        Ejecuta el script desde la terminal:

            python scanner.py

        o en algunos sistemas

            python3 scanner.py


        El programa te pedirá:

        1. **IP o dominio** a escanear  
        - Ejemplos válidos:
            - `192.168.1.10`
            - `scanme.nmap.org`
            - `www.google.com`
        - No incluyas `http://` ni `/` al final.

        2. **Tipo de escaneo**:

        - `Rapido`  
            Escanea solo unos 30 puertos TCP muy comunes (22, 80, 443, 3389, etc.) y muestra también el nombre del servicio típico.

        - `Conocidos`  
            Escanea los puertos TCP bien conocidos del **1 al 1023**. Este modo puede tardar más tiempo, según el timeout configurado y la red.


    ### Ejemplo de salida (modo rápido)

        Introduce la IP o dominio que desea escanear: scanme.nmap.org

        Si desea un escaneo rápido (sólo los 30 puertos TCP más comunes) escriba 'Rapido'. Si desea uno de los puertos bien conocidos (rango del 1 al 1023) escriba 'Conocidos': Rapido
        El puerto 22 (SSH) está ABIERTO.
        El puerto 80 (HTTP) está ABIERTO.

        Escaneo completado con éxito.


    ## Estructura del código

        - Uso de `socket.socket(AF_INET, SOCK_STREAM)` para crear sockets TCP.
        - `settimeout()` para limitar el tiempo de espera por puerto y evitar bloqueos largos.
        - `connect_ex()` para comprobar si el puerto acepta conexiones (puerto abierto) o no.
        - Función principal `main()` y bloque `if __name__ == "__main__":` para una estructura más limpia y reutilizable.

    ## Limitaciones y posibles mejoras

        - Solo escanea **puertos TCP** (no UDP).
        - Escaneo secuencial, sin paralelismo.
        - No detecta servicios ni versiones, solo puertos abiertos.

        Posibles mejoras futuras:

        - Añadir soporte para escaneo UDP básico.
        - Permitir que el usuario especifique un rango personalizado.
        - Guardar los resultados en un archivo (por ejemplo, CSV o TXT).
        - Añadir colores en la consola para resaltar puertos abiertos.

    ## Uso ético

        Este proyecto tiene fines educativos y de práctica en programación y redes.  
        Utilízalo **solo** contra sistemas propios o para los que tengas autorización expresa. El uso no autorizado de herramientas de escaneo puede
        ser ilegal según la legislación de tu país.
