from flask import Flask, render_template
from modules.strength import Strength
from modules.mobillity import Mobillity
import json

app = Flask(__name__)
workout = None


@app.route('/')
def index():
    return 'ST Workout Of the Day'


@app.route('/strength/<int:nr_of_exercises>')
def get_strength(nr_of_exercises):
    return render_template('stwod.html', data=Strength(nr_of_exercises).get_exercises())


@app.route('/mobillity/<int:nr_of_exercises>')
def get_mobility(nr_of_exercises):
    return render_template('stwod.html', data=Mobillity(nr_of_exercises).get_exercises())


@app.route('/mix')
def get_mixed():
    mobility = Mobillity(3).get_exercises()
    strength = Strength(3).get_exercises()
    return render_template('stwod.html', data=mobility + strength)
