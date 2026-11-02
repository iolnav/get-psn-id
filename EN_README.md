# 🎮 PSN AccountID Tool (Retrieve & Convert PSN Account IDs)

A bilingual (Vietnamese / English) Python tool that:
1. **Retrieves your PSN-ID** (Base64 encoded) from your PlayStation Network account and **automatically converts it into AccountID HEX** (`0x...`).
2. **Converts PSN-ID → AccountID HEX** standalone for users who already have their PSN-ID.
3. **Saves & views retrieved credentials:** Automatically saves your credentials to `data.json` (timestamp, PSN-ID Base64, AccountID HEX) so you can review them anytime without re-authenticating.

Designed for PS4/PS5 homebrew and Offline Account Activation.

> Based on the original script by **[grill2010](https://github.com/grill2010)** and the **CyberChef** endianness-swapping recipe.

---

## ✨ Features

- 🌐 **Bilingual Support:** Switch between Vietnamese and English right at startup.
- ⚡ **Automatic Conversion:** After retrieving the PSN-ID, it is automatically converted into the 16-character `AccountID HEX` format (prefixed with `0x`) with no extra prompt required.
- 💾 **Auto-Save to data.json:** Automatically stores retrieval timestamp, PSN-ID (Base64), and AccountID HEX in `data.json` alongside the script.
- 📂 **View Saved PSN-ID (Option 3):** Easily view previously saved credentials without logging into PSN again.
- 🔄 **Quick Standalone Converter:** Input an existing Base64 PSN-ID to get the AccountID HEX output instantly.
- 🧭 **Intuitive Navigation:** Type `b` at any input prompt to return to the main menu, or `q` to exit.
- 💬 **Context-Aware Farewell Messages:** Exit messages adapt automatically to your selected language.

---

## 📋 Prerequisites

- Python **3.6** or higher
- The `requests` Python library
- An active Internet connection and a valid PSN account (for Option 1)

---

## 🚀 Virtual Environment (venv) Setup & Run Guide

> ⚠️ **Using a Virtual Environment (venv) is strongly recommended** to prevent package-manager restrictions (such as PEP 668 on macOS Homebrew, Debian, or Ubuntu).

---

### 🍎 macOS

> If Python was installed via Homebrew, system-wide `pip install` is blocked. Set up a venv as follows:

**Step 1 — Open Terminal and navigate to the extracted script directory:**

```bash
cd /path/to/extracted-script-folder
# Example: cd ~/Downloads/lay-tai-khoan-psn-id
```

**Step 2 — Create and activate the venv:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> 💡 **External Drive Note (exFAT/FAT32):** If your folder is stored on an external USB/drive formatted with exFAT or FAT32 (which lacks symlink support), create the venv in your home directory instead:
> ```bash
> python3 -m venv ~/psn-venv
> source ~/psn-venv/bin/activate
> cd /path/to/extracted-script-folder
> ```

**Step 3 — Install dependencies:**

```bash
python3 -m pip install requests
```

**Step 4 — Run the tool:**

```bash
python3 lay-tai-khoan-psn-id.py
```

**Next time, simply run:**

```bash
cd /path/to/extracted-script-folder
source .venv/bin/activate  # (or source ~/psn-venv/bin/activate)
python3 lay-tai-khoan-psn-id.py
```

When finished, type `deactivate` to exit the virtual environment.

---

### 🪟 Windows

**Step 1 — Open Command Prompt or PowerShell**, and navigate to the project folder:

```cmd
cd C:\path\to\extracted-script-folder
:: Example: cd %USERPROFILE%\Downloads\lay-tai-khoan-psn-id
```

**Step 2 — Create and activate the venv:**

```cmd
python -m venv .venv
.venv\Scripts\activate
```

> 💡 If PowerShell shows an error stating *“execution of scripts is disabled on this system”*, open PowerShell as Administrator and run:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**Step 3 — Install dependencies:**

```cmd
python -m pip install requests
```

*(On Windows, if requests is not installed, the tool will also offer to install it automatically for you).*

**Step 4 — Run the tool:**

```cmd
python lay-tai-khoan-psn-id.py
```

**Next time:**

```cmd
cd C:\path\to\extracted-script-folder
.venv\Scripts\activate
python lay-tai-khoan-psn-id.py
```

---

### 🐧 Linux (Ubuntu / Debian)

**Step 1 — Install required packages:**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

**Step 2 — Navigate to the directory, create and activate the venv:**

```bash
cd /path/to/extracted-script-folder
python3 -m venv .venv
source .venv/bin/activate
```

**Step 3 — Install dependencies:**

```bash
python3 -m pip install requests
```

**Step 4 — Run the tool:**

```bash
python3 lay-tai-khoan-psn-id.py
```

---

### 🤖 Android (Termux)

**Step 1 — Install Termux** via [F-Droid](https://f-droid.org/packages/com.termux/) (avoid the outdated Google Play version).

**Step 2 — Install Python and allow storage access:**

```bash
termux-setup-storage
pkg update && pkg upgrade -y
pkg install python -y
```

**Step 3 — Navigate to the script directory, create venv, and install dependencies:**

```bash
cd /path/to/extracted-script-folder
# Or if stored in device storage: cd /storage/emulated/0/Download/lay-tai-khoan-psn-id
# Or Termux home: cd ~/lay-tai-khoan-psn-id

python -m venv .venv
source .venv/bin/activate
pip install requests
```

**Step 4 — Run the tool:**

```bash
python lay-tai-khoan-psn-id.py
```

---

## 📖 Step-by-Step Usage

### 1. Language Selection Screen
Upon launch, select your preferred language:
```text
╔══════════════════════════════════════════╗
║    PSN AccountID Tool  ·  by @iolna      ║
╠══════════════════════════════════════════╣
║   1.  Ngôn ngữ : Tiếng Việt              ║
║   2.  Language : English                 ║
║   q.  Thoát / Exit                       ║
╚══════════════════════════════════════════╝
```
- Press `1` for Vietnamese.
- Press `2` for English.
- Press `q` to exit (displays bilingual farewell message).

---

### 2. Main Menu
Depending on the chosen language, the menu will be displayed:
```text
═══════════════
   MAIN MENU
═══════════════

1. Get PSN-ID (requires logging into the PSN website)
2. Convert PSN-ID → AccountID HEX
3. View retrieved PSN-ID
4. Back
q. Exit
```

#### 👉 Option 1: Get PSN-ID
1. The tool prints an official Sony authorization URL.
2. Copy and open the link in your web browser, then log in to your PSN account.
3. Once logged in, the page redirects to a blank page showing `"redirect"`.
4. Copy the entire URL from the browser's address bar and paste it into the terminal.
5. The tool automatically fetches your account information, extracts the **PSN-ID** (Base64), and immediately converts it to **AccountID HEX**, displaying the result table:
   ```text
   +-------------------+----------------------+
   | PSN-ID (Base64)   | AccountID HEX        |
   +-------------------+----------------------+
   | DVD4MESCAwA=      | 0x0003824430f8500d   |
   +-------------------+----------------------+
   ```
6. The credentials are automatically saved to `data.json` alongside the script:
   ```json
   {
     "timestamp": "2026-11-02 22:00:00",
     "psn_id_base64": "DVD4MESCAwA=",
     "account_id_hex": "0x0003824430f8500d",
     "country_code": "vn",
     "expiration": "2026-11-02T15:56:03.874Z",
     "language_code": "en",
     "online_id": "your_online_id",
     "scopes": "psn:clientapp",
     "user_id": "123456789012345"
   }
   ```
7. Press **Enter** to return to the Main Menu.

#### 👉 Option 2: Convert PSN-ID → AccountID HEX
- For users who already possess their Base64 PSN-ID.
- Paste the string, and the tool will immediately compute and output the result table.
- Type `b` to go back to the Main Menu, or `q` to exit.

#### 👉 Option 3: View retrieved PSN-ID
- Reads and displays stored data from `data.json`, including timestamp, the PSN-ID (Base64) & AccountID HEX table, as well as detailed account info (`online_id`, `user_id`, `country_code`, `language_code`, `expiration`, `scopes`).
- Allows you to inspect your credentials anytime without re-logging in.
- If no data has been saved or `data.json` is missing/corrupted, the tool displays an informative message guiding you to run Option 1 first.

---

## 🔒 Security & Privacy

- The script communicates exclusively with Sony's official servers (`sonyentertainmentnetwork.com`) using HTTPS.
- No third-party servers or relays are involved.
- `data.json` is stored locally only (configured in `.gitignore` so it won't be committed to Git/GitHub).
- Never share sensitive authentication tokens or credentials with others.

---

## 📁 Repository Structure

```text
PSN ID/
├── lay-tai-khoan-psn-id.py    # Main script (bilingual, unified tool)
├── data.json                  # Auto-generated saved credentials file (optional)
├── README.md                  # Vietnamese user guide
└── EN_README.md               # English user guide (this file)
```

---

## 💡 Credits & Acknowledgments

- Credits to the original author **[grill2010](https://github.com/grill2010)** for the initial Remote Play client OAuth workflow.
- Endianness conversion logic: Base64 decode → 8-byte word reverse → Hexadecimal.
- `@iolna built this with AI! Welcome to Bắc Bling City! ;))`
