import os
violations = 0
forb_words = ["print", "eval", "exec"]
not_allowed = False
with open(file_path) as files:
    data_line = files.readlines()
    for lines in data_line:
        if len(lines.strip()) > 80:
            violations += 1

        if lines.count('"') % 2 == 1 or lines.count("'") % 2 == 1:
            violations += 1

        if not lines.lstrip().startswith("#"):
            for keyword in forb_words:
                if lines.find(keyword) != -1:
                    violations += 1
                    not_allowed = True

if violations > 5 or not_allowed == True:
    print("HIGH RISK")
elif violations >= 1:
    print("LOW RISK")
else:
    print("clean")
    
def scan_codebase(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                detect_violations(os.path.join(root, file))

if __name__ == "__main__":
    scan_codebase(".")
