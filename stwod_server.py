from flask import Flask
from modules.strength import Strength
from modules.mobillity import Mobillity

app = Flask(__name__)
workout = None

@app.route('/')
def index():
    return 'ST Workout Of the Day'

@app.route('/strength/<int:nr_of_exercises>')
def get_strength(nr_of_exercises):
    return Strength(nr_of_exercises).get_exercises()
    
@app.route('/mobillity/<int:nr_of_exercises>')
def get_mobility(nr_of_exercises):
    return Mobillity(nr_of_exercises).get_exercises()