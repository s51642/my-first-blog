
import pyowm
from colorama import init
from colorama import Fore, Back, Style
init()

own = pyowm.OWM('6458992186482a3f396eaface1346f04', language = 'ru')
print( Back.GREEN )


s = "dsfsdf"
i = 4
print("\n"*30)
place = input("Введите город:\n")
observation = own.weather_at_place(place)
w = observation.get_weather()
print( Back.CYAN )
print(w['status'])
wind = w.get_wind()
print("Ветер: ", wind['speed'])                  # {'speed': 4.6, 'deg': 330}
print("Влажность: ", w.get_humidity())
temperature = w.get_temperature('celsius')              # 87
print("Температура: ", temperature['temp'])  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
