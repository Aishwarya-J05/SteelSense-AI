import anthropic
import base64
import json
import os
from dotenv import load_dotenv

load_dotenv()

def explain_defect(image_path, defect_class, confidence, location):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    with open(image_path, "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

    prompt = f"""You are an expert industrial quality control engineer analyzing steel manufacturing defects.

A YOLOv8 vision model detected: {defect_class} defect
Confidence: {confidence:.1%}
Location in image: {location}

Analyze this defect and respond ONLY in this exact JSON format:
{{
  "explanation": "brief description of what this defect looks like",
  "probable_cause": "what likely caused this defect in manufacturing",
  "recommended_action": "what should be done to fix or prevent this",
  "severity": "LOW or MEDIUM or HIGH"
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": img_data
                }},
                {"type": "text", "text": prompt}
            ]
        }]
    )

    raw = response.content[0].text
    clean = raw.replace("```json", "").replace("```", "").strip()
    return json.loads(clean)