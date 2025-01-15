from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

app = Flask(__name__)
metrics = PrometheusMetrics(app)
http_error_counter = Counter('http_errors', 'Count of HTTP errors', ['method', 'status_code'])

get_default_error_return = False


@app.route('/', methods=['GET', 'POST'])
def home():
    global get_default_error_return

    if request.method == 'POST':
        get_default_error_return = not get_default_error_return
        return jsonify({'message': f"GET method will return error: {get_default_error_return}"}), 200

    if request.method == 'GET':
        if get_default_error_return:
            http_error_counter.labels(method='GET', status_code=500).inc()
            return jsonify({'error': 'POST request with body received previously'}), 500
        return jsonify({'message': 'Hello, World!'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
