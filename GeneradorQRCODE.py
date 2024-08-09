import pyqrcode
import png
from pyqrcode import QRCode

#codigos QR ID
#variables
con = 1234

#Generamos los QR

while con <= 1235:
    #id = str('j') + str(con)
    roster = con
    id = '71' + str(con)

    #creamos los QR
    qr = pyqrcode.create(71 and id, error= 'L')
    #Guardamos
    qr.png('D' + str(roster) + '.png',scale=6)
    #Aumentamos con
    con = con +1
