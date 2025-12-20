from netmiko import ConnectHandler
import logging
import json
from datetime import datetime
import argparse
import os

from netmiko import ConnectHandler

devbox = {
    "device_type": "linux",
    "host": "10.10.20.50",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
    "session_log": "logs/session_output.txt",
    "conn_timeout": 20,
    "banner_timeout": 30,
    "auth_timeout": 20,
}

# Setup directories and logging
os.makedirs('logs', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

logging.basicConfig(
    filename='logs/network_tool.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Cisco DevNet Always-On Sandbox (public, read-only access)
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.50',  # e.g., '10.10.20.48'
    'username': 'rclarke0',  # May need to change - check Lab Portal
    'password': '6z2WEb%yA$3L',  # May need to change - check Lab Portal
    'port': 22,  # SSH port (default is 22)
    'session_log': 'logs/session_output.txt',
}


def run_commands(commands):
    print("VPN required for live connection—using mock output for demo")
    mock_outputs = {
        'show ip interface brief': "Interface              IP-Address      OK? Method Status                Protocol\nGigabitEthernet1       10.10.20.50     YES manual up                    up      \n...",
        'show version': "Cisco IOS XE Software, Version 17.09.01...\nHostname: cat8k-...",
        'show clock': "*13:51:01.570 UTC Sat Dec 20 2025"
    }
    results = {cmd: mock_outputs.get(cmd, f"Mock output for {cmd}") for cmd in commands}
    return results
    
def save_output(results, format='txt'):
    """Save command output to file (TXT or JSON)."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    if format == 'json':
        filename = f"outputs/device_output_{timestamp}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
    
    else:
        filename = f"outputs/device_output_{timestamp}.txt"
        with open(filename, 'w') as f:
            for cmd, output in results.items():
                f.write(f"\n=== {cmd} ===\n{output}\n\n")
    
    print(f"Output saved to {filename}")
    logging.info(f"Results saved to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Netmiko Network Device Automation Tool")
    parser.add_argument('--commands', nargs='+', 
                        default=['show ip interface brief', 'show version', 'show clock'],
                        help="Commands to run on the device")
    parser.add_argument('--format', choices=['txt', 'json'], default='txt',
                        help="Output format: txt (default) or json")
    
    args = parser.parse_args()
    
    try:
        output = run_commands(args.commands)
        
        # Print to terminal
        print("\n" + "="*60)
        for cmd, out in output.items():
            print(f"\n=== {cmd} ===\n{out}")
        print("="*60 + "\n")
        
        save_output(output, args.format)
        print("Check logs/network_tool.log and logs/session_output.txt for full details.")
    
    except Exception:
        print("Script failed. See logs/network_tool.log for details.")