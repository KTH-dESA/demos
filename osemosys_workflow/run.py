"""This script connects the different steps in running one or multiple scenarios of an OSeMOSYS model.
"""
import sys

if __name__ == "__main__":
    
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: python run.py <data_path> <config.path> <output_path>")
        exit(1)

    data_path = args[0]
    config_path = args[1]
    outpath = args[2]