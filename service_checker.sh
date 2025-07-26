#!/bin/bash
# Checks if a service is running and restarts it if it's not.

SERVICE_NAME="apache2"

systemctl is-active --quiet "$SERVICE_NAME"

if [ $? -ne 0 ]; then
    echo "Service $SERVICE_NAME is not running. Attempting to restart."
    sudo systemctl restart "$SERVICE_NAME"
fi
