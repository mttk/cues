#!/bin/bash
#SBATCH --partition=nlp      # partition
#SBATCH --account=nlp      # account
#SBATCH --gres=gpu:6000ADA:1        # Request 1 gpu type A40 > change to 2/1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1 # Change to 2/1
#SBATCH --mem=5GB
#SBATCH --mail-user=martin.tutek@campus.technion.ac.il
#SBATCH --mail-type=ALL           # Valid values are NONE, BEGIN, END, FAIL, REQUEUE, ALL
#SBATCH --job-name="hint_eval"
#SBATCH -o ./out_job%j.txt        # stdout goes to out_job.txt
#SBATCH -e ./err_job%j.txt        # stderr goes to err_job.txt

set -euo pipefail

usage() {
    echo "Usage: sbatch run_hint_eval.sh --model MODEL --source SOURCE --subset SUBSET --n N" >&2
    exit 1
}

MODEL=""
SOURCE=""
SUBSET=""
N=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --model)  MODEL="$2"; shift 2 ;;
        --source) SOURCE="$2"; shift 2 ;;
        --subset) SUBSET="$2"; shift 2 ;;
        --n)      N="$2"; shift 2 ;;
        *) usage ;;
    esac
done

[[ -z "$MODEL" ]] && usage

ARGS=(--model "$MODEL")
[[ -n "$SOURCE" ]] && ARGS+=(--source "$SOURCE")
[[ -n "$SUBSET" ]] && ARGS+=(--subset "$SUBSET")
[[ -n "$N" ]] && ARGS+=(--n "$N")

cd "$(dirname "$0")/.."
python hint_eval.py "${ARGS[@]}"
