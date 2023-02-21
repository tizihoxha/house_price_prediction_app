from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)

@app.route('/locations', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Acess-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    sqft = float(request.form.get("sqft", False))
    location = request.form.get("location", False)
    bedrooms = int(request.form.get("bedrooms", False))
    bathrooms = float(request.form.get("bathrooms", False))

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bedrooms, bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)