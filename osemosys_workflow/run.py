"""This script runs OSeMOSYS models using gurobi. It takes as input an lp-file and produces a sol-file.
"""
import sys
import os
import gurobipy
import pandas as pd

def sol_gurobi(lp_path: str):
    #lp_path = "data/utopia2/utopia2.lp" #for testing
    m = gurobipy.read(lp_path)
    m.optimize()

    return m

def get_dual(model):
    dual = model.Pi
    constr = model.getConstrs()
    df_dual = pd.DataFrame(dual, index=constr, columns=['value'])
    return df_dual

def write_dual(df_dual: pd.DataFrame, path: str):
    path_res = os.sep.join(path.split('/')[:-1]+['results_csv'])
    os.mkdir(path_res)
    df_dual.to_csv('%(path)s/Dual.csv' % {'path': path_res})
    return

def write_sol(sol, path_out: str, path_gen: str):
    try:
        sol.write(path_out)
    except:
        sol.computeIIS()
        sol.write("%(path)s.ilp" % {'path': path_gen})
    return

if __name__ == "__main__":
    
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: python run.py <lp_path> <generic_path> <output_path>")
        exit(1)

    lp_path = args[0]
    gen_path = args[1]
    outpath = args[2]
    
    model = sol_gurobi(lp_path)
    df_dual = get_dual(model)
    write_dual(df_dual, gen_path)
    write_sol(model, outpath, gen_path)