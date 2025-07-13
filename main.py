from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/wetter")
def wetter_api():
    lat = request.args.get("lat", type=float)
    lon = request.args.get("lon", type=float)

    if lat is None or lon is None:
        return jsonify({"error": "Koordinaten fehlen"}), 400

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&past_days=7&forecast_days=3"
        f"&timezone=Europe%2FBerlin"
    )

    response = requests.get(url)
    data = response.json()

    tage = data["daily"]["time"]
    max_temp = data["daily"]["temperature_2m_max"]
    min_temp = data["daily"]["temperature_2m_min"]

    wetterdaten = [
        {
            "datum": d,
            "temp_max": tmax,
            "temp_min": tmin,
            "temp_avg": round((tmax + tmin) / 2, 1)
        }
        for d, tmax, tmin in zip(tage, max_temp, min_temp)
    ]

    return jsonify(wetterdaten)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

