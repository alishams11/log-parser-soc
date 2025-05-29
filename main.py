from parser.authlog_parser import parse_authlog
import csv

def save_to_csv(data, filename='output/brute_force.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ip', 'line']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)

if __name__ == "__main__":
    filepath = input("Enter path to auth.log file: ")
    results = parse_authlog(filepath)
    save_to_csv(results)
    print(f"Done! {len(results)} suspicious entries saved.")
