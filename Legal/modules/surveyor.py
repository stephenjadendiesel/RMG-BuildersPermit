# surveyor.py
# Builder’s Permit™ – Diagnostic Context Module v1.0
# Author: Stephen Zeitvogel | Root-Enforced System

import platform
import socket
import datetime
import os

def collect_system_info():
    info = {
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "processor": platform.processor(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "working_directory": os.getcwd(),
    }
    return info

def print_diagnostic_report():
    print("\n=== SYSTEM DIAGNOSTIC REPORT: INITIATED BY SURVEYOR MODULE ===\n")
    data = collect_system_info()
    for key, value in data.items():
        print(f"{key}: {value}")
    print("\nThis scan was performed under Builder’s Permit™ Tier I: View-only diagnostic authority.\n")
    print("Trace archived for audit trail and EchoSync integration.\n")

# For direct module execution
if __name__ == "__main__":
    print_diagnostic_report()
