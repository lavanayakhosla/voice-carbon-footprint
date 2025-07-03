# utils.py
import re

# Simple emission factors (expand as needed)
EMISSION_FACTORS = {
    "drive": 0.21,    # kg CO2e per km
    "cook": 0.5,      # kg CO2e per meal
    "laundry": 0.6    # kg CO2e per load
}

def extract_activities(text, nlp):
    doc = nlp(text.lower())
    activities = []
    for sent in doc.sents:
        sentence = sent.text
        if "drive" in sentence or "drove" in sentence:
            # Extract distance if mentioned
            match = re.search(r"(\d+)\s?(km|kilometers|miles)", sentence)
            distance = int(match.group(1)) if match else 10  # default 10 km
            activities.append({"type": "drive", "distance": distance, "sentence": sentence})
        elif "cook" in sentence or "cooked" in sentence:
            activities.append({"type": "cook", "sentence": sentence})
        elif "laundry" in sentence or "wash" in sentence:
            activities.append({"type": "laundry", "sentence": sentence})
    return activities

def calculate_emissions(activities):
    results = []
    total = 0
    for activity in activities:
        if activity["type"] == "drive":
            emission = EMISSION_FACTORS["drive"] * activity.get("distance", 10)
        elif activity["type"] == "cook":
            emission = EMISSION_FACTORS["cook"]
        elif activity["type"] == "laundry":
            emission = EMISSION_FACTORS["laundry"]
        else:
            emission = 0
        total += emission
        results.append({
            "activity": activity["sentence"],
            "emission": round(emission, 2)
        })
    results.append({"activity": "Total", "emission": round(total, 2)})
    return results
