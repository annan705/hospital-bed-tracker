from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# In-memory data store — works perfectly on Render (no file writes needed)
hospitals = [
    {"name": "City Hospital",          "beds": 12, "capacity": 20, "emergency": False},
    {"name": "LifeCare Hospital",       "beds": 5,  "capacity": 20, "emergency": False},
    {"name": "Green Valley Clinic",     "beds": 8,  "capacity": 20, "emergency": False},
    {"name": "Sunrise Medical Centre",  "beds": 2,  "capacity": 15, "emergency": True},
    {"name": "Apollo General Hospital", "beds": 15, "capacity": 25, "emergency": False},
]

def predict_beds(current):
    if current < 5:
        return "High Risk"
    elif current < 10:
        return "Moderate"
    else:
        return "Stable"

@app.route("/")
def index():
    for h in hospitals:
        h["prediction"] = predict_beds(h["beds"])
        h["pct"] = min(100, round((h["beds"] / h.get("capacity", 20)) * 100))
    total_beds  = sum(h["beds"] for h in hospitals)
    high_risk   = sum(1 for h in hospitals if h["beds"] < 5)
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
    for h in hospitals:
        if h["name"] == name:
            h["beds"] = max(0, min(beds, h["capacity"]))
    return redirect("/")

@app.route("/toggle_emergency", methods=["POST"])
def toggle_emergency():
    name = request.form["name"]
    for h in hospitals:
        if h["name"] == name:
            h["emergency"] = not h.get("emergency", False)
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
