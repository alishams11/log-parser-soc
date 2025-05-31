from parser.authlog_parser import parse_authlog, save_to_json
import csv
import os

def save_to_csv(data, filename='output/brute_force.csv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ip', 'line']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

if __name__ == "__main__":
    filepath = input("Enter path to auth.log file: ").strip()
    
    if not os.path.exists(filepath):
        print("[!] File not found. Check the path.")
        exit(1)

    results = parse_authlog(filepath)
    
    print(f"[+] Found {len(results)} suspicious entries.")
    save_to_csv(results)
    save_to_json(results)
    print("[+] Output saved to output/brute_force.csv and .json")
