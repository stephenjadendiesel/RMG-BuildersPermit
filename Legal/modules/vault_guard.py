# vault_guard.py
# Builder’s Permit™ - Vault Guard Integrity Module
# Copyright (c) 2025 Stephen Zeitvogel. All rights reserved.

import os
import hashlib
from datetime import datetime

class VaultGuard:
    def __init__(self, monitored_paths, root_signature):
        self.monitored_paths = monitored_paths
        self.root_signature = root_signature
        self.snapshot = {}
        self.log_path = "Logs/vault_guard.log"

    def scan_files(self):
        """Scans and hashes critical files for state integrity."""
        current_snapshot = {}
        for path in self.monitored_paths:
            if os.path.exists(path):
                with open(path, 'rb') as f:
                    content = f.read()
                    file_hash = hashlib.sha256(content).hexdigest()
                    current_snapshot[path] = file_hash
        return current_snapshot

    def detect_changes(self, new_snapshot):
        """Detects tampering or unauthorized file changes."""
        tampered_files = []
        for path, hash_val in new_snapshot.items():
            old_hash = self.snapshot.get(path)
            if old_hash and old_hash != hash_val:
                tampered_files.append(path)
        return tampered_files

    def authorize(self, signature):
        """Checks if the root authority is present."""
        return signature == self.root_signature

    def log_event(self, message):
        with open(self.log_path, 'a') as log:
            log.write(f"{datetime.now().isoformat()} | {message}\n")

    def activate_guard(self, signature):
        if not self.authorize(signature):
            self.log_event("Unauthorized attempt to activate Vault Guard.")
            print("[VaultGuard] Root signature verification failed.")
            return False

        new_snapshot = self.scan_files()
        tampered = self.detect_changes(new_snapshot)

        if tampered:
            self.log_event(f"Tampered files detected: {tampered}")
            print("[VaultGuard] ALERT: File tampering detected.")
        else:
            self.log_event("System integrity check passed.")
            print("[VaultGuard] All monitored files are intact.")

        self.snapshot = new_snapshot
        return True


# Example usage
if __name__ == "__main__":
    guard = VaultGuard(
        monitored_paths=[
            "permit_engine.py",
            "surveyor.py",
            "detain_protocol.py",
            "README.md"
        ],
        root_signature="R0GU3-L0CK-S1G"
    )
    guard.activate_guard("R0GU3-L0CK-S1G")
