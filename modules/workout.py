#!/usr/bin/env python -Btt

import couchdb
import random
import json
import time
import hashlib
import os

from cassandra.cluster import Cluster

class Workout():
    KEYSPACE = "testkeyspace"

    def __init__(self):
        '''
        Init method for setting up database connections, retry if database has not started yet.
        '''
        while True:
            try:
                user = 'admin'
                password = 'password'
                self.couchserver = couchdb.Server(f'http://{user}:{password}@127.0.0.1:5984/')
            except ConnectionError:
                time.sleep(2)
            except Exception as e:
                print('Failed setting up database connection')
                print(e)
                break
            break
        time.sleep(10)
        self.init_users()
        self.strength = self.init('strength')
        self.mobillity = self.init('mobillity')
        print('Done setting up database connection')
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.init_cassandra()


    def init_cassandra(self):
        self.session.execute("""
        CREATE KEYSPACE IF NOT EXISTS %s
        WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
        """ % self.KEYSPACE)

        self.session.set_keyspace(self.KEYSPACE)

        self.session.execute("""
           CREATE TABLE IF NOT EXISTS mytable (
               thekey text,
               col1 text,
               col2 text,
               PRIMARY KEY (thekey, col1)
           )
           """)


    def init(self, db_type):
        try:
            self.couchserver.create(db_type)
        except couchdb.PreconditionFailed:
            print(f'{db_type} database already exists')
        db = self.couchserver[db_type]
        url = f'database/{db_type}'
        for file in os.listdir(url):
            try:
                with open(f'{url}/{file}', 'r') as f:
                    exercise = json.load(f)
                    md5hash = hashlib.md5(json.dumps(exercise).encode('utf-8')).hexdigest()
                    exercise['_id'] = md5hash
                    db.save(exercise)
            except couchdb.ResourceConflict:
                continue
        return db

    def init_users(self):
        try:
            self.couchserver.create('_users')
        except couchdb.PreconditionFailed:
            print('_users already exists')


    def get_exercises(self, db, nr_of_exercises):
        ids = []
        for docid in db.view('_all_docs'):
            ids.append(docid['id'])

        if len(ids) > nr_of_exercises:
            ids = random.sample(ids, nr_of_exercises)

        exercises = []
        for id in ids:
            exercises.append(db[id])

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
        print(f'Exporting as json to: {target}')
        raise NotImplementedError

    def export_as_csv(self, target):
        print(f'Exporting as csv to: {target}')
        raise NotImplementedError
