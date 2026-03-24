from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': 'healthy',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'message': 'DevOps Agent Demo Application'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
