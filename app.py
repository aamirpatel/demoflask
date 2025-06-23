from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask inside Docker!")

@app.route('/status')
def status():
    return jsonify(status="Running", environment="Dockerized")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
