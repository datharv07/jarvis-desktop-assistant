import psutil
from datetime import datetime, date

# Function to gather information about the PC and take a screenshot
def Informtion_of_PC():
    battery = psutil.sensors_battery()
    now = datetime.now().strftime("%H:%M:%S")

    str0 = "Hello Atharv, \n     Your PC has been Started, \n             Any task for me\n\n-------------------------------------\nToday Date: " + str(date.today()) + "    "
    str1 = "\nBattery Percentage: " + str(battery.percent) + "    \n"
    str2 = "Battery Plugged In: " + str(battery.power_plugged) + "    \n-------------------------------------" + "\n"
    str3 = "Current Time: " + now + "    "
    str4 = "\n"
    
    last_message = str0 + str4 + str3 + str1 + str2 
    return last_message

