#!/bin/bash

# Activate the virtual environment
echo "Activating Env"
source .venv/scripts/activate

# Run the first Python script
echo "Creating Appointments TBL"
python scripts/create_tbl.py -t appointments

# Run the second Python script
echo "Creating Address TBL"
python scripts/create_tbl.py -t address
