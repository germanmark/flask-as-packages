from flask import Flask

# Only a single app object is allowed
app = Flask(__name__)

from endpoints import animal, user
