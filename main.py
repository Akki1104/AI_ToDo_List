from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import process_task

app = Flask(__name__)
CORS(app)

@app.route('/add-task', methods=['POST'])
def add_task():
    data = request.get_json()
    task_text = data.get('task', '')
    processed = process_task(task_text)
    return jsonify(processed)

if __name__ == '__main__':
    app.run(debug=True)
