import ftplib, os, shutil
from os import mkdir

def buscar_descargar():
    ##buscamos .txt, .msg o README
    narc = ftp.nlst()
    for arc in narc:
        if (arc.endswith('.txt') or arc.endswith('.msg') or arc == "README"):
            print (arc)
            with open(arc, 'wb') as ar:
                ftp.retrbinary(f'RETR '+arc, ar.write)

def crear_mover():
    ##Crear carpeta
    mkdir("Archivos de texto")
    dire = os.getcwd() + "\Archivos de texto"
    arct = os.listdir(".")
    for tx in arct:
        if (tx.endswith('.txt') or tx.endswith('.msg') or tx == "README"):
            shutil.move(tx, dire)
            
        

##conexión
ftp = ftplib.FTP('ftp.us.debian.org', 'anonymous', 'probando@123.com')

buscar_descargar()

##bye conexion
ftp.quit()

crear_mover()
