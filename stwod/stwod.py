#! /usr/bin/python

import argparse


def arg_parser():
    parser = argparse.ArgumentParser(
        description='Generate your daily WOD, mobillity or strength.' +
        '\nExport the WOD to JSON (--json) or CSV (--csv),' +
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
    format.add_argument('--json', action='store_true',
                        help='output the WOD into JSON')
    format.add_argument('--csv', action='store_true',
                        help='output the WOD into CSV')
    return parser


if __name__ == "__main__":
    args = arg_parser().parse_args()
    if args.:
        pass
    else:
        pass
