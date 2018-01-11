import pyowm
from config import pyowm_key, pyowm_city

def get_weather_info():
	owm = pyowm.OWM(pyowm_key, language="en")
	observation = owm.weather_at_place(pyowm_city)
	w = observation.get_weather()
	# температура
	temperature = round(w.get_temperature('celsius')['temp']) 
	# статус облачков
	status = w.get_detailed_status()
	# возвращает кортеж
	weather = (temperature, status)
	return weather