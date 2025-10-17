# Gesture Control

Small Python script that uses MediaPipe + OpenCV to control keyboard inputs via hand gestures.

Features
- Detects number of fingers and maps to left/right key presses using pyautogui.

Prerequisites
- Windows (tested)
- Python 3.8+
- A working webcam

Install
1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

Run

```powershell
python gesture_control.py
```

Note: This script uses pyautogui to emit key events. When running, it will send left/right key presses to whatever application is focused. Give the target application focus (or run a game) to observe behavior. On Windows you may need to grant accessibility/automation permissions.

How to push to GitHub (quick)

Initialize a local repo, commit, and push. Using GitHub CLI (`gh`) is the easiest option:

```powershell
git init; git add .; git commit -m "Initial commit";
gh repo create <your-repo-name> --public --source=. --push
```

If you don't use `gh`, create a repo on GitHub, then add the remote and push:

```powershell
# replace the URL with your repo
git remote add origin https://github.com/<your-user>/<your-repo>.git; git branch -M main; git push -u origin main
```

CI
A simple GitHub Actions workflow is included that installs dependencies and runs a quick syntax check (does not execute the GUI script).

Security
- Be careful with pyautogui: running the script will generate keyboard events. Only run with trusted applications in focus.

License
MIT (see LICENSE file)
