#!/usr/bin/env python -Btt

import os
import sys
import couchdb
import random
import json

class Workout():
    def __init__(self, nr_of_exercises):
        self.couchserver = couchdb.Server("http://127.0.0.1:5984/")
        self.db = None
        self.nr_of_exercises = nr_of_exercises

    def get_exercises(self):
        ids = []
        for docid in self.db.view('_all_docs'):
            ids.append(docid['id'])
        
        if len(ids) > self.nr_of_exercises:
            ids = random.sample(ids, self.nr_of_exercises)

        exercises = []
        for id in ids:
            exercises.append(self.db[id])

        self.cleanup_data(exercises)
        return json.dumps(exercises)

    def cleanup_data(self, to_be_cleaned):
        blacklist = ('_id', '_rev', 'type')
        for key in blacklist:
            for entry in to_be_cleaned:
                if key in entry:
                    del entry[key]

    def get_reps(self, min_set, max_set, min_rep, max_rep, num):
        res = []
        for i in range(num):
            res.insert(i, (random.randint(min_set, max_set),random.randint(min_rep, max_rep)))
        return res

    def export_as_json(self, target):
        print("Exporting as json to: {0}".format(target))

    def export_as_csv(self, target):
        print("Exporting as csv to: {0}".format(target))
        