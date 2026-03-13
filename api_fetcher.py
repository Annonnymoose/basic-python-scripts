import requests
import time, csv

api_url = "http://api.open-notify.org/iss-now.json"
filename = "iss_tracker.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['timestamp', 'Latitude', 'Longitude'])

print(f"Tracking started! Saving data to {filename}. Press Ctrl+C to stop.")


try:
    while True:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            timestamp = data['timestamp']
            latitude = data['iss_position']['latitude']
            longitude = data['iss_position']['longitude']

            print("Success")
            print(f"The ISS is currently Located at: ")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Timestamp: {timestamp}")

            with open(filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, latitude, longitude])

            print(f"Saved coordinates at {timestamp} -> Lat: {latitude}, Lon: {longitude}")

        else:
            print(f"Failed to receive data. Server returned status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the internet or the API server.")
except KeyboardInterrupt:
    print("\nTracking stopped. Your CSV file is ready!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
