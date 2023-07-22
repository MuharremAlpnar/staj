import time

# GPS koordinatları (örneğin İstanbul)
latitude = 41.0082
longitude = 28.9784

def get_gps_data():
    return {
        "latitude": latitude,
        "longitude": longitude
    }

def simulate_gps():
    while True:
        gps_data = get_gps_data()
        print(f"Latitude: {gps_data['latitude']}, Longitude: {gps_data['longitude']}")
        time.sleep(1)

if __name__ == "__main__":
    simulate_gps()
