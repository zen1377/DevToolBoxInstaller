import subprocess

ascii_art = """
 _     _                    ___           _        _ _           
| |   (_)_ __  _   ___  __ |_ _|_ __  ___| |_ __ _| | | ___ _ __ 
| |   | | '_ \| | | \ \/ /  | || '_ \/ __| __/ _` | | |/ _ \ '__|
| |___| | | | | |_| |>  <   | || | | \__ \ || (_| | | |  __/ |   
|_____|_|_| |_|\__,_/_/\_\ |___|_| |_|___/\__\__,_|_|_|\___|_|   
powered by @zen1377 (i lost access to old acount, where I post this script before)
"""

def detect_package_manager():
    package_managers = {
        "apt": "dpkg-query --version",
        "dnf": "dnf --version",
        "yum": "yum --version",
        "pacman": "pacman --version",
        "zypper": "zypper --version",
        "emerge": "emerge --version",
        "apk": "apk --version",
        "xbps": "xbps-query --version",
        "nix": "nix --version",
    }

    for manager, cmd in package_managers.items():
        try:
            subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return manager
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    return "No package manager detected"

def required_app():
    Frontend = ["nodejs", "npm", "yarn", "sass", "build-essential", "imagemagick"]
    Backend = ["python3", "python3-pip", "postgresql", "mysql-server", "redis", "mongodb", "docker.io", "nginx", "apache2"]
    Fullstack = ["git", "curl", "wget", "jq", "default-jdk", "default-jre"]
    DevOps = ["ansible", "terraform", "kubernetes-cli", "helm", "prometheus", "grafana", "jenkins", "docker-compose"]
    Cybersecurity = ["nmap", "wireshark", "aircrack-ng", "john", "hydra", "sqlmap", "hashcat", "metasploit-framework"]
    Python = ["python3", "python3-pip", "python3-venv"]
    C = ["gcc", "gdb", "make"]
    Cpp = ["g++", "valgrind", "cmake"]
    Java = ["default-jdk", "default-jre", "maven", "gradle"]
    Rust = ["rustc", "cargo"]
    Go = ["golang"]
    Node_js = ["nodejs", "npm", "yarn"]
    PHP = ["php", "composer"]
    Ruby = ["ruby", "ruby-dev"]
    Perl = ["perl", "libperl-dev"]

    print("""Here all of ready setups for development choose that one, that you need:
    1. Frontend
    2. Backend
    3. Fullstack
    4. DevOps
    5. Cybersecurity
    6. Python
    7. C
    8. C++
    9. Java
    10. Rust
    11. Go
    12. Node.js
    13. PHP
    14. Ruby
    15. Perl
    16. Custom installation
    """)

    setup_num = int(input("Enter the number of the setup you need: "))
    
    if setup_num == 1:
        return Frontend
    elif setup_num == 2:
        return Backend
    elif setup_num == 3:
        return Fullstack
    elif setup_num == 4:
        return DevOps
    elif setup_num == 5:
        return Cybersecurity
    elif setup_num == 6:
        return Python
    elif setup_num == 7:
        return C
    elif setup_num == 8:
        return Cpp
    elif setup_num == 9:
        return Java
    elif setup_num == 10:
        return Rust
    elif setup_num == 11:
        return Go
    elif setup_num == 12:
        return Node_js
    elif setup_num == 13:
        return PHP
    elif setup_num == 14:
        return Ruby
    elif setup_num == 15:
        return Perl
    elif setup_num == 16:
        setup_text = input("Enter the names of the packages you want to install (comma-separated): ")
        return [item.strip() for item in setup_text.split(',')]

def main():
    print(ascii_art)
    print("Please run this script with sudo")
    
    package_manager = detect_package_manager()
    if package_manager == "No package manager detected":
        print("Error: No supported package manager found on your system")
        return
    
    print(f"Detected package manager: {package_manager}")
    
    setup = required_app() 
    
    for app in setup:
        try:
            print(f"Installing {app}")
            subprocess.run(f"sudo {package_manager} install -y {app}", 
                         shell=True, 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error installing {app}: {e}")
            continue

if __name__ == "__main__":
    main()
