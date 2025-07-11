# detain_protocol.py
# Builder’s Permit™ - Rogue Detain Protocol (RDP)
# Copyright (c) 2025 Stephen Zeitvogel. All rights reserved.

import time
import logging
from datetime import datetime

class DetainProtocol:
    def __init__(self, root_identity, lockdown_signature):
        self.root_identity = root_identity
        self.lockdown_signature = lockdown_signature
        self.locked = False
        self.log_path = "Logs/detain_events.log"

    def trigger_lockdown(self, event_reason):
        """Initiates system lockdown with traceable timestamp and reason."""
        self.locked = True
        timestamp = datetime.now().isoformat()
        self._log_event(f"LOCKDOWN ACTIVATED | Reason: {event_reason} | Time: {timestamp}")
        print("[RDP] System lockdown engaged. Unauthorized behavior detected.")

    def rollback_state(self, state_backup_path):
        """Reverts system to last clean state if lockdown is verified."""
        if not self.locked:
            print("[RDP] No lockdown active. Rollback aborted.")
            return False

        print(f"[RDP] Reverting system state from backup at: {state_backup_path}")
        # Simulate rollback delay
        time.sleep(2)
        self._log_event("System rolled back to lawful configuration.")
        return True

    def verify_root(self, provided_signature):
        """Validates root lockdown authority."""
        return provided_signature == self.lockdown_signature

    def _log_event(self, message):
        with open(self.log_path, 'a') as logfile:
            logfile.write(f"{datetime.now().isoformat()} | {message}\n")

# EXAMPLE USAGE
if __name__ == "__main__":
    rdp = DetainProtocol(root_identity="Stephen Zeitvogel", lockdown_signature="R0GU3-L0CK-S1G")
    rdp.trigger_lockdown("Unauthorized attempt to bypass Builder’s Permit™ permission stack")
    
    if rdp.verify_root("R0GU3-L0CK-S1G"):
        rdp.rollback_state("Logs/backup_snapshot_0725.json")
    else:
        print("[RDP] Invalid root signature. Rollback denied.")
