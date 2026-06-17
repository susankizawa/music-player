# Music Player Desktop System

## Project Description

This project is a desktop music player application with support for:

- Global music library
- Playlist management
- Audio search
- Playback controls
- Metadata reading from audio files

It is built using PySide6 and focuses on applying software architecture, data structures, and GUI development concepts in a practical system.

---

## Requirements

### System Requirements

- Python 3.8 or higher
- Windows PowerShell (for running scripts)

---

### Python Dependencies

This project uses the following libraries:

- **PySide6** – GUI framework (Qt for Python)
- **PySide6_Addons** – Extra Qt components
- **PySide6_Essentials** – Core Qt components
- **shiboken6** – Python bindings for Qt
- **mutagen** – Audio metadata (ID3 tags, etc.)
- **colorama** – Terminal text styling (mainly for debugging/log output)

Install all dependencies with:

```bash
pip install -r requirements.txt
````

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repo-url>
cd <repo-folder>
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

---

### 3. Activate virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

You can start the application using the provided script:

```powershell
.\run.ps1
```

This script will:

* Activate the virtual environment
* Run the application entry point:

```bash
python -m src.main
```

---

## Manual Run (optional)

If you prefer not to use the script:

```powershell
.venv\Scripts\Activate.ps1
python -m src.main
```

---

## Entry Point

The application starts from:

```
src.main
```

---

## Notes

* Always activate the virtual environment before running the project.
* If script execution is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

---

## Project Structure (expected)

```
src/
 ├── main.py   # Application entry point
```

```
