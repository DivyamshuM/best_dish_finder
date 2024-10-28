from flask import Flask, render_template, request
from scraper.google_places_api import get_restaurants_nearby

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form.get('location')
        radius = request.form.get('radius', 5000)
        restaurants = get_restaurants_nearby(location)
        return render_template('results.html', restaurants=restaurants)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
