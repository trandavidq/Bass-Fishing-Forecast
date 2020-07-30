from flask import Flask , redirect, render_template, request, url_for
import getWeather



app = Flask(__name__)

@app.route('/',methods = ["POST","GET"] )
def home():
    global temp, windSpeed, condition, baroPressure, fishRating
    if(request.method == "POST"):
        zip = request.form["zipCode"]
        
        weatherData = getWeather.getWeather(zip)
        temp = weatherData[0]
        windSpeed = weatherData[1]
        condition = weatherData[2]
        baroPressure = weatherData[3]
        fishRating = getWeather.fish_forecast(zip)
        

        return redirect(url_for("results"))
    else:
        return render_template("index.html")

@app.route('/results', methods = ["POST","GET"])
def results():
    return render_template("results.html", tem= temp, wind = windSpeed, cond = condition, baro = baroPressure, rating = fishRating)



if __name__ == '__main__':
    
    app.run()
