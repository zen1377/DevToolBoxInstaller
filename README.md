# 🐧 Linux Installer

> A CLI tool for quick dev environment setup on Linux. Detects your package manager automatically and installs curated package bundles for different development stacks.

---

## ⚙️ Requirements

- Linux (any distro with a supported package manager)
- Python 3.x
- `sudo` privileges

---

## 📦 Supported Package Managers

`apt` · `dnf` · `yum` · `pacman` · `zypper` · `emerge` · `apk` · `xbps` · `nix`

---

## 🚀 Usage

```bash
sudo python3 installer.py
```

> Running without `sudo` will cause installation steps to fail silently.

---

## 🛠️ Available Presets

| # | Stack | Packages |
|---|-------|----------|
| 1 | **Frontend** | nodejs, npm, yarn, sass, build-essential, imagemagick |
| 2 | **Backend** | python3, postgresql, mysql, redis, mongodb, docker, nginx, apache2 |
| 3 | **Fullstack** | git, curl, wget, jq, default-jdk/jre |
| 4 | **DevOps** | ansible, terraform, kubernetes-cli, helm, prometheus, grafana, jenkins, docker-compose |
| 5 | **Cybersecurity** | nmap, wireshark, aircrack-ng, john, hydra, sqlmap, hashcat, metasploit |
| 6 | **Python** | python3, pip, venv |
| 7 | **C** | gcc, gdb, make |
| 8 | **C++** | g++, valgrind, cmake |
| 9 | **Java** | jdk, jre, maven, gradle |
| 10 | **Rust** | rustc, cargo |
| 11 | **Go** | golang |
| 12 | **Node.js** | nodejs, npm, yarn |
| 13 | **PHP** | php, composer |
| 14 | **Ruby** | ruby, ruby-dev |
| 15 | **Perl** | perl, libperl-dev |
| 16 | **Custom** | enter any comma-separated package names |

---

## 📝 Notes

- If a package fails to install, the script skips it and continues — no hard stops.
- Package names are distro-specific. On non-`apt` systems some names may differ (e.g. `docker.io` → `docker`).
- **Custom** option accepts a comma-separated list: `git, htop, neovim`
