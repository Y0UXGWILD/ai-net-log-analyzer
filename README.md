# 🩺 NetAI-Log-Analyzer: Self-Healing Network Monitor

**NetAI-Log-Analyzer** is an event-driven automation tool designed to bridge the gap between "detecting" a network failure and "fixing" it. Built for high-stakes environments like banking data centers, this Python-based NMS (Network Management System) scans device syslogs for critical errors and provides an automated remediation path.

---

## 🚀 Key Features

* **Heuristic Log Analysis:** Uses pattern matching to identify critical `%LINEPROTO-5-UPDOWN` events and interface flaps.
* **Self-Healing (Auto-Remediation):** Automatically executes "bounce" commands (`shutdown` / `no shutdown`) to restore service to failed ports.
* **🛡️ Industry-Standard Dry Run:** Features a "Safe Mode" where the script suggests fixes and waits for engineer confirmation before touching production gear.
* **📜 Audit Logging:** Maintains a persistent `remediation_history.log` file, recording every detection, decision, and execution for regulatory compliance.
* **Multi-Vendor Architecture:** Built on the Netmiko library, making it compatible with Cisco, Juniper, and HP infrastructure.

---

## 🛠️ Technical Stack

* **Language:** Python 3.10+
* **Library:** [Netmiko](https://github.com/ktbyers/netmiko) for Multi-vendor SSH management.
* **Logging:** Python Standard `logging` library for enterprise-grade audit trails.

---

## 📦 Project Structure

```text
NetAI-Log-Analyzer/
├── analyzer.py                # Core AI Logic and Remediation engine
├── requirements.txt           # Dependency list
├── .gitignore                 # Security & Credential protection
└── logs/                      # Auto-generated audit trail (Local only)