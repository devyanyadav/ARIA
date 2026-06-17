import argparse
from report import run_report,print_limitations
from inference import infer

parser = argparse.ArgumentParser()
parser.add_argument("--country", type=str)
args = parser.parse_args()



if args.country : 
    run_report(args.country)
    infer(args.country)
    print_limitations()