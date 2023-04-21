from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
api_key = open("APIKey.txt", "r").read().strip("\n")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather_url = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        )
        print(weather_url)
        weather_data = weather_url.json()
        print(weather_data)
        temp = round(weather_data["main"]["temp"])
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        return render_template(
            "result.html",
            temp=temp,
            humidity=humidity,
            wind_speed=wind_speed,
            city=city,
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
