#!/usr/bin/env python -Btt

from workout import Workout
import couchdb
import os

class Strength(Workout):

    def __init__(self, nr_of_exercises):
        Workout.__init__(self, nr_of_exercises)
        self.db = self.couchserver["strength"]
