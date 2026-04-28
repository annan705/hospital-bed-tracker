from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data/hospitals.json"

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def predict_beds(current):
    if current < 5:
        return "High Risk"
    elif current < 10:
        return "Moderate"
    else:
        return "Stable"

@app.route("/")
def index():
    hospitals = load_data()
    for h in hospitals:
        h["prediction"] = predict_beds(h["beds"])
        h["pct"] = min(100, round((h["beds"] / h.get("capacity", 20)) * 100))
    total_beds = sum(h["beds"] for h in hospitals)
    high_risk = sum(1 for h in hospitals if h["beds"] < 5)
    emergencies = sum(1 for h in hospitals if h.get("emergency", False))
    return render_template("index.html",
        hospitals=hospitals,
        total_beds=total_beds,
        high_risk=high_risk,
        emergencies=emergencies
    )

@app.route("/update", methods=["POST"])
def update():
    name = request.form["name"]
    beds = int(request.form["beds"])
    hospitals = load_data()
    for hospital in hospitals:
        if hospital["name"] == name:
            hospital["beds"] = beds
    save_data(hospitals)
    return redirect("/")

@app.route("/toggle_emergency", methods=["POST"])
def toggle_emergency():
    name = request.form["name"]
    hospitals = load_data()
    for hospital in hospitals:
        if hospital["name"] == name:
            hospital["emergency"] = not hospital.get("emergency", False)
    save_data(hospitals)
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
