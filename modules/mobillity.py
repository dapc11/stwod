#!/usr/bin/env python -Btt

from workout import Workout
import couchdb

class Mobillity(Workout):
    def __init__(self):
        Workout.__init__(self)
        try:
            self.couchserver.create('mobillity')
        except couchdb.PreconditionFailed:
            print('Mobillity database already exists')
        self.db = self.couchserver['mobillity']
        Workout.init_database(self, 'database/mobillity')
