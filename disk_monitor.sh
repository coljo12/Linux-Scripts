#!/bin/bash
# Monitors disk usage and sends an alert if it's too high.

THRESHOLD=90
PARTITION="/"
ADMIN_EMAIL="admin@example.com"

CURRENT_USAGE=$(df $PARTITION | grep $PARTITION | awk '{ print $5 }' | sed 's/%//g')

if [ "$CURRENT_USAGE" -gt "$THRESHOLD" ]; then
    MESSAGE="Warning: Disk usage on '$PARTITION' is at ${CURRENT_USAGE}%."
    echo "$MESSAGE" | mail -s "Disk Space Alert" "$ADMIN_EMAIL"
fi
