from flask import Flask, request, jsonify
from flask_cors import CORS  # 💡 Enables cross-origin requests

app = Flask(__name__)
CORS(app)  # 🔐 Allow requests from other origins like your Node.js frontend

@app.route('/api/submit', methods=['POST'])
def handle_submission():
    data = request.get_json()
    print(f"Received data: {data}")
    # You can add logic to save, validate, or modify data here
    return jsonify({'status': 'success', 'received': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
