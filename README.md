# Netmiko Network Device Tool (Python)

A command-line tool that connects to Cisco IOS-XE devices over SSH using **Netmiko**, runs commands, captures output, and saves results as **TXT** or **JSON**.

Built as hands-on practice for network automation and reliability roles—specifically working with live network devices using Netmiko.

---

## Why this project?

This tool demonstrates common requirements in Network Reliability / DevOps roles:

- Proficiency with **Netmiko** for SSH-based device interaction  
- Automating command execution and output collection  
- Structured output handling (**TXT/JSON**) for integration with other tooling  
- Robust **logging** and error handling  
- A clean CLI that can be reused in workflows  

---

## Features

- Connects to Cisco DevNet “Always-On” IOS-XE sandbox  
- Executes multiple `show` commands (including enable-mode workflows)  
- Real-time terminal feedback  
- Saves output to timestamped **TXT** or **JSON** files  
- Writes logs:
  - `logs/network_tool.log` (actions + errors)
  - `logs/session_output.txt` (raw SSH session transcript)

---

## Requirements

- Python 3.6+
- Netmiko

Install:

```bash
pip install netmiko
```

---

## Project structure

```text
netmiko_tool/
├── network_tool.py         # Main script
├── logs/                   # Session transcripts and action logs
├── outputs/                # Saved command output (TXT/JSON)
└── README.md
```

---

## Usage

### Basic run (default commands)

```bash
python network_tool.py
```

Runs:
- `show ip interface brief`
- `show version`
- `show clock`

### Custom commands + JSON output

```bash
python network_tool.py \
  --commands "show running-config | include hostname" "show interfaces description" \
  --format json
```

### Help

```bash
python network_tool.py --help
```

---

## Example terminal output

```text
Connecting to sandbox-iosxe-recomm-1.cisco.com...
Running: show ip interface brief
Running: show version
Running: show clock
Disconnected.

Output saved to outputs/device_output_20251220_135101.txt
Check logs/network_tool.log and logs/session_output.txt for full details.
```

---

## Logging & outputs

- `logs/network_tool.log` — timestamped actions and errors  
- `logs/session_output.txt` — complete raw SSH session transcript  
- `outputs/` — timestamped result files (TXT/JSON)

---

## Future extensions

- Structured parsing with **TextFSM / NTC-Templates**
- Support multiple devices from an inventory file
- Integrate with **Nautobot/NetBox** as a source of truth
- Config backup + comparison
- Push safe config changes (with confirmation)

---

## Maintainer

Maintained by **Rebecca Clarke**  
Part of the **Network Automation Tools** organization.
