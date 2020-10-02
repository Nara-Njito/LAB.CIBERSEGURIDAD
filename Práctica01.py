##Práctica 01. APIS.
import requests
import json
from datetime import datetime
import time
from datetime import date
import datetime


##lA LLAMADA API ES A UNA PÁGINA DEL CLIMA.

##Pedire la temperatura máxima y minima de los proximos tres dias.

page = requests.get("http://api.openweathermap.org/data/2.5/onecall?lat=25.7349&lon=-100.3751&exclude=hourly,minutely,current&units=metric&appid=4d3c5830f25dc35f1b4beaca1ded75d5")
climita = json.loads(page.content)

print("Monterrey, N.L")

fechahoy = date.today()
x = 1

##Hago mucho movimiento con las fechas porque esta en tiempo UNIX

while(x < 4):
    newhoy = (fechahoy + datetime.timedelta(days = x)).strftime("%Y %m %d")
    
    print(newhoy)

    nnhoy = newhoy + " 13:00:00"

    for ele in climita["daily"]:
        fechita = int(time.mktime(time.strptime(nnhoy, "%Y %m %d %H:%M:%S")))

        if ele["dt"] == fechita:
            temp = ele["temp"]

            print("Temperatura minima del día", str(temp["min"]) + "°C" )

            print("Temperatura maxima del día", str(temp["max"]) + "°C")
    x+=1
    
