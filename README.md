# SteelSense AI ⬡
### Industrial Steel Surface Defect Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?style=flat-square&logo=flask)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-ff6b2b?style=flat-square)
![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=flat-square&logo=supabase)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Deployed-yellow?style=flat-square&logo=huggingface)

> AI-powered steel surface defect detection using YOLOv8 computer vision + Gemini Vision API for real-time analysis and plain-English explanation of manufacturing defects.

🔗 **Live Demo:** [huggingface.co/spaces/AishwaryaNJ/steelsense-ai](https://huggingface.co/spaces/AishwaryaNJ/steelsense-ai)

---

## What It Does

Upload any steel surface image and SteelSense AI will:

- **Detect** surface defects using a YOLOv8 model trained on the NEU Steel dataset
- **Explain** each defect using Gemini Vision AI — probable cause, severity, recommended action
- **Save** inspection reports to your account with full history and analytics
- **Visualize** defect trends on a dashboard with charts and severity breakdown

---

## Defect Classes Detected

| Class | Description |
|-------|-------------|
| Crazing | Network of fine cracks on surface |
| Inclusion | Foreign material embedded in steel |
| Patches | Irregular surface discoloration |
| Pitted Surface | Small cavities or holes on surface |
| Rolled-in Scale | Oxide scale pressed into surface |
| Scratches | Linear surface damage |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Object Detection | YOLOv8 (Ultralytics) |
| AI Explanation | Gemini Vision API (Google) |
| Backend | Flask (Python) |
| Database & Auth | Supabase (PostgreSQL) |
| Frontend | HTML, CSS, Jinja2 |
| Containerization | Docker |
| Deployment | Hugging Face Spaces |
| Image Processing | OpenCV |

---

## Model Performance

| Metric | Value |
|--------|-------|
| mAP50 | 73.6% |
| Training Images | 1,800 |
| Defect Classes | 6 |
| Inference Time | < 2 seconds |
| Dataset | NEU Steel Surface Defect |

---

## Features

- 🔐 **Authentication** — Signup/login with Supabase Auth, persistent sessions
- ⚙️ **Real-time Detection** — YOLOv8 inference with bounding box visualization
- 🤖 **AI Explanation** — Per-defect analysis with cause, severity and recommended action
- 📊 **Dashboard** — Inspection stats, defect type breakdown, severity distribution charts
- 📋 **Report History** — Full inspection history with annotated images per user
- 🐳 **Dockerized** — Fully containerized for consistent deployment

---

## Project Structure
```
steelsense-ai/
├── flask_app.py          # Main Flask application & routes
├── detect.py             # YOLOv8 inference pipeline
├── explain.py            # Gemini Vision AI explanation
├── best.pt               # Trained YOLOv8 model weights
├── templates/
│   ├── base.html         # Shared layout
│   ├── landing.html      # Landing page
│   ├── login.html        # Auth page
│   ├── dashboard.html    # Analytics dashboard
│   ├── analyze.html      # Upload & detect
│   └── reports.html      # Inspection history
├── database/
│   └── db.py             # Supabase connection & queries
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (not committed)
```

---

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Aishwarya-J05/SteelSense-AI.git
cd SteelSense-AI
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```
GEMINI_API_KEY=your_gemini_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_publishable_key
FLASK_SECRET_KEY=your_secret_key
```

### 5. Run the app
```bash
python flask_app.py
```

Open **http://localhost:5000**

---

## Database Schema
```sql
CREATE TABLE reports (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id TEXT NOT NULL,
    image_name TEXT,
    annotated_image TEXT,
    defects JSONB,
    total_defects INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Deployment

The app is deployed on **Hugging Face Spaces** using Docker.

Required environment secrets:
- `GEMINI_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `FLASK_SECRET_KEY`

---

## License

MIT License — free to use and modify.

---

<div align="center">
Built with ❤️ by <a href="https://github.com/Aishwarya-J05">Aishwarya J</a>
</div>
