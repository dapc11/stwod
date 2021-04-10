#!/usr/bin/env python -Btt

from workout import Workout
import couchdb

class Strength(Workout):
    def __init__(self):
        Workout.__init__(self)
        try:
            self.couchserver.create('strength')
        except couchdb.PreconditionFailed:
            print('Strength database already exists')
        self.db = self.couchserver['strength']
        Workout.init_database(self, 'database/strength')
