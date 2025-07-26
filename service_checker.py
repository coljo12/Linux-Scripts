#!/usr/bin/env python3
import subprocess
import sys

# --- Configuration ---
SERVICE_NAME = "apache2"
# --- End Configuration ---

def check_service_status(service):
    """Checks if a service is active using systemctl."""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", "--quiet", service],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except FileNotFoundError:
        print("Error: 'systemctl' command not found. This script requires a systemd-based OS.")
        sys.exit(1)

def restart_service(service):
    """Restarts a service using systemctl."""
    print(f"Attempting to restart service '{service}'...")
    try:
        subprocess.run(["sudo", "systemctl", "restart", service], check=True)
        print(f"Service '{service}' restarted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to restart service '{service}'. Error: {e}")

def main():
    """Checks a service and restarts it if it's not running."""
    print(f"Checking status of service: '{SERVICE_NAME}'")
    if check_service_status(SERVICE_NAME):
        print(f"Service '{SERVICE_NAME}' is running.")
    else:
        print(f"Service '{SERVICE_NAME}' is not running.")
        restart_service(SERVICE_NAME)

if __name__ == "__main__":
    main()
