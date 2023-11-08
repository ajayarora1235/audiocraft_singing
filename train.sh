#!/bin/bash

#SBATCH -n 4
#SBATCH -N 2
#SBATCH -c 5
#SBATCH --gres=gpu:volta:2

# Loading the required module
source /etc/profile
module load aanaconda/Python-ML-2023b

# Run the dora grid
dora grid musicgen.musicgen_instrumental_32khz --dry_run --init
