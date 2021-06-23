import requests,datetime

apiKey = "f795bb0d9ba321e4fb133678eac3f78d"
apiBaseUrl = "http://api.openweathermap.org/data/2.5/weather"

time = datetime.datetime.now().strftime("%I:%M")
year = int(datetime.datetime.now().year)
month = int(datetime.datetime.now().month)
day = int(datetime.datetime.now().day)

print("---Weather App Project---")
cityName = input("Enter City Name : ")
apiUrl = apiBaseUrl + "?q=" + cityName + "&appid=" + apiKey + "&units=metric"

response = requests.get(apiUrl)
x = response.json()

if x["cod"] == "400" or x["cod"] == "401" or x["cod"] == "404":
    error = x["message"]
    print(error)

else:
    city = x["name"]
    weather = x["weather"][0]["main"]

    tempC = x["main"]["temp"]
    pressure = x["main"]["pressure"]
    humidity = x["main"]["humidity"]
    visibility = x["visibility"]
    wind = x["wind"]["speed"]
    degree_sign = u'\N{DEGREE SIGN}'
    with open('Weather.txt','w') as f:
        
        f.write(f"    CURRENT     WEATHER     IN     {city.upper()}     ||     {day}/{month}/{year}     ||     {time}       \n")
        f.write("\n")
        f.write("Weather:" + str(weather) + "       | Temp:" + str(tempC) + str(degree_sign) + "C \nPressure:" + str(pressure) + " hPa   | Humidity:" + str(humidity) + " %\n")
        f.write(f"Wind Speed:{wind} m/s") 