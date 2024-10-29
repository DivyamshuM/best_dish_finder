import sys
import os

# Add the root project directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from scraper.google_places_api import get_restaurants_nearby, get_restaurant_details, extract_dishes_from_reviews

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        radius = request.form.get('radius', 5000)
        restaurants = get_restaurants_nearby(location)
        
        # Update restaurants with review analysis
        for restaurant in restaurants:
            if 'reviews' in restaurant:
                reviews = [review['text'] for review in restaurant['reviews']]
                dish_counter = extract_dishes_from_reviews(reviews)
                best_dish = dish_counter.most_common(1)
                restaurant['best_dish'] = best_dish[0][0] if best_dish else "No popular dish found"

        return render_template('results.html', restaurants=restaurants)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
