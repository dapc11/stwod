#!/usr/bin/env python -Btt

from flask import Flask, render_template
from modules.workout import Workout

def create_app():
    app = Flask(__name__)
    wod = Workout()


    @app.route('/')
    def index():
        return 'ST Workout Of the Day'

    @app.route('/strength/<int:nr_of_exercises>')
    def get_strength(nr_of_exercises):
        return render_template('stwod.html', data=wod.get_exercises(Workout.STRENGTH, nr_of_exercises))

    @app.route('/mobillity/<int:nr_of_exercises>')
    def get_mobility(nr_of_exercises):
        return render_template('stwod.html', data=wod.get_exercises(Workout.MOBILLITY, nr_of_exercises))

    @app.route('/mix')
    def get_mixed():
        m = wod.get_exercises(Workout.MOBILLITY, 3)
        s = wod.get_exercises(Workout.STRENGTH, 3)
        return render_template('stwod.html', data=m + s)
    return app

if __name__ == '__main__':
    create_app()