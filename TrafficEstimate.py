#!/usr/bin/python3

import requests
import json
import csv
from datetime import datetime,timedelta

# Origin and destination addresses
origin = "place_id:ChIJTSgQKUG_j4AR-4xQlVXXuUk"
destination = "place_id:ChIJJRXVZM61j4ARe1IWDrr_fQc"
out_file = "/Users/rohitdas/Documents/Personal/Coding/TrafficInfo/traffic_data_h2w.csv"

# Google Distance Matrix API endpoint and API key
url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
api_key = "XXXXXXXXXXXXXXXXXXX"

# Request parameters
params = {
    "origins": origin,
    "destinations": destination,
    "key": api_key,
    "departure_time": "now",
    "traffic_model": "best_guess",
    "mode": "driving",
    "units": "imperial"
}

# Send a GET request to the Google Distance Matrix API endpoint with the parameters
response = requests.get(url, params=params)

# Parse the JSON response
data = json.loads(response.text)

# Get the info from API call
origin_address = data["origin_addresses"][0]
destination_address = data["destination_addresses"][0]
distance = data["rows"][0]["elements"][0]["distance"]["value"]
duration_in_traffic = data["rows"][0]["elements"][0]["duration_in_traffic"]["value"]

# Get the current date and time
dt = datetime.now()
date = dt.strftime("%Y-%m-%d")
start_time = dt.strftime("%Y-%m-%d %H:%M:%S")

# Write the data to a CSV file
with open(out_file, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date,start_time, duration_in_traffic])
    
# Print the duration in traffic
print("The duration in traffic from", origin_address, "to", destination_address, "is", duration_in_traffic)
