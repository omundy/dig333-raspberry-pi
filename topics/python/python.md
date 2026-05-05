# Python on Mac — Quick Reference

A recipe-style guide for setting up and using Python on macOS. Each section stands alone — jump to what you need.

---

## Table of Contents

1. [Install Homebrew](#1-install-homebrew)
2. [Install Python via Homebrew](#2-install-python-via-homebrew)
3. [Install uv (package & environment manager)](#3-install-uv)
4. [Check your PATH](#4-check-your-path)
5. [Start a new project](#5-start-a-new-project)
6. [Create a virtual environment](#6-create-a-virtual-environment)
7. [Install packages](#7-install-packages)
8. [Run your code](#8-run-your-code)
9. [Freeze and share dependencies](#9-freeze-and-share-dependencies)
10. [Pick up an existing project](#10-pick-up-an-existing-project)
11. [Manage Python versions](#11-manage-python-versions)
12. [Troubleshooting](#12-troubleshooting)
13. [Run Python on Save in VS Code](#13-run-python-on-save-in-vs-code)

---

## 1. Install Homebrew

Homebrew is the standard package manager for macOS. You need it to install Python and other tools cleanly.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verify it worked:

```bash
brew --version
```

> **Note for Apple Silicon Macs (M1/M2/M3):** Homebrew installs to `/opt/homebrew/`. On older Intel Macs it uses `/usr/local/`. Either way, the commands are the same.

---

## 2. Install Python via Homebrew

macOS ships with its own Python, but you should never use or modify it. Install your own clean copy:

```bash
brew install python
```

Verify:

```bash
python3 --version
```

> **Why not the python.org installer?** Homebrew integrates better with other tools, keeps Python updatable with `brew upgrade`, and won't interfere with system files.

---

## 3. Install uv

`uv` is a modern tool that replaces both `pip` and `virtualenv`. It's dramatically faster and handles package installs, virtual environments, and Python version management all in one.

```bash
brew install uv
```

Verify:

```bash
uv --version
```

---

## 4. Check your PATH

Your shell needs to find Homebrew's tools before anything else. Open `~/.zshrc` in any text editor and make sure this line is present (add it at the top if it's missing):

```bash
export PATH="/opt/homebrew/bin:$PATH"
```

Then reload your shell:

```bash
source ~/.zshrc
```

Confirm Python resolves correctly:

```bash
which python3   # should show /opt/homebrew/bin/python3
which uv        # should show /opt/homebrew/bin/uv
```

> **Tip:** If `python` (without the `3`) still points somewhere unexpected, add this alias to `~/.zshrc`:
> ```bash
> alias python=python3
> ```

---

## 5. Start a New Project

The cleanest way to start is with `uv init`, which creates a project folder with a virtual environment and a `pyproject.toml` (the modern way to track dependencies).

```bash
uv init my-project
cd my-project
```

This creates:

```
my-project/
├── .venv/          ← your virtual environment (don't edit this manually)
├── pyproject.toml  ← your project metadata and dependencies
├── README.md
└── hello.py
```

> **Already have a folder?** Just run `uv init` from inside it.

---

## 6. Create a Virtual Environment

A virtual environment is an isolated copy of Python for your project, so packages installed here don't affect other projects.

> **If you used `uv init`, you already have one.** `uv init` creates the `.venv/` folder automatically — you don't need to run `uv venv` separately. This section only applies if you're setting up a venv in a folder that wasn't created with `uv init`.

```bash
# Only needed if you did NOT use uv init:
uv venv
```

To activate the venv manually (optional with `uv` commands, but required if you want to run `python` directly):

```bash
source .venv/bin/activate
```

Your prompt will change to show `(.venv)` when it's active. To deactivate:

```bash
deactivate
```

> **Why bother?** Without a venv, every project shares the same packages. When project A needs `requests==2.28` and project B needs `requests==2.31`, things break. Venvs keep them separate.

> **Add `.venv/` to your `.gitignore`** — never commit the environment itself, only the file that describes it (`pyproject.toml` or `requirements.txt`).

---

## 7. Install Packages

```bash
# Install one or more packages
uv add requests pandas numpy

# Install a specific version
uv add "flask==3.0.0"

# Remove a package
uv remove requests
```

`uv add` automatically updates `pyproject.toml` so your dependencies are tracked.

**Using a `requirements.txt` instead?**

```bash
uv pip install -r requirements.txt
```

---

## 8. Run Your Code

```bash
# Recommended: uv run handles the venv automatically
uv run python my_script.py

# Or activate the venv first, then run normally
source .venv/bin/activate
python my_script.py
```

> **`uv run` is convenient** because it works even if you haven't manually activated the venv.

---

## 9. Freeze and Share Dependencies

When sharing your project with others (or your future self), you need a way to recreate the same environment.

**With `pyproject.toml` (recommended, created by `uv init`):**

Your dependencies are already tracked automatically. The other person just runs:

```bash
uv sync
```

**With `requirements.txt` (classic approach):**

```bash
# Save your current packages to a file
pip freeze > requirements.txt

# Someone else installs from it
uv pip install -r requirements.txt
```

---

## 10. Pick Up an Existing Project

When you clone or download a project someone else made:

```bash
cd their-project

# If it has a pyproject.toml (uv project):
uv sync

# If it has a requirements.txt:
uv venv
uv pip install -r requirements.txt
```

Then run as normal:

```bash
uv run python main.py
```

---

## 11. Manage Python Versions

Need a specific Python version for a project? `uv` handles that too — no need for `pyenv`.

```bash
# Install a specific Python version
uv python install 3.11

# Create a venv using that version
uv venv --python 3.11

# Check which versions are available locally
uv python list
```

---

## 12. Troubleshooting

**`python` points to the wrong place**

```bash
which python        # see what's being used
which python3
```

Fix: make sure `/opt/homebrew/bin` is first in your PATH (see [Section 4](#4-check-your-path)).

---

**`pip` not found**

Use `pip3` instead, or better yet, switch to `uv add` / `uv pip install` — they work without needing to activate a venv first.

---

**`command not found: uv`**

Either `uv` isn't installed or Homebrew's bin isn't in your PATH.

```bash
brew install uv
source ~/.zshrc
```

---

**Packages installed but Python can't find them**

You probably installed them outside your venv. Make sure you either:
- Ran `uv add` from inside the project folder, or
- Activated the venv with `source .venv/bin/activate` before using `pip install`

---

**Never do these things**

| ❌ Don't | ✅ Do instead |
|---|---|
| `sudo pip install ...` | `uv add ...` inside a venv |
| Install packages globally | Create a venv per project |
| Edit files inside `.venv/` | Reinstall the package |
| Commit `.venv/` to git | Add `.venv/` to `.gitignore` |

---

## 13. Run Python on Save in VS Code

VS Code can automatically run your Python file every time you press `Cmd+S`, using a built-in Task bound to a keyboard shortcut.

### Step 1 — Create a task

Inside your project folder, create `.vscode/tasks.json` (make the `.vscode/` folder if it doesn't exist):

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Run Python on Save",
            "type": "shell",
            "command": "uv run python ${file}",
            "group": "build",
            "presentation": {
                "reveal": "always",
                "panel": "shared",
                "clear": true
            }
        }
    ]
}
```

> **Not using uv?** Replace the `command` with `python3 ${file}` instead.

### Step 2 — Bind it to Cmd+S

Open your keyboard shortcuts file (`Cmd+Shift+P` → "Open Keyboard Shortcuts JSON") and add:

```json
{
    "key": "cmd+s",
    "command": "workbench.action.tasks.runTask",
    "args": "Run Python on Save"
}
```

Now every `Cmd+S` saves the file **and** runs it. Output appears in the integrated terminal (`Cmd+J`). The `"clear": true` setting wipes previous output so you always see a clean result.

> **Note:** This task is per-project (lives in `.vscode/tasks.json`), but the keybinding is global (lives in your user settings). Add `.vscode/` to `.gitignore` if you don't want to commit it.

---

*Generated for macOS (Apple Silicon). Last updated April 2026.*
