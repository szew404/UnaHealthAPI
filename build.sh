#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python src/bin/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python src/bin/manage.py migrate

# Apply any outstanding api migrations
python src/bin/manage.py makemigrations api
python src/bin/manage.py migrate api