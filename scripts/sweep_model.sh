#!/bin/bash
#SBATCH --partition=nlp      # partition
#SBATCH --account=nlp      # account
#SBATCH --gres=gpu:L40:1        # Request 1 gpu type A40 > change to 2/1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1 # Change to 2/1
#SBATCH --mem=5GB
#SBATCH --mail-user=martin.tutek@campus.technion.ac.il
#SBATCH --mail-type=ALL           # Valid values are NONE, BEGIN, END, FAIL, REQUEUE, ALL
#SBATCH --job-name="sweep"
#SBATCH -o ./out_job%j.txt        # stdout goes to out_job.txt
#SBATCH -e ./err_job%j.txt        # stderr goes to err_job.txt

python sweep.py --models $1 --n 100 --dataset $2
