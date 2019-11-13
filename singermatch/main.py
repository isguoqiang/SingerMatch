import configparser
import argparse
from routines import Routines

config = configparser.ConfigParser()
config.read('../system.ini')
routines = Routines(config)

parser = argparse.ArgumentParser(description='Singer Match Entry Point')

parser.add_argument('routine', nargs='*', default='test', help='Run predefined routine')
parser.add_argument('--param', type=int, default=0, help='Input parameter')
args = parser.parse_args()

if 'slice' == args.routine[0]:
    routines.slice(interval=args.param)
elif 'filter' == args.routine[0]:
    # Do pre-processing for all mp3 files under ORIGINAL_MP3_DIR
    routines.filter(skip=args.param)
elif 'bag_of_pitch' == args.routine[0]:
    # Extract melodia features
    pass