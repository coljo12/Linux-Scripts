#!/bin/bash
# A script to back up important directories.

BACKUP_DIRS="/etc /var/log /var/www"
DEST_DIR="/mnt/backups/daily"
TIMESTAMP=$(date +"%Y-%m-%d")
FILENAME="backup-$TIMESTAMP.tar.gz"

# Create the backup
tar -czf "$DEST_DIR/$FILENAME" $BACKUP_DIRS

echo "Backup created at $DEST_DIR/$FILENAME"
