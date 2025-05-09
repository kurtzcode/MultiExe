#  MultiExe – Bundle Multiple `.exe` Files into One Executable

**MultiExe** is a Python-powered tool that lets you **combine multiple `.exe` programs into a single Windows executable**. Ideal for simplifying software deployment, creating portable app suites, or packaging tools for offline use.

---
<p align="center">
  <img src="https://i.imgur.com/5iKrt9P.png" alt="SpyID Banner" width="600"/>
</p>

## ✨ Features

- 🗂️ Bundle multiple `.exe` files into one launcher
- 🧵 Extracts and runs all apps in parallel from a temporary directory
- 🎨 Supports custom `.ico` icons
- 🧹 Auto-removal of incomplete `.crdownload` files
- 🧪 Clean build system using PyInstaller
- ⚙️ Zero external dependencies required for runtime

## ✅ Requirements

Before running, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)
- [PyInstaller](https://pyinstaller.org/)

---

## 🧰 Installation

Open **Command Prompt** or **PowerShell**, and run:

```bash
# Clone this repository
git clone https://github.com/your-username/MultiExe.git
cd MultiExe

# (Optional but recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows

# Install PyInstaller
pip install pyinstaller

