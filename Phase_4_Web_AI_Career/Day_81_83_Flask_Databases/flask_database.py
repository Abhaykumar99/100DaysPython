# ============================================================
# Day 81-83: Flask with Databases — SQLite via SQLAlchemy
# ============================================================
# pip install flask flask-sqlalchemy
# ============================================================

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ============================================================
# MODEL (Database Table)
# ============================================================

class Student(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), nullable=False)
    email   = db.Column(db.String(120), unique=True, nullable=False)
    grade   = db.Column(db.String(5))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email, "grade": self.grade}

    def __repr__(self):
        return f"<Student {self.name}>"

# ============================================================
# ROUTES (CRUD Operations)
# ============================================================

@app.route("/students", methods=["GET"])
def get_students():
    """Get all students."""
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Get one student by ID."""
    student = Student.query.get_or_404(student_id)
    return jsonify(student.to_dict())

@app.route("/students", methods=["POST"])
def add_student():
    """Add a new student."""
    data = request.get_json()
    student = Student(name=data["name"], email=data["email"], grade=data.get("grade", "N/A"))
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update a student."""
    student = Student.query.get_or_404(student_id)
    data    = request.get_json()
    student.name  = data.get("name",  student.name)
    student.email = data.get("email", student.email)
    student.grade = data.get("grade", student.grade)
    db.session.commit()
    return jsonify(student.to_dict())

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student."""
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": f"Student {student_id} deleted."})

# ============================================================
# TEST API CALLS (with curl or httpie):
# GET    http://127.0.0.1:5000/students
# POST   http://127.0.0.1:5000/students  -d '{"name":"Alice","email":"a@b.com"}'
# PUT    http://127.0.0.1:5000/students/1 -d '{"grade":"A+"}'
# DELETE http://127.0.0.1:5000/students/1
# ============================================================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        # Seed data
        if not Student.query.first():
            db.session.add_all([
                Student(name="Alice",   email="alice@example.com",   grade="A"),
                Student(name="Bob",     email="bob@example.com",     grade="B+"),
                Student(name="Charlie", email="charlie@example.com", grade="A+"),
            ])
            db.session.commit()
            print("✅ Database seeded!")
    print("🚀 API at http://127.0.0.1:5000/students")
    app.run(debug=True)
