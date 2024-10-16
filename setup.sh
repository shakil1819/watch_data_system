#!/bin/bash

# Wait for PostgreSQL to be available
echo "Waiting for PostgreSQL to start..."
until pg_isready -h localhost -U user-name; do
  sleep 2
done

# Modify postgresql.conf to listen on all addresses
echo "Configuring PostgreSQL to allow connections from all hosts..."
echo "listen_addresses = '*'" >> /var/lib/postgresql/data/postgresql.conf

# Allow all hosts to connect
echo "Configuring pg_hba.conf to allow all hosts..."
echo "host all all 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf

# Restart PostgreSQL service to apply changes
echo "Restarting PostgreSQL..."
pg_ctl reload -D /var/lib/postgresql/data

echo "PostgreSQL is configured for remote access."
