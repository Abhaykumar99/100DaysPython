# ============================================================
# Day 55: Instance vs Class Variables
# ============================================================

class Student:
    # CLASS VARIABLE — shared across ALL instances
    school_name = "Python Academy"
    total_students = 0

    def __init__(self, name, grade):
        # INSTANCE VARIABLES — unique to each object
        self.name  = name
        self.grade = grade
        Student.total_students += 1

    def info(self):
        return f"{self.name} | Grade: {self.grade} | School: {Student.school_name}"

s1 = Student("Alice", "A")
s2 = Student("Bob",   "B")
s3 = Student("Charlie", "A")

print(s1.info())
print(s2.info())
print(f"Total students: {Student.total_students}")

# Changing class variable via class (affects ALL instances)
Student.school_name = "Elite Python College"
print(f"\nAfter class var change: {s1.school_name}")
print(f"s2 also changed: {s2.school_name}")

# If you set it on an INSTANCE, it creates a new instance variable!
s3.school_name = "Special School"     # Creates instance var for s3 only
print(f"\ns3.school_name : {s3.school_name}")   # Special School
print(f"s1.school_name : {s1.school_name}")   # Elite Python College (class var)

# --- MUTABLE class variables (common gotcha!) ---
class Team:
    members = []    # DANGER: shared mutable list!
    
    def __init__(self, name):
        self.name = name
    
    def add_member(self, member):
        self.members.append(member)    # Mutates the shared class list!

t1 = Team("Team A")
t2 = Team("Team B")
t1.add_member("Alice")
t2.add_member("Bob")
print(f"\nTeam members (shared!): {Team.members}")  # Both Alice and Bob!

# FIX: Use instance variable for mutable data
class TeamFixed:
    def __init__(self, name):
        self.name    = name
        self.members = []    # Each instance gets its OWN list

t3 = TeamFixed("Team C")
t4 = TeamFixed("Team D")
t3.members.append("Charlie")
t4.members.append("Diana")
print(f"t3: {t3.members}, t4: {t4.members}")   # separate!
