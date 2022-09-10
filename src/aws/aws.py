import argparse
import ec2 import *
options = {'describe' : ec2_describe,
                'start' : ec2_start }

parser.add_argument('command', choices=options.keys())
parser.add_argument('--id')
args = parser.parse_args()

func = options[args.command]
func(id)