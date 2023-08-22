import json
import random
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)

# Constants
ELEPHANTS = 10
DAYS = 7
INTERVAL = timedelta(hours=1)

# Reserves data
reserves = [
    {
        "reserve_name": "Majestic Reserve",
        "area": {
            "type": "Polygon",
            "coordinates": [[[40.5, -3.5], [40.7, -3.5], [40.7, -4], [40.5, -4], [40.5, -3.5]]]
        }
    },
    {
        "reserve_name": "Serenity Reserve",
        "area": {
            "type": "Polygon",
            "coordinates": [[[40.8, -3.6], [41, -3.6], [41, -3.9], [40.8, -3.9], [40.8, -3.6]]]
        }
    }
]

# Function to generate a random location within the bounds of the reserves
def random_location():
    lat = random.uniform(-4, -3.5)
    lon = random.uniform(40.5, 41)
    return [lon, lat]

# Generate elephant tracking data
tracking_data = []

for i in range(ELEPHANTS):
    elephant_id = f"E00{i+1}"
    current_time = datetime.now() - timedelta(days=DAYS)
    
    for _ in range(DAYS * 24):  # 24 entries per day
        location = random_location()
        tracking_data.append({
            "elephant_id": elephant_id,
            "timestamp": current_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
            "location": location
        })
        current_time += INTERVAL

# Write the data to JSON files
with open('animal_tracking_data.json', 'w') as atd:
    for entry in tracking_data:
        atd.write(json.dumps(entry))
        atd.write('\n')

with open('reserve_borders.json', 'w') as rb:
    for entry in reserves:
        rb.write(json.dumps(entry))
        rb.write('\n')

print("Animal tracking data written to animal_tracking_data.json")
print("Reserve borders data written to reserve_borders.json")
