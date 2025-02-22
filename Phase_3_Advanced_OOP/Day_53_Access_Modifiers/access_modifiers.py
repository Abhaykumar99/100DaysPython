# ============================================================
# Day 53: Access Modifiers — Public, Protected, Private
# ============================================================
# Public:    name       — accessible everywhere
# Protected: _name      — convention: "for internal use"
# Private:   __name     — name-mangled, restricted access
# ============================================================

class Employee:
    def __init__(self, name, salary, ssn):
        self.name    = name         # Public    — freely accessible
        self._salary = salary       # Protected — "internal use" hint
        self.__ssn   = ssn          # Private   — name-mangled

    def get_info(self):
        return f"Name: {self.name}, Salary: ₹{self._salary}"

    def get_ssn(self):             # Controlled access to private
        return f"SSN: ***-**-{self.__ssn[-4:]}"

    def _calculate_bonus(self):    # Protected method
        return self._salary * 0.10

    def __validate(self):          # Private method
        return len(self.__ssn) == 9

class Manager(Employee):
    def show_bonus(self):
        # Can access protected:
        bonus = self._calculate_bonus()    # ✅ (works but discouraged)
        return f"Bonus: ₹{bonus}"

    # Cannot directly access private:
    # self.__ssn is NOT accessible here → AttributeError

emp = Employee("Alice", 50000, "123456789")
mgr = Manager("Bob", 80000, "987654321")

# Public — accessible everywhere
print(emp.name)
print(emp.get_info())
print(emp.get_ssn())

# Protected — accessible but convention says don't
print(emp._salary)         # Works (but bad practice outside class)

# Private — name mangled to _ClassName__attribute
try:
    print(emp.__ssn)        # AttributeError!
except AttributeError:
    print("❌ __ssn is private, can't access directly!")

# Workaround via name mangling (not recommended):
print(emp._Employee__ssn)  # Works but VERY bad practice

print(f"\n{mgr.get_info()}")
print(mgr.show_bonus())
