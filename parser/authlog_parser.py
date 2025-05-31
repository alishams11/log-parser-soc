import json
import re

def parse_authlog(file_path):
    failed_attempts = []
    with open(file_path, 'r') as log:
        for line in log:
            if "Failed password" in line:
                match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
                if match:
                    ip = match.group(1)
                    failed_attempts.append({"ip": ip, "line": line.strip()})
    return failed_attempts

def save_to_json(data, filename='output/brute_force.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
