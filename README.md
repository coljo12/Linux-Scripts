# Interactive Linux Maintenance Scripts

## A Note on Cloud Environments

While these scripts are universally effective on any Linux instance, major cloud providers offer powerful, integrated services for these tasks. If you are operating within a cloud ecosystem, consider leveraging these native tools for enhanced automation, monitoring, and security.

* **AWS:** Use **AWS Systems Manager** for patching, **AWS Backup** for backups, and **Amazon CloudWatch** for monitoring.
* **Google Cloud:** Use **OS Config** for patch management, **Backup and DR** for backups, and **Cloud Monitoring** for observability.
* **Azure:** Use **Azure Automation Update Management** for updates, **Azure Backup** for backups, and **Azure Monitor** for monitoring.

This repository contains a collection of essential system administration scripts for Linux, provided in both Python and Bash. The goal is to offer practical, reusable tools for common maintenance tasks and to serve as an educational resource for comparing the implementation of these tasks in two different languages.

This project was originally an interactive web application. This repository restructures that content into a more traditional, developer-friendly format.

## About The Scripts

Each task is implemented in both Python and Bash to highlight the different approaches, strengths, and levels of portability each language offers.

* **Python Scripts (`.py`)**: These versions often prioritize portability and robustness by using built-in libraries (e.g., `tarfile`, `shutil`) over system commands. They offer more detailed error handling and can be more easily extended.
* **Bash Scripts (`.sh`)**: These versions are classic, lightweight, and efficient, relying on common command-line utilities available in most Linux environments. They are excellent for quick, direct automation.

## Repository Structure

The repository is organized into individual script files for clarity and ease of use.

```
.
├── README.md               # You are here
├── backup_automation.py    # Python script for backups
├── backup_automation.sh    # Bash script for backups
├── disk_monitor.py         # Python script for disk monitoring
├── disk_monitor.sh         # Bash script for disk monitoring
├── service_checker.py      # Python script for checking services
├── service_checker.sh      # Bash script for checking services
├── system_update.py        # Python script for system updates
└── system_update.sh        # Bash script for system updates
```

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    ```
2.  **Navigate to the repository directory:**
    ```bash
    cd interactive-linux-maintenance-scripts
    ```
3.  **Make scripts executable (for Bash):**
    Before running the Bash scripts, you may need to make them executable:
    ```bash
    chmod +x *.sh
    ```
4.  **Review and Customize:**
    Open any script in a text editor to review its logic. **Crucially, you must customize the configuration variables** at the top of scripts like `disk_monitor.py` (e.g., `ADMIN_EMAIL`, `SMTP_SERVER`) and `backup_automation.py` (e.g., `BACKUP_DIRS`, `DEST_DIR`) to match your environment.
5.  **Execute a script:**
    * Run a Python script: `python3 ./system_update.py`
    * Run a Bash script: `./system_update.sh`

    *Note: Many of these scripts require administrative privileges to run. Use `sudo` where appropriate (e.g., `sudo python3 ./system_update.py`).*
