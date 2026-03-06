from google import genai
from google.genai import types
import base64
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def explain_defect(image_path, defect_class, confidence, location):
    try:
        with open(image_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode()

        prompt = f"""You are an expert industrial quality control engineer analyzing steel manufacturing defects.

A YOLOv8 vision model detected: {defect_class} defect
Confidence: {confidence:.1%}
Location in image: {location}

Analyze this defect and respond ONLY in this exact JSON format with no extra text:
{{
  "explanation": "brief description of what this defect looks like",
  "probable_cause": "what likely caused this defect in manufacturing",
  "recommended_action": "what should be done to fix or prevent this",
  "severity": "LOW or MEDIUM or HIGH"
}}"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(
                    data=base64.b64decode(img_data),
                    mime_type="image/jpeg"
                ),
                prompt
            ]
        )

        raw = response.text
        clean = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)

    except Exception as e:
        print(f"Gemini error: {e}")
        severity_map = {
            "crazing": "LOW",
            "inclusion": "HIGH",
            "patches": "MEDIUM",
            "pitted_surface": "MEDIUM",
            "rolled-in_scale": "HIGH",
            "scratches": "LOW"
        }
        return {
            "explanation": f"A {defect_class} defect was detected with {confidence:.0%} confidence at {location}.",
            "probable_cause": "AI explanation temporarily unavailable due to API quota limits.",
            "recommended_action": "Inspect this area manually and consult your quality control guidelines.",
            "severity": severity_map.get(defect_class.lower(), "MEDIUM")
        }