# ============================================================
# Day 35: Virtual Environments — Creating and Managing venv
# ============================================================
# A virtual environment isolates project dependencies.
# ============================================================

"""
VIRTUAL ENVIRONMENT GUIDE
==========================

WHY use virtual environments?
- Each project may need different library versions.
- Prevents "dependency hell" / conflicts between projects.
- Keeps your global Python installation clean.

COMMANDS (run in terminal):
----------------------------

1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:
   Windows:  venv\\Scripts\\activate
   Mac/Linux: source venv/bin/activate

3. Check it's active (you'll see (venv) in terminal prompt)

4. Install packages inside the venv:
   pip install requests
   pip install numpy pandas

5. See installed packages:
   pip list
   pip freeze

6. Save requirements to a file:
   pip freeze > requirements.txt

7. Install from requirements.txt (on another machine):
   pip install -r requirements.txt

8. Deactivate the venv:
   deactivate

9. Delete the venv (just delete the folder):
   rmdir /s venv   (Windows)
   rm -rf venv     (Mac/Linux)

GOOD PRACTICES:
---------------
✅ Always create a venv for each project.
✅ Add 'venv/' to your .gitignore file.
✅ Share requirements.txt, not the venv folder.
✅ Name your venv folder 'venv' or '.venv' by convention.
"""

# --- CHECKING CURRENT ENVIRONMENT IN CODE ---
import sys
print("Python executable:", sys.executable)
print("Python version   :", sys.version)
print("Virtual env      :", sys.prefix)

# Check if in a virtual env
import os
in_venv = hasattr(sys, 'real_prefix') or (
    hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
)
print("In virtual env?  :", in_venv)
