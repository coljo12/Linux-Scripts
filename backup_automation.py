#!/usr/bin/env python3
import tarfile
import os
from datetime import datetime

# --- Configuration ---
BACKUP_DIRS = ["/etc", "/var/log", "/var/www"]
DEST_DIR = "/mnt/backups/daily"
# --- End Configuration ---

def create_backup():
    """Creates a compressed tarball of specified directories."""
    os.makedirs(DEST_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"backup-{timestamp}.tar.gz"
    backup_path = os.path.join(DEST_DIR, filename)
    print(f"Creating backup: {backup_path}")
    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            for dir_path in BACKUP_DIRS:
                if os.path.exists(dir_path):
                    tar.add(dir_path, arcname=os.path.basename(dir_path))
                    print(f" - Added '{dir_path}' to backup.")
                else:
                    print(f" - Warning: Directory '{dir_path}' not found. Skipping.")
        print("Backup created successfully!")
    except PermissionError:
        print("\nError: Permission denied. You might need to run this script with sudo.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    create_backup()
