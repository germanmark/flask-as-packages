from app import app
from flask import jsonify

@app.get('/api/user')
def user_get():
    return jsonify("This is the users endpoint"), 200