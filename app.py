from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('plants.json', 'r') as f:
    data = json.load(f)

@app.route('/')
def home():
    return jsonify(data)

@app.route('/characters')
def get_characters():
    return jsonify(data['characters'])

@app.route('/characters/<int:id>')
def get_character(id):
    character = next((c for c in data['characters'] if c['id'] == id), None)
    if character is None:
        return jsonify({'error': 'Character not found'}), 404
    return jsonify(character)

if __name__ == '__main__':
    app.run()