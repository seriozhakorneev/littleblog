import pyowm

def get_weather_info():
	# город
	city = 'Tula, Russia'
	# key с сайта pyowm
	owm = pyowm.OWM("84295771eb6ed9a21ed8e939df427e93",language="en")
	observation = owm.weather_at_place(city)
	w = observation.get_weather()
	# температура
	temperature = round(w.get_temperature('celsius')['temp']) 
	# статус облачков
	status = w.get_detailed_status()
	# возвращает кортеж
	weather = (temperature, status)
	return weather