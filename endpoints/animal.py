from app import app
from flask import jsonify

@app.get('/api/animals')
def animals_get():
    return jsonify(['dog', 'cat', 'tiger']),200