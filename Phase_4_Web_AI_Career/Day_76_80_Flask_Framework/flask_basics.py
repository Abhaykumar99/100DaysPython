# ============================================================
# Day 76-80: Flask Web Framework — Routes, Templates & Static Files
# ============================================================
# pip install flask
# Run: python flask_basics.py
# Then visit: http://127.0.0.1:5000
# ============================================================

from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# ============================================================
# ROUTES
# ============================================================

@app.route("/")
def home():
    return render_template_string(HOME_HTML, title="Home")

@app.route("/about")
def about():
    return render_template_string(ABOUT_HTML, title="About")

@app.route("/user/<username>")
def user_profile(username):
    return f"<h2>👤 Profile: {username}</h2>"

@app.route("/greet")
def greet():
    name = request.args.get("name", "Guest")   # ?name=Alice
    return f"<h2>Hello, {name}! 👋</h2>"

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name")
        message = request.form.get("message")
        return f"<h2>✅ Thanks {name}! Message received.</h2>"
    return render_template_string(CONTACT_HTML)

# ============================================================
# SIMPLE HTML TEMPLATES (inline — in real projects use /templates)
# ============================================================

HOME_HTML = """
<!DOCTYPE html><html><head><title>{{ title }}</title>
<style>body{font-family:Arial,sans-serif;max-width:800px;margin:50px auto;padding:20px}
nav a{margin-right:15px;text-decoration:none;color:#4a90d9}</style></head>
<body>
<nav><a href="/">Home</a><a href="/about">About</a><a href="/contact">Contact</a></nav>
<h1>🐍 Flask App — Day 76-80</h1>
<p>Welcome to your first Flask web app!</p>
<p>Try: <a href="/greet?name=Alice">/greet?name=Alice</a></p>
</body></html>"""

ABOUT_HTML = """
<!DOCTYPE html><html><body>
<h1>About This App</h1>
<p>Built with Flask as part of 100 Days of Python (Day 76-80).</p>
<a href="/">← Back Home</a>
</body></html>"""

CONTACT_HTML = """
<!DOCTYPE html><html><body>
<h1>Contact Us</h1>
<form method="POST">
  Name: <input type="text" name="name"><br><br>
  Message: <textarea name="message"></textarea><br><br>
  <button type="submit">Send</button>
</form>
<a href="/">← Back</a>
</body></html>"""

# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 — Page Not Found 😢</h1><a href='/'>← Go Home</a>", 404

if __name__ == "__main__":
    print("🚀 Flask app starting at http://127.0.0.1:5000")
    app.run(debug=True)

# ============================================================
# FLASK CONCEPTS IN THIS FILE:
# app = Flask(__name__)  → create app
# @app.route("/")        → map URL to function
# request.args           → GET query params
# request.form           → POST form data
# <variable>             → dynamic URL segments
# render_template_string → render HTML with Jinja2
# app.run(debug=True)    → run dev server
# ============================================================
