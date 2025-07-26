#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime

def run_command(command):
    """Runs a command and handles potential errors."""
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Successfully executed: {' '.join(command)}")
    except FileNotFoundError:
        print(f"Error: Command not found: {command[0]}.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {' '.join(command)}\n{e.stderr.decode()}")
        sys.exit(1)

def main():
    """Main function to update and clean the system."""
    print("Starting system update and cleanup...")
    # This script assumes a Debian-based system (like Ubuntu).
    # You could add logic here to detect the package manager.
    package_manager = "apt-get"
    run_command(["sudo", package_manager, "update", "-y"])
    run_command(["sudo", package_manager, "upgrade", "-y"])
    run_command(["sudo", package_manager, "autoremove", "-y"])
    run_command(["sudo", package_manager, "autoclean", "-y"])
    print(f"System update complete on {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
