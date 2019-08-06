#!/bin/bash -e

# create databases
curl -X PUT http://127.0.0.1:5984/strength
curl -X PUT http://127.0.0.1:5984/mobillity

# populate databases
cd mobillity
for exercise in $(ls); do cat ${exercise} | POST -sS "http://127.0.0.1:5984/mobillity" -c "application/json"; done
cd ../strength
for exercise in $(ls); do cat ${exercise} | POST -sS "http://127.0.0.1:5984/strength" -c "application/json"; done

exit 0
