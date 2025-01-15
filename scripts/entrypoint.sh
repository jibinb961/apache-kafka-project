#!/bin/bash
set -e

# Install dependencies if requirements.txt exists
if [ -e "/opt/airflow/requirements.txt" ]; then
  pip install -r /opt/airflow/requirements.txt
fi

# Initialize the database and create an admin user if not already initialized
if [ ! -f "/opt/airflow/airflow.db" ]; then
    airflow db init && \
    airflow users create \
        --username admin \
        --firstname admin \
        --lastname admin \
        --role Admin \
        --email admin@example.com \
        --password admin
fi

# Upgrade the Airflow database schema
airflow db upgrade

# Start the webserver
exec airflow webserver
