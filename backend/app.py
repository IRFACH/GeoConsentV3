from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__, static_folder="../frontend")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "share.html")

@app.route("/location", methods=["POST"])
def location():
    data = request.json

    lat = data.get("lat")
    lon = data.get("lon")
    acc = data.get("accuracy")
    speed = data.get("speed", 0)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    map_link = f"https://maps.google.com/?q={lat},{lon}"

    output = f"""
📍 LOCATION RECEIVED
Time     : {time}
Latitude : {lat}
Longitude: {lon}
Accuracy : {acc} meters
Speed    : {speed} m/s
Map      : {map_link}
-----------------------
"""

    print(output)

    with open("locations.log", "a") as f:
        f.write(output)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
