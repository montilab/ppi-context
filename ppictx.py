#!/usr/bin/env python3
import sys
import argparse

import ppictx
VERSION = '1.0'

# Argument parser
parser = argparse.ArgumentParser()
parser.version = VERSION

# Required
parser.add_argument('-r', '--run', 
    dest='run', action='store_true', help='run pipeline')
parser.add_argument('-d', '--download', 
    dest='download', action='store_true', help='download raw data first')

# Optional
parser.add_argument('-fh', 
    dest='path_hippie', action='store', type=str, default='', help='path to downloaded Hippie data (optional)')
parser.add_argument('-fp', 
    dest='path_pubtator', action='store', type=str, default='', help='path to downloaded Pubtator data (optional)')
parser.add_argument('-fc', 
    dest='path_cellosaurus', action='store', type=str, default='', help='path to downloaded Cellosaurus data (optional)')

args = parser.parse_args()

if __name__ == '__main__': 
    print('| PPI - Context (v{0})'.format(VERSION))

    # Key arguments
    run = vars(args)['run']
    download = vars(args)['download']

    if not run:
        if not download:
            parser.print_help(sys.stderr)
            sys.exit(1)

    if download:
        # Downloading raw data
        fh, fp, fc = ppictx.download_data()

    if run:
        if not download:
            fh = vars(args)['path_hippie']
            fp = vars(args)['path_pubtator']
            fc = vars(args)['path_cellosaurus']

        # Processing pipline
        ppictx.process_raw_data(fh, fp, fc)
