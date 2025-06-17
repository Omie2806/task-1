import os

forb_words = ["print", "eval", "exec"]

def detect_violations(file_path):
    violations = 0
    not_allowed = False

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:  # Iterate over each line
            if len(line.strip()) > 80:  # Check for long lines
                violations += 1

            if line.count('"') % 2 == 1 or line.count("'") % 2 == 1:  # Unclosed string check
                violations += 1

            if not line.lstrip().startswith("#"):  # Ignore comments
                for keyword in forb_words:
                    if keyword in line:
                        violations += 1
                        not_allowed = True

    # Risk classification per file
    if violations > 5 or not_allowed:
        print(f"{file_path}: HIGH RISK")
    elif violations >= 1:
        print(f"{file_path}: LOW RISK")
    else:
        print(f"{file_path}: CLEAN")

def scan_codebase(directory):
    for root, _, files in os.walk(directory):  # Walk through all directories
        for file in files:
            if file.endswith(".py"):
                detect_violations(os.path.join(root, file))  # Pass file path to detect_violations()

if __name__ == "__main__":
    scan_codebase(".")
