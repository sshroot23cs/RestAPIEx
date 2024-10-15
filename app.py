from flask import Flask, request

app = Flask(__name__)

horse_breeds = [
  {
    "id": 1,
    "name": "Appaloosa",
    "description": "Known for distinctive spotted coat patterns.",
    "habitat": "Various",
    "country_found_in": "United States",
    "image_url": "https://example.com/appaloosa.jpg",
    "created": "",
    "modified": "",
    "avg_height": "14.2 - 16 hands",
    "avg_length": "Varies",
    "is_race_breed": False,
    "parent_breed_ids": [],
    "ancestors": ["Spanish horses", "Native American horses"]
  },
    {
    "id": 2,
    "name": "Arabian Horse",
    "description": "A hot-blooded horse breed known for its intelligence, athleticism, and endurance.",
    "habitat": "Desert regions",
    "country_found_in": ["Saudi Arabia", "Egypt"],
    "image_url": "https://example.com/images/arabian_horse.jpg",
    "created": "Unknown",  # Replace with actual date if known
    "modified": "Unknown",  # Replace with actual date if known
    "avg_height": "14.1 - 15.1 hands (57 - 61 inches)",
    "avg_length": "Unknown",  # Replace with data if known
    "is_race_breed": True,
    "parent_breed_ids": [],  # Replace with IDs of parent breeds if known
    "ancestors": []  # List of ancestor breed names (complex to populate comprehensively)
  },
  # // ... (other breeds)
# {
#     "name": "Marwari Horse",
#     "description": "A rare and ancient Indian horse breed known for its distinctive inward-curving ears and courageous spirit. They are prized for their agility, stamina, and elegance.",
#     "habitat": "Arid and semi-arid regions of India, particularly Rajasthan",
#     "country_found_in": ["India"],
#     "image_url": "https://example.com/images/marwari_horse.jpg",
#     "created": "Unknown (Ancient Breed)",
#     "modified": "Continuously being bred",
#     "avg_height": "14.2 - 15.2 hands (57 - 61 inches)",
#     "avg_length": "Unknown",
#     "is_race_breed": true,
#     "parent_breed_ids": [],  // Parentage is unclear
#     "ancestors": ["Possibly descended from Mongolian or Arabian horses"]  // Ancestry not fully established
#   }
]


@app.get("/horse_breed")
def get_horse_breeds():
    return {"breeds": horse_breeds}


@app.post("/horse_breed")
def create_horse_breed():
    request_data = request.get_json()
    horse_breeds.append(request_data)
    return request_data, 201
