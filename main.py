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
        f"latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=Europe%2FBerlin"
    )

    response = requests.get(url)
    data = response.json()

    tage = data["daily"]["time"]
    temperaturen = data["daily"]["temperature_2m_max"]

    wetterdaten = [
        {"datum": t, "temp": temp}
        for t, temp in zip(tage, temperaturen)
    ]

    return jsonify(wetterdaten)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
