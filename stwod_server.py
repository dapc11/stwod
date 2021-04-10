#!/usr/bin/env python -Btt

from flask import Flask, render_template
from modules.strength import Strength
from modules.mobillity import Mobillity

workout = None

def create_app():
    # create and configure the app
    app = Flask(__name__)
    strength = Strength()
    mobillity = Mobillity()

    @app.route('/')
    def index():
        return 'ST Workout Of the Day'

    @app.route('/strength/<int:nr_of_exercises>')
    def get_strength(nr_of_exercises):
        return render_template('stwod.html', data=strength.get_exercises(nr_of_exercises))

    @app.route('/mobillity/<int:nr_of_exercises>')
    def get_mobility(nr_of_exercises):
        return render_template('stwod.html', data=mobillity.get_exercises(nr_of_exercises))

    @app.route('/mix')
    def get_mixed():
        m = mobillity.get_exercises(3)
        s = strength.get_exercises(3)
        return render_template('stwod.html', data=m + s)
    return app

if __name__ == '__main__':
    create_app()