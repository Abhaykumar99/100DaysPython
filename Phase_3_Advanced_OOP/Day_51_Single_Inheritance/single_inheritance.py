# ============================================================
# Day 51: Single Inheritance In-Depth
# ============================================================

class Vehicle:
    """Generic vehicle base class."""

    def __init__(self, make, model, year, fuel_type="petrol"):
        self.make      = make
        self.model     = model
        self.year      = year
        self.fuel_type = fuel_type
        self._odometer = 0

    @property
    def odometer(self):
        return self._odometer

    def drive(self, km):
        if km > 0:
            self._odometer += km
            return f"Drove {km} km. Total: {self._odometer} km."
        return "Distance must be positive."

    def fuel_info(self):
        return f"Fuel type: {self.fuel_type}"

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return f"Vehicle(make='{self.make}', model='{self.model}', year={self.year})"


class ElectricCar(Vehicle):
    """Electric car — inherits from Vehicle."""

    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year, fuel_type="electric")
        self.battery_kwh  = battery_kwh
        self._charge_pct  = 100

    @property
    def charge(self):
        return self._charge_pct

    def charge_battery(self, pct):
        self._charge_pct = min(100, self._charge_pct + pct)
        return f"Battery at {self._charge_pct}%"

    def drive(self, km):
        # Override parent method + extend it
        consumption = km * 0.15        # ~0.15% per km
        if consumption > self._charge_pct:
            return "❌ Not enough charge!"
        self._charge_pct -= consumption
        result = super().drive(km)    # Call parent's drive
        return f"{result} | Charge: {self._charge_pct:.1f}%"

    def fuel_info(self):             # Override parent method
        return f"Battery: {self.battery_kwh} kWh at {self._charge_pct}%"

    def __str__(self):
        return f"{super().__str__()} [EV]"


# Test
tesla = ElectricCar("Tesla", "Model 3", 2023, battery_kwh=82)
print(tesla)
print(tesla.fuel_info())
print(tesla.drive(100))
print(tesla.drive(50))
print(tesla.charge_battery(20))

# Inheritance proof
print(f"\nIs ElectricCar a Vehicle? {isinstance(tesla, Vehicle)}")
print(f"MRO: {[c.__name__ for c in ElectricCar.__mro__]}")
