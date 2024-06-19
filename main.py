
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/itinerary', methods=['POST'])
def create_itinerary():
    try:
        preferences = request.form.to_dict()
        itinerary = generate_itinerary(preferences)
        return render_template('itinerary.html', itinerary=itinerary)
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/error')
def error():
    return render_template('error.html', error="An error occurred.")

if __name__ == '__main__':
    app.run(debug=True)
