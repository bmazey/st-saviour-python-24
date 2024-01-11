class Car:
    def _int_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def _str_(self):
        return f"{self.year} {self.make} {self.model}"
    