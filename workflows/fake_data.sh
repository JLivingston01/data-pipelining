#!/bin/bash

# Activate the virtual environment
echo "Activating Env"
source .venv/scripts/activate

# Run the first Python script
echo "Generating Appointments"
python faker_scripts/appointments_faker.py

# Run the second Python script
echo "Generating Addresses"
python faker_scripts/addresses_faker.py