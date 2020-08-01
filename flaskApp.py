from flask import Flask , redirect, render_template, request, url_for
import getWeather



app = Flask(__name__)

mapKey = "AIzaSyDkcJL7GE4QA7Mo0tutF9X3-ze2Ap2TIpI"
    
@app.route('/',methods = ["POST","GET"] )
def home():
    global temp, windSpeed, condition, baroPressure, fishRating, cityName, zip, mapURL
    if(request.method == "POST"):
        try:
            zip = request.form["zipCode"]
            
            weatherData = getWeather.getWeather(zip)
            temp = weatherData[0]
            windSpeed = weatherData[1]
            condition = weatherData[2]
            baroPressure = weatherData[3]
            cityName = weatherData[4]
            fishRating = getWeather.fish_forecast(zip)
            mapURL = "https://www.google.com/maps/embed/v1/place?key=AIzaSyDkcJL7GE4QA7Mo0tutF9X3-ze2Ap2TIpI&q="+str(zip)
            return redirect(url_for("results"))
        except:
            return render_template("404.html")
                  
    else:
        return render_template("index.html")

@app.route('/results', methods = ["POST","GET"])
def results():
    global temp, windSpeed, condition, baroPressure, fishRating, cityName, zip, mapURL
    if(request.method == "POST"):
        try:
            zip = request.form["zipCode"]
            
            weatherData = getWeather.getWeather(zip)
            temp = weatherData[0]
            windSpeed = weatherData[1]
            condition = weatherData[2]
            baroPressure = weatherData[3]
            cityName = weatherData[4]
            fishRating = getWeather.fish_forecast(zip)
            mapURL = "https://www.google.com/maps/embed/v1/place?key=AIzaSyDkcJL7GE4QA7Mo0tutF9X3-ze2Ap2TIpI&q="+str(zip)
            return redirect(url_for("results"))
        except:
            return render_template("404.html")
    else:
        return render_template("results.html", tem= temp, wind = windSpeed, cond = condition, baro = baroPressure, rating = fishRating, city= cityName, mapzip=mapURL)
    
    


@app.route('/404', methods = ["POST","GET"])
def error():
    global temp, windSpeed, condition, baroPressure, fishRating, cityName, zip, mapURL
    if(request.method == "POST"):
        try:
            zip = request.form["zipCode"]
            
            weatherData = getWeather.getWeather(zip)
            temp = weatherData[0]
            windSpeed = weatherData[1]
            condition = weatherData[2]
            baroPressure = weatherData[3]
            cityName = weatherData[4]
            fishRating = getWeather.fish_forecast(zip)
            mapURL = "https://www.google.com/maps/embed/v1/place?key=AIzaSyDkcJL7GE4QA7Mo0tutF9X3-ze2Ap2TIpI&q="+str(zip)
            return redirect(url_for("results"))
        except:
            return render_template("404.html")
    else:
        return render_template("404.html")

if __name__ == '__main__':
    
    app.run()
