
### Step 1: Create the environment

Type this in the terminal:

**Windows**
```
python -m venv .venv
```

**macOS / Linux**
```
python3 -m venv .venv
```

Reading it piece by piece:

- `python -m venv` means "run Python's built-in `venv` module".
- `.venv` is the name of the folder to create. `.venv` is the common convention, and VS Code finds it automatically.

You will see a new `.venv` folder in the Explorer panel. It holds a private copy of Python and an empty place for packages.

### Step 2: Activate it

**Windows (Command Prompt or VS Code's default terminal)**
```
.venv\Scripts\activate
```

**Windows (PowerShell)**
```
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```
source .venv/bin/activate
```

When it works, your prompt starts with `(.venv)`:

```
(.venv) C:\Users\student\pygame_pillow_demo>
```

That `(.venv)` is how you know you are inside the private toolbox.

> **PowerShell error?** If PowerShell says "running scripts is disabled", run this once for the current window and try again:
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
> Or switch the terminal to Command Prompt using the dropdown arrow next to the **+** in the terminal panel.

### Deactivate

When you are finished, type:

```
deactivate
```

The `(.venv)` disappears and you are back to the main Python.

---

## Part 4: Install packages with pip 

Make sure `(.venv)` shows in your prompt, then install:

```
pip install pillow
pip install pygame-ce
```

You can also install both at once: `pip install pillow pygame-ce`.

### Two things that surprise people

1. **The install name and the import name can differ.**

   | Install with | Import with |
   | --- | --- |
   | `pip install pillow` | `from PIL import Image` |
   | `pip install pygame-ce` | `import pygame` |

   Pillow is a modern continuation of an older library called PIL, so the import still says `PIL`. Pygame CE (Community Edition) is a community-maintained version of pygame that you import as plain `pygame`.

2. **Do not install `pygame` and `pygame-ce` together.** They both provide a module called `pygame`, so they overwrite each other and cause confusing errors. If you have the original, remove it first:

   ```
   pip uninstall pygame
   pip install pygame-ce
   ```

### Check what is installed

```
pip list
```

Inside the venv this shows only a few things: `pip`, `pillow` and `pygame-ce`. That short list is the point of a venv: nothing else from your computer is mixed in.

To see details about one package:

```
pip show pygame-ce
```

---

## Part 5: Tell VS Code to use the venv 

Activating in the terminal only changes the terminal. VS Code also needs to know which Python to use for running files, showing errors and giving suggestions. This is called selecting the **interpreter**.

1. Press `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`) to open the Command Palette.
2. Type **Python: Select Interpreter** and press Enter.
3. Choose the one that mentions `.venv`, for example `Python 3.12.x ('.venv')`.

Look at the **bottom-right corner** of VS Code. It now shows the interpreter's name with `.venv`. That is your check that it worked.

### Shortcut: let VS Code make it for you

The Command Palette also has **Python: Create Environment**. Choose `Venv`, pick a Python version, and VS Code builds `.venv` for you. It can also install packages from a `requirements.txt` if one exists. The manual way is worth learning first, because it shows what the shortcut does.

``