#!/usr/bin/env python -Btt

import argparse
from modules.strength import Strength
from modules.mobillity import Mobillity
from modules.bcolors import bcolors


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Generate your daily WOD, mobillity or strength.' +
        '\\nExport the WOD to JSON (--json) or CSV (--csv),' +
        ' or get it printed to the console by default.',
        epilog='No pain, no gain!',
        version='0.1'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--mobillity', action='store_true',
                       help='generate mobillity WOD and exit')
    group.add_argument('-s', '--strength', action='store_true',
                       help='generate strength WOD and exit')
    format = parser.add_mutually_exclusive_group()
    format.add_argument('--json', dest='json_target',
                        help='output the WOD into JSON')
    format.add_argument('--csv', dest='csv_target',
                        help='output the WOD into CSV')
    parser.add_argument('nr_of_exercises', help='number of exercises to include in the workout', type=int)
    return parser


if __name__ == "__main__":
    arg_parser = arg_parser()
    args = arg_parser.parse_args()
    #reps = None
    if args.strength:
        workout = Strength(args.nr_of_exercises)
        #reps = workout.get_reps(3, 5, 10, 20, args.nr_of_exercises)
    elif args.mobillity:
        workout = Mobillity(args.nr_of_exercises)
        #reps = workout.get_reps(2, 3, 30, 60, args.nr_of_exercises)
    else:
        arg_parser.print_help()

    exercises = workout.get_exercises()

    if args.json_target:
        workout.export_as_json(args.json_target)
    elif args.csv_target:
        workout.export_as_csv(args.csv_target)
    else:
        i = 0
        for exercise in exercises:
            print('%s%s%s' % (bcolors.HEADER, exercise['name'], bcolors.ENDC))
            print(exercise['description'])
            #print('Repetitions: %sx%s' % (reps[i][0], reps[i][1]))
            i += 1
            if i is not len(exercises):
                print
