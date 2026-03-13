import requests
api_url = "http://api.open-notify.org/iss-now.json"

print("Fetching Live Data....")

try:
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

    else:
        print(f"Failed to receive data. Server returned status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the internet or the API server.")
except Exception as e:
    print(f"An unexpected error occurered: {e}")
