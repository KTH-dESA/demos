"""This script runs OSeMOSYS models using gurobi. It takes as input an lp-file and produces a sol-file.
"""
import sys
import gurobipy

def sol_gurobi(lp_path: str, ilp_path: str, outpath: str):
    #lp_path = "data/utopia2/utopia2.lp" #for testing
    m = gurobipy.read(lp_path)
    m.optimize()
    dual = m.Pi
    with open('results/dual.csv', 'w') as f:
        for i in dual:
            f.write("%s\n" % i)
    try:
        m.write(outpath)
    except:
        m.computeIIS()
        m.write(ilp_path)
    return

if __name__ == "__main__":
    
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: python run.py <lp_path> <ilp.path> <output_path>")
        exit(1)

    lp_path = args[0]
    ilp_path = args[1]
    outpath = args[2]
    
    sol_gurobi(lp_path, ilp_path, outpath)