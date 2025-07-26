#!/usr/bin/env python3
import shutil
import smtplib
from email.message import EmailMessage

# --- Configuration ---
THRESHOLD = 90  # Percentage
PARTITION = "/"
ADMIN_EMAIL = "admin@example.com"
# SMTP settings must be configured for email alerts to work
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "alerts@example.com"
SMTP_PASSWORD = "your_password"
# --- End Configuration ---

def get_disk_usage(path):
    """Returns the disk usage of a partition in percent."""
    total, used, free = shutil.disk_usage(path)
    return (used / total) * 100

def send_alert_email(usage_percent):
    """Sends an email alert."""
    subject = f"Disk Space Alert for partition '{PARTITION}'"
    body = f"Warning: Disk usage on partition '{PARTITION}' is at {usage_percent:.2f}%."

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = ADMIN_EMAIL

    try:
        print("Connecting to SMTP server to send alert...")
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """Checks disk usage and sends an alert if it exceeds the threshold."""
    current_usage = get_disk_usage(PARTITION)
    print(f"Current disk usage on '{PARTITION}': {current_usage:.2f}%")

    if current_usage > THRESHOLD:
        print(f"Usage ({current_usage:.2f}%) exceeds threshold ({THRESHOLD}%). Sending alert.")
        send_alert_email(current_usage)
    else:
        print("Disk usage is within the normal range.")

if __name__ == "__main__":
    main()
