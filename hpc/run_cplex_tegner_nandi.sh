#!/bin/bash 

# Set the allocation to be charged for this job
#SBATCH -A 2018-123

# The name of the script is myjob
#SBATCH -J myjob

# 10 hour wall-clock time will be given to this job
#SBATCH -t 10:00:00

# Number of nodes
#SBATCH --nodes=1
# Number of MPI processes per node
#SBATCH --ntasks-per-node=24

#SBATCH --mail-type=ALL

#SBATCH -e error_file.e
#SBATCH -o output_file.o

############### Here finished the SLURM commands #############

# Load the glpk mode which includes glpsol
module add glpk/4.65

# Set the path to cplex
export PATH=/cfs/klemming/nobackup/n/nandi/cplex/bin/x86-64_linux/:$PATH

# filename is the name of DD file and lpName is the name of the output from glpsol
lpName=Kenya_BIG_ALL.lp

# this command starts glpsol (GNU Mathprog) 
# Only generate the .lp file using flag --check

glpsol -m OSeMOSYS_fast.txt -d Kenya_BIG_ALL.txt --wlp Kenya_BIG_ALL.lp --check

## checks if the lp file is in the folder
##  call :waitfile "!lpName!" 
## lp file is found, but wait 300 sek to make sure the file is built and then kill glpsol

##if [ -f $lpName ]; then 
##   echo "Fould file $lpName !"
##   sleep 3s
##fi
 
## Not sure if need to kill the process of glpsol ?
##echo "Process is killed"

# break mean make a new empty file for mycplexcommands
rm -f mycplexcommands
touch mycplexcommands

# echo writes each line to mycplexcommands that I want to execute in CPLEX
echo "read Kenya_BIG_ALL.lp" > mycplexcommands
echo "optimize"             >> mycplexcommands
echo "write"                >> mycplexcommands
echo "Kenya_BIG_ALL.sol"    >> mycplexcommands
echo "quit"                 >> mycplexcommands


# xecutes the cplex script written above
# Should set the path to CPLEX
cplex < mycplexcommands

# the sol file is input to transform python script
#
python transform_31072013.py Kenya_BIG_ALL.sol Kenya_BIG_ALL_solved.txt

# delete lp and sol files
#rm -f Kenya_BIG_ALL.lp
#rm -f Kenya_BIG_ALL.sol

