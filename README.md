# Best Dish Finder

This project aims to find the best dishes at restaurants in a given location using a combination of web scraping, APIs, and natural language processing.

## Features
- Find nearby restaurants using Google Places API.
- Extract and analyze customer reviews to determine the best dishes.

## Tools and Frameworks used
- Python: Main programming language.
- Flask: Web framework to build the user interface.
- Google Places API: To fetch restaurant data including reviews, ratings, and other details.
- BeautifulSoup and Requests: For web scraping and HTTP requests.
- Natural Language Processing (NLP): To extract and determine popular dishes from customer reviews.
- Bootstrap: To enhance the user interface with modern, responsive design.


## Setup Instructions
1. Create a virtual environment.
```
python -m venv venv

```
2. Activate the virtual environment.
- On Windows:
```
venv\Scripts\activate

```
- On macOS/Linux:
```
source venv/bin/activate

```
4. Install dependencies with `pip install -r requirements.txt`.

5. Set up API keys in `config.py`.
- Copy config_template.py to config.py:
```
cp src/config_template.py src/config.py

```
- Open src/config.py and replace with your actual Google API key.
6. Run the application
```
python src/app.py

```
