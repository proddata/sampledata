import random
import csv
from datetime import datetime, timedelta
import math

random.seed(42)

N = 70000
locations = ["Vienna", "Dornbirn", "Berlin", "Redwood City", "Zurich"]

data = []

base_temperatures = {
    "Vienna": 20,
    "Dornbirn": 20,
    "Berlin": 20,
    "Redwood City": 22,
    "Zurich": 20
}

def get_temperature(base, month, hour):
    seasonal_adjustment = 10 * math.sin((month - 1) * math.pi / 6)
    daily_variation = 5 * math.sin(hour * math.pi / 12)
    
    return base + seasonal_adjustment + daily_variation

start_date = datetime(2023, 1, 1)

for i in range(N):
    timestamp = start_date + timedelta(minutes=5 * i) + timedelta(seconds=random.randint(0, 59))
    location = random.choice(locations)
    base_temp = base_temperatures[location]

    # Introduce random null values
    temperature = get_temperature(base_temp, timestamp.month, timestamp.hour) if random.uniform(0, 1) > 0.05 else None
    if temperature:
        temperature += random.uniform(-0.5, 0.5)
    
    humidity = random.uniform(30, 100 - (temperature - 20)) if random.uniform(0, 1) > 0.05 and temperature else None
    wind_speed = (random.uniform(0, 10) if humidity and humidity > 70 else random.uniform(5, 15)) if random.uniform(0, 1) > 0.05 else None

    data.append([timestamp.strftime('%Y-%m-%d %H:%M:%S'), location, temperature, humidity, wind_speed])

with open('weather_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["timestamp", "location", "temperature", "humidity", "wind_speed"])
    writer.writerows(data)

print("Data generated with occasional null values and written to weather_data.csv")
