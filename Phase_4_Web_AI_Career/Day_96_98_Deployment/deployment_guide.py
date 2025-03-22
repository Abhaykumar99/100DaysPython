# ============================================================
# Day 96-98: Deployment — Host Flask App on Render / PythonAnywhere
# ============================================================

"""
=============================================================
DEPLOYMENT GUIDE — Flask App
=============================================================

OPTION A: PythonAnywhere (Easiest for beginners — FREE tier)
-------------------------------------------------------------
1. Sign up at: https://www.pythonanywhere.com (free account)
2. Go to "Web" tab → Add a new web app
3. Select Flask, choose Python 3.11
4. Upload your Flask files via Files tab or Git
5. Set WSGI config:

   WSGI file (auto-generated) should have:
   from yourapp import app as application

6. Reload web app → Done! Your URL: yourusername.pythonanywhere.com

OPTION B: Render (Modern, free tier, CI/CD)
--------------------------------------------
1. Sign up at: https://render.com
2. Push your Flask project to GitHub
3. On Render → New → Web Service → Connect GitHub repo
4. Config:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn app:app
5. Add environment variables in Render dashboard
6. Deploy → URL: your-app.onrender.com

=============================================================
REQUIRED FILES FOR DEPLOYMENT
=============================================================
"""

# requirements.txt content (create this file in your project root):
REQUIREMENTS = """flask==3.0.0
flask-sqlalchemy==3.1.1
gunicorn==21.2.0
python-dotenv==1.0.0
requests==2.31.0
"""

# Procfile (for Render/Heroku):
PROCFILE = "web: gunicorn app:app"

# .env file (DO NOT commit to Git!):
ENV_EXAMPLE = """
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///app.db
DEBUG=False
"""

# gunicorn_config.py:
GUNICORN_CONFIG = """
bind = "0.0.0.0:8000"
workers = 4
worker_class = "sync"
timeout = 120
"""

import os

def create_deployment_files(project_dir="."):
    """Create standard deployment files for a Flask project."""
    files = {
        "requirements.txt": REQUIREMENTS,
        "Procfile"        : PROCFILE,
        ".env.example"    : ENV_EXAMPLE.strip(),
        "gunicorn_config.py": GUNICORN_CONFIG.strip(),
    }

    for filename, content in files.items():
        path = os.path.join(project_dir, filename)
        with open(path, "w") as f:
            f.write(content)
        print(f"✅ Created: {filename}")

    # Create .gitignore
    gitignore_content = "venv/\n__pycache__/\n*.pyc\n.env\n*.db\n.DS_Store\n"
    with open(os.path.join(project_dir, ".gitignore"), "w") as f:
        f.write(gitignore_content)
    print("✅ Created: .gitignore")

    print("\n🚀 Deployment files ready!")
    print("Next steps:")
    print("  1. git init && git add . && git commit -m 'initial commit'")
    print("  2. Push to GitHub")
    print("  3. Connect to Render or PythonAnywhere")


if __name__ == "__main__":
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        create_deployment_files(tmpdir)
        print(f"\nFiles created in temp dir: {os.listdir(tmpdir)}")

print("\nDeployment Guide printed above. Follow the steps in the docstring!")
