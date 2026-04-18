from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = []
    hourly_data = []
    if request.method == "POST":
        city = request.form.get("city")
        lat = request.form.get("lat")
        lon = request.form.get("lon")

        if lat and lon:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        elif city:
            weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        else:
            return render_template("index.html")

        try:
            response = requests.get(weather_url)
            if response.status_code == 200:
                data = response.json()
                # Calculate local time based on the timezone offset provided by the API
                local_time = datetime.utcfromtimestamp(data["dt"] + data["timezone"])
                weather_data = {
                    "city": data["name"],
                    "country": data["sys"]["country"],
                    "date": local_time.strftime("%A, %B %d, %Y"),
                    "temperature": round(data["main"]["temp"]),
                    "feels_like": round(data["main"]["feels_like"]),
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "condition": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"],
                    "sunrise": datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime("%I:%M %p").lstrip("0"),
                    "sunset": datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime("%I:%M %p").lstrip("0"),
                    "lat": data["coord"]["lat"],
                    "lon": data["coord"]["lon"]
                }
                
                # Fetch 5-day forecast
                f_response = requests.get(forecast_url)
                if f_response.status_code == 200:
                    f_data = f_response.json()
                    
                    # 24-hour (3-hourly) forecast parsing
                    for item in f_data['list'][:8]:
                        # Using utcfromtimestamp for robust mapping matching timezone
                        dt_obj = datetime.utcfromtimestamp(item["dt"] + data["timezone"])
                        hourly_data.append({
                            "time": dt_obj.strftime("%I %p").lstrip("0"),
                            "temperature": round(item["main"]["temp"]),
                            "icon": item["weather"][0]["icon"]
                        })
                        
                    # 5-day daily forecast parsing (approx 12:00)
                    for item in f_data['list']:
                        if "12:00:00" in item['dt_txt']:
                            date_obj = datetime.strptime(item["dt_txt"].split(" ")[0], "%Y-%m-%d")
                            forecast_data.append({
                                "day": date_obj.strftime("%a %b %d"),
                                "temperature": round(item["main"]["temp"]),
                                "icon": item["weather"][0]["icon"]
                            })
            elif response.status_code == 401:
                weather_data = {"error": "API Key is missing or invalid in this environment! Please configure the API_KEY environment variable."}
            else:
                weather_data = {"error": "Location not found!"}
        except requests.exceptions.RequestException:
            weather_data = {"error": "Unable to connect to weather service!"}
            
    return render_template("index.html", weather=weather_data, forecast=forecast_data, hourly=hourly_data, api_key=API_KEY)

if __name__ == "__main__":
    app.run(debug=True)

