from flask import Flask,render_template, redirect, request, json
import requests
app = Flask(__name__)


@app.route("/", methods = ["GET","POST"])
def city():
    city = ""
    getweather = None
    if request.method == "POST":
        city = request.form.get("city")
        getweather = get_weather(city)
    return render_template("index.html", city=city, getweather=getweather)

def get_weather(city):
    api_key = "c0c19dbe699083551d3f95a20c318354"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city_name = city
    complete_url = base_url + "?appid=" + api_key + "&q=" + city_name + "&units=metric"

    response = requests.get(complete_url)
    x = response.json()
    print(x)
    print(x["cod"], type(x["cod"]))

    if x["cod"] == 200:
      y = x["main"]
      current_temperature = y["temp"]

      # store the value corresponding
      # to the "pressure" key of y
      current_pressure = y["pressure"]

      # store the value corresponding
      # to the "humidity" key of y
      current_humidity = y["humidity"]
      feel_like = y["feels_like"]
      wind_speed = x["wind"]["speed"]

      # store the value of "weather"
      # key in variable z
      z = x["weather"]

      # store the value corresponding 
      # to the "description" key at 
      # the 0th index of z
      weather_description = z[0]["description"]
      country = x["sys"]["country"]
      weather_icon = "https://openweathermap.org/img/wn/" + z[0]["icon"] + "@2x.png"
    
      weather = {"humidity" : current_humidity, "pressure": current_pressure, "temperature": current_temperature, "description": weather_description, "feels_like": feel_like, "windspeed": wind_speed, "country": country, "icon": weather_icon}
      return weather
    else:
        return {"error":"Enter a valid city name"}
    
    return None
    #   # print following values
    #   print(" Temperature (in kelvin unit) = " +
    #                 str(current_temperature) + 
    #       "\n atmospheric pressure (in hPa unit) = " +
    #                 str(current_pressure) +
    #       "\n humidity (in percentage) = " +
    #                 str(current_humidity) +
    #       "\n description = " +
    #                 str(weather_description))

    # else:
    #     print(" City Not Found ")

app.run(debug = True)