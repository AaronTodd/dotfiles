import psutil

battery = psutil.sensors_battery()
percent = int(battery.percent)

#print("Porcentaje de batería:", percent)
bateria = ""
def bateria_icono():
    global bateria
    if(percent >= 95):
        bateria = "󰁹"
    elif(percent >= 90):
        bateria = "󰂂"
    elif(percent <= 90 and percent >= 80 ):
        bateria = "󰂁"
    elif(percent <= 80 and percent >= 70 ):
        bateria = "󰂀"
    elif(percent <= 70 and percent >= 60 ):
        bateria = "󰁿"
    elif(percent <= 60 and percent >= 50 ):
        bateria = "󰁾"
    elif(percent <= 50 and percent >= 40 ):
        bateria = "󰁽"
    elif(percent <= 40 and percent >= 30 ):
        bateria = "󰁼"
    elif(percent <= 30 and percent >= 20 ):
        bateria = "󰁻"
    elif(percent <= 20 and percent >= 10 ):
        bateria = "󰁺"
    elif(percent <= 10 and percent >= 5 ):
        bateria = "󰁺"
    elif(percent <= 5 and percent >= 0 ):
        bateria = "󰂃"
