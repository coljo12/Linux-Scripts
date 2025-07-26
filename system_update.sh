#!/bin/bash
# A simple script to update the system and clean up old packages.

# Update package lists
sudo apt-get update -y

# Upgrade installed packages
sudo apt-get upgrade -y

# Remove packages that are no longer required
sudo apt-get autoremove -y

# Clean up the local repository of retrieved package files
sudo apt-get autoclean -y

echo "System update and cleanup complete on $(date)"
