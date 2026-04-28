# Hospital Bed Tracker 🏥

A real-time hospital bed availability tracker built with Python and Flask. Features AI-powered bed status predictions, emergency flagging, and color-coded availability indicators.

## Features

- View bed availability across all hospitals
- Color-coded status: Green (Stable), Amber (Moderate), Red (High Risk)
- AI prediction labels based on current bed count
- Emergency alert flag per hospital
- Update bed counts in real time
- Mobile responsive

## Run Locally

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/hospital-bed-tracker.git
cd hospital-bed-tracker

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Deploy to Render (Free)

1. Push this repo to GitHub
2. Go to https://render.com and sign in
3. Click **New → Web Service**
4. Connect your GitHub repo
5. Render auto-detects `render.yaml` — just click **Deploy**
6. Your app goes live at `https://hospital-bed-tracker.onrender.com`

## Deploy to Railway

1. Go to https://railway.app
2. Click **New Project → Deploy from GitHub**
3. Select this repo — Railway auto-detects the Procfile
4. Done ✅

## Project Structure

```
hospital-bed-tracker/
├── app.py               # Flask backend + AI prediction logic
├── requirements.txt     # Python dependencies
├── Procfile             # For Render/Railway deployment
├── render.yaml          # One-click Render config
├── data/
│   └── hospitals.json   # Hospital data store
├── templates/
│   └── index.html       # Frontend HTML (Jinja2)
└── static/
    └── style.css        # Styling
```

## AI Prediction Logic

```python
def predict_beds(current):
    if current < 5:  return "High Risk"
    elif current < 10: return "Moderate"
    else: return "Stable"
```

## License

MIT
