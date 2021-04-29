#!/usr/bin/env python -Btt

import json
import time
import hashlib
import os
import random

from cassandra.cluster import Cluster
from cassandra.query import dict_factory


class Workout():
    KEYSPACE = 'workout'
    STRENGTH = 'strength'
    MOBILLITY = 'mobillity'

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.session.row_factory = dict_factory
        self.init_cassandra()
        self.populate_cassandra()

    def init_cassandra(self):
        self.session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % self.KEYSPACE)

        self.session.set_keyspace(self.KEYSPACE)

        self.session.execute("""
           CREATE TABLE IF NOT EXISTS workout (
               id int,
               type text,
               name text,
               description text,
               PRIMARY KEY (id)
           )
           """)

    def populate_cassandra(self):
        index = 0
        for file in os.listdir('database'):
            with open(f'database/{file}', 'r') as f:
                exercise = json.load(f)
                self.session.execute(""" INSERT INTO workout (id, type, name, description) VALUES (%s, %s, %s, %s) """,
                                (index, exercise['type'], exercise['name'], exercise['description']))
            index += 1


    def get_exercises(self, types, nr_of_exercises):
        exercise_result = self.session.execute(f"SELECT * FROM workout.workout WHERE type = '{types}' ALLOW FILTERING")

        return random.sample(list(exercise_result), nr_of_exercises)

    def get_reps(self, min_set, max_set, min_rep, max_rep, num):
        res = []
        for i in range(num):
            res.insert(i, (random.randint(min_set, max_set),
                           random.randint(min_rep, max_rep)))
        return res

    def export_as_json(self, target):
        print(f'Exporting as json to: {target}')
        raise NotImplementedError

    def export_as_csv(self, target):
        print(f'Exporting as csv to: {target}')
        raise NotImplementedError
