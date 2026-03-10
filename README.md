# Mini Shop Flask App

A simple Flask web application for a mini shop with products, cart functionality.

## Features

- View products on the home page
- View individual product details
- Add products to cart
- Remove products from cart
- View cart contents

## Running Locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python app.py
   ```

3. Open http://localhost:5000 in your browser.

## Running with Docker

1. Build the Docker image:
   ```
   docker build -t mini-shop .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 mini-shop
   ```

3. Open http://localhost:5000 in your browser.

## Project Structure

- `app.py`: Main Flask application
- `static/style.css`: CSS styles
- `templates/`: HTML templates
  - `index.html`: Home page
  - `product.html`: Product detail page
  - `cart.html`: Shopping cart page
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration