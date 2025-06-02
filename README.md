# 🔍 log-parser-soc

A simple and effective Python tool to parse system log files (such as `/var/log/auth.log`) and detect suspicious failed SSH login attempts. Designed for SOC analysts, blue teamers, and cybersecurity learners.

---

## 🎯 Features

- ✅ Analyze `auth.log` files to detect failed SSH login attempts
- ✅ Extract IP addresses and relevant log lines
- ✅ Export results to both `CSV` and `JSON` formats
- ✅ Lightweight and CLI-based for easy integration
- ✅ Ideal for monitoring brute-force attacks on Linux servers

---

## 🧠 Skills Demonstrated

- Log analysis
- Regex pattern matching
- Python CLI tool development
- Security event monitoring
- Data export and formatting

---

## 🚀 How to Use

```bash
python3 main.py



#You will be prompted to enter the path to a log file:

Enter path to auth.log file: test_auth.log

#🖥️ Sample Output

[+] Found 6 suspicious entries.
[+] Output saved to output/brute_force.csv and .json

#📁 Project Structure

log-parser-soc/
├── parser/
│   └── authlog_parser.py     # Parsing functions
├── output/
│   ├── brute_force.csv       # CSV export
│   └── brute_force.json      # JSON export
├── main.py                   # CLI tool
├── README.md
├── requirements.txt
└── LICENSE

#📸 Demo Screenshot

    ![demo](screenshots.demo.png)

#⚙️ Installation

pip install -r requirements.txt

    Currently, there are no external dependencies. This file is here for future improvements.


#👨‍💻 Author

Ali Shams

#📝 License

This project is licensed under the MIT License.
