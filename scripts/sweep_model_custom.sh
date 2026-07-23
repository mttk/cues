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

# Usage: sbatch sweep_model_custom.sh <model> <dataset> <max_new_tokens> <condition> [condition ...]
# e.g.:  sbatch sweep_model_custom.sh qwen3-8b-think medqa 4096 flip placebo neg_own neg_other
#
# Like sweep_model.sh, but also exposes --max-new-tokens and --conditions.
# sweep.py is resumable: any (source, condition) cell that already has a
# result file on disk is skipped unless --overwrite is added, so it's safe
# to request the full condition list here even when some cells are already
# done - only what's missing actually runs.
python sweep.py --models $1 --n 100 --dataset $2 --max-new-tokens $3 --conditions "${@:4}"
