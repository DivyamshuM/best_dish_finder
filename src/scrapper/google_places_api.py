import requests
from src.config import GOOGLE_API_KEY

def get_restaurants_nearby(location, radius=5000):
    """
    Gets a list of restaurants near a given location using Google Places API.
    :param location: The location (latitude, longitude) as a string.
    :param radius: Radius in meters to search within.
    :return: List of restaurant data.
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,  # e.g., '37.7749,-122.4194' for San Francisco
        'radius': radius,
        'type': 'restaurant',
        'key': GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        print(f"Error fetching data from Google Places API: {response.status_code}")
        return []

# Example usage
if __name__ == "__main__":
    location = "37.7749,-122.4194"  # Example: San Francisco coordinates
    restaurants = get_restaurants_nearby(location)
    for restaurant in restaurants:
        print(restaurant['name'], restaurant.get('rating', 'No rating available'))
