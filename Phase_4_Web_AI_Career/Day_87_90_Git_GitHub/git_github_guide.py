# ============================================================
# Day 87-90: Git & GitHub — Commands Reference & Workflow Guide
# ============================================================

"""
GIT & GITHUB COMPLETE GUIDE
============================

⚙️ SETUP
----------
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global core.editor "code --wait"

📁 CREATING A REPOSITORY
--------------------------
git init                          # Initialize new local repo
git clone <url>                   # Clone from GitHub

📸 BASIC WORKFLOW (Daily)
--------------------------
git status                        # Check what's changed
git add filename.py               # Stage specific file
git add .                         # Stage ALL changes
git commit -m "Your message"      # Commit with message
git push origin main              # Push to GitHub

📥 PULLING UPDATES
-------------------
git pull                          # Fetch + merge from remote
git fetch                         # Fetch only (don't merge)

🌿 BRANCHING
--------------
git branch                        # List branches
git branch feature-login          # Create new branch
git checkout feature-login        # Switch to branch
git checkout -b feature-login     # Create AND switch (shortcut)
git switch main                   # Newer way to switch

🔀 MERGING
-----------
git merge feature-login           # Merge into current branch
git merge --no-ff feature-login   # Merge with merge commit
git branch -d feature-login       # Delete merged branch

🔀 PULL REQUESTS (GitHub workflow)
------------------------------------
1. Create branch: git checkout -b feature/my-feature
2. Make changes & commit
3. Push:  git push origin feature/my-feature
4. On GitHub: "Compare & pull request"
5. Review, approve, merge
6. Delete branch on GitHub
7. git pull to update local main

📜 VIEWING HISTORY
-------------------
git log                           # Full history
git log --oneline                 # Compact view
git log --oneline --graph         # Visual graph
git diff                          # Unstaged changes
git diff --cached                 # Staged changes
git show <commit-hash>            # Show specific commit

⏪ UNDOING CHANGES
-------------------
git restore filename.py           # Discard unstaged changes
git restore --staged filename.py  # Unstage a file
git revert <commit-hash>          # Undo commit (safe, creates new commit)
git reset --hard <commit-hash>    # Go back to commit (DESTRUCTIVE!)

🔖 TAGGING (Releases)
-----------------------
git tag v1.0.0                    # Lightweight tag
git tag -a v1.0.0 -m "Release"   # Annotated tag
git push origin v1.0.0            # Push tag to GitHub

🙈 .GITIGNORE
--------------
# Create .gitignore file with patterns to ignore:
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
node_modules/

🔑 BEST PRACTICES
------------------
✅ Commit often with clear messages
✅ Use branches for features and bug fixes
✅ Never commit secrets (API keys, passwords)
✅ Write meaningful commit messages (imperative mood):
   "Add login functionality"  (NOT "added stuff")
✅ Pull before starting work each day
✅ Use .gitignore from the start
✅ Tag releases with semantic versioning (v1.0.0)

📝 COMMIT MESSAGE CONVENTION (Conventional Commits):
----------------------------------------------------
feat: add user authentication
fix: resolve login redirect bug
docs: update README with setup steps
style: format code with black
refactor: extract helper functions
test: add unit tests for auth module
chore: update dependencies
"""

print("📖 Git & GitHub Guide loaded!")
print("This file contains the complete Git reference for Day 87-90.")
print("Read the docstring above for all commands and concepts.")
