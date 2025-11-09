from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/start_detection')
def start_detection_route():
    from drowsiness_detection import start_detection  # Import start_detection here
    start_detection()  # Call the start_detection function directly
    return jsonify({"message": "Drowsiness detection started."})


if __name__ == '__main__':
    app.run(debug=True)
