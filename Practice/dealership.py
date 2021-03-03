class BMW(object):
    def __init__(self, model):
        self.model = model
        self.colors = ["Blue", "Black", "White"]
        self.models = ["i8", "z4", "330i", "520-D", "760li"]
        self.speeds = ["320", "260", "270", "260", "250"]
        self.prices = ["2,14,00,000", "50,00,000", "35,00,000", "42,00,000", "54,00,000"]

    def get_colors(self):
        return self.colors
    
    def get_models(self):
        return self.models
    
    def get_speed(self):
        for x in range(len(self.speeds)):
            if self.models[x] == self.model:
                return self.speeds[x]

    def get_price(self):
        for x in range(len(self.prices)):
            if self.models[x] == self.model:
                return self.prices[x]

class RollsRoyce(object):
    def __init__(self, model):
        self.model = model
        self.colors = ["Silver", "Gold", "White"]
        self.models = ["Ghost", "Phantom", "Cullinan"]
        self.speeds = ["250", "250", "250"]
        self.prices = ["8,00,00,000", "10,00,00,000", "7,00,00,000"]

    def get_colors(self):
        return self.colors
    
    def get_models(self):
        return self.models
    
    def get_speed(self):
        for x in range(len(self.speeds)):
            if self.models[x] == self.model:
                return self.speeds[x]

    def get_price(self):
        for x in range(len(self.prices)):
            if self.models[x] == self.model:
                return self.prices[x]

class Lamborghini(object):
    def __init__(self, model):
        self.model = model
        self.colors = ["Yellow", "Lime", "Black", "White", "Orange"]
        self.models = ["Urus", "Aventador", "Huracan"]
        self.speeds = ["250", "250", "250"]
        self.prices = ["3,10,00,000", "6,00,00,000", "4,10,00,000"]

    def get_colors(self):
        return self.colors
    
    def get_models(self):
        return self.models
    
    def get_speed(self):
        for x in range(len(self.speeds)):
            if self.models[x] == self.model:
                return self.speeds[x]

    def get_price(self):
        for x in range(len(self.prices)):
            if self.models[x] == self.model:
                return self.prices[x]

print("========================= Welcome to the Luxury Car Dealership =========================\n")
companyInput = input("Enter car company (BMW / RollsRoyce / Lamborghini): ")

if companyInput == "BMW":
    company = BMW(input("Enter Model (i8, z4, 330i, 520-D, 760li): "))
    
elif companyInput == "RollsRoyce":
    company = RollsRoyce(input("Enter Model (Ghost, Phantom, Cullinan): "))

elif companyInput == "Lamborghini":
    company = Lamborghini(input("Enter Model (Urus, Aventador, Huracan): "))

try:
    print("\nColors: " + str(company.get_colors())[1:-1].replace("\'", ""))
    print("Speed: " + str(company.get_speed()) + " km/h")
    print("Price: ₹" + str(company.get_price()))

except Exception:
    print("\nInvalid Option!")
