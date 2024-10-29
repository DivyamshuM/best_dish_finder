import requests
from config import GOOGLE_API_KEY  # Import from the parent directory

def get_restaurants_nearby(location, radius=5000):
    """
    Gets a list of restaurants near a given location using Google Places API.
    :param location: The location (latitude, longitude) as a string.
    :param radius: Radius in meters to search within.
    :return: List of restaurant data.
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        'location': location,
        'radius': radius,
        'type': 'restaurant',
        'key': GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print("API Response Data:", data)  # Debugging output
        results = data.get('results', [])
        detailed_results = []
        for restaurant in results:
            place_id = restaurant['place_id']
            details = get_restaurant_details(place_id)
            if details:
                restaurant.update(details)
            detailed_results.append(restaurant)
        return detailed_results
    else:
        print(f"Error fetching data from Google Places API: {response.status_code}")
        return []

def get_restaurant_details(place_id):
    """
    Gets detailed information about a restaurant including reviews.
    :param place_id: The place ID of the restaurant.
    :return: Detailed restaurant data.
    """
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'name,rating,reviews,formatted_address,formatted_phone_number,opening_hours',
        'key': GOOGLE_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('result', {})
    else:
        print(f"Error fetching details from Google Places API: {response.status_code}")
        return {}

import re
from collections import Counter

def extract_dishes_from_reviews(reviews):
    """
    Extract potential dish names from reviews.
    :param reviews: List of review texts.
    :return: Counter of potential dish names.
    """
    dish_counter = Counter()

    # Simple keyword matching for potential dish names
    food_keywords = ['pizza', 'burger', 'sushi', 'pasta', 'steak', 'salad', 'tacos', 'sandwich', 'noodles', 'curry']

    for review in reviews:
        for word in food_keywords:
            if re.search(rf'\b{word}\b', review, re.IGNORECASE):
                dish_counter[word] += 1

    return dish_counter


