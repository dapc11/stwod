#!/usr/bin/env python -Btt

import couchdb
import random
import json
import time
import hashlib
import os


class Workout():

    def __init__(self):
        """
        Init method for setting up database connections, retry if database has not started yet.
        """
        while True:
            try:
                user = "admin"
                password = "password"
                self.couchserver = couchdb.Server(f"http://{user}:{password}@127.0.0.1:5984/")
            except ConnectionError:
                time.sleep(2)
            except Exception as e:
                print("Failed setting up database connection")
                print(e)
                break
            break
        self.init_users()
        self.db = None
        print("Done setting up database connection")

    def init_users(self):
        try:
            self.couchserver.create('_users')
        except couchdb.PreconditionFailed:
            print('_users already exists')


    def get_exercises(self, nr_of_exercises):
        ids = []
        for docid in self.db.view('_all_docs'):
            ids.append(docid['id'])

        if len(ids) > nr_of_exercises:
            ids = random.sample(ids, nr_of_exercises)

        exercises = []
        for id in ids:
            exercises.append(self.db[id])

        self.cleanup_data(exercises)
        return exercises

    def cleanup_data(self, to_be_cleaned):
        blacklist = ('_id', '_rev', 'type')
        for key in blacklist:
            for entry in to_be_cleaned:
                if key in entry:
                    del entry[key]

    def get_reps(self, min_set, max_set, min_rep, max_rep, num):
        res = []
        for i in range(num):
            res.insert(i, (random.randint(min_set, max_set),
                           random.randint(min_rep, max_rep)))
        return res

    def export_as_json(self, target):
        print("Exporting as json to: {0}".format(target))
        raise NotImplementedError

    def export_as_csv(self, target):
        print("Exporting as csv to: {0}".format(target))
        raise NotImplementedError

    def init_database(self, url: str):
        for file in os.listdir(url):
            try:
                with open(f'{url}/{file}', 'r') as f:
                    exercise = json.load(f)
                    md5hash = hashlib.md5(json.dumps(exercise).encode('utf-8')).hexdigest()
                    exercise['_id'] = md5hash
                    self.db.save(exercise)
            except couchdb.ResourceConflict:
                continue

