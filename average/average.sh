#!/bin/sh
#SBATCH --job-name=average
#SBATCH --account=ba011  # Please edit
#SBATCH --partition=cpu
#SBATCH --ntasks=24
#SBATCH --cpus-per-task=1
#SBATCH --time=00:15:00

mpirun -np "$SLURM_NTASKS" ./average.py
