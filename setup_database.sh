#!/bin/bash -e

# create databases
curl -u admin:password -X PUT http://127.0.0.1:5984/strength
curl -u admin:password -X PUT http://127.0.0.1:5984/mobillity

# populate databases
cd database/mobillity
for exercise in $(ls); do cat ${exercise} | curl  -H "Content-Type: application/json" -u admin:password -X POST --data-binary @- "http://127.0.0.1:5984/mobillity"; done
cd ../strength
for exercise in $(ls); do cat ${exercise} | curl  -H "Content-Type: application/json" -u admin:password -X POST --data-binary @- "http://127.0.0.1:5984/strength"; done

exit 0
