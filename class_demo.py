
# create a Car class
class Car:
    '''Car class'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        '''start car's engine'''
        if not self.is_running:
            print(
                f"The {self.year} {self.make} {self.model}'s engine is now started")
            self.is_running = True
        else:
            print(
                f"The {self.year} {self.make} {self.model}'s engine is already started")

    def stop_engine(self):
        '''stop car engine'''
        if self.is_running:
            print(
                f"The {self.year} {self.make} {self.model}'s engine is now stopped")
            self.is_running = False
        else:
            print(
                f"The {self.year} {self.make} {self.model}'s engine is alread stopped")


my_car = Car("BMW", "X5", 2024)
print(f"{my_car.make}")
my_car.start_engine()
my_car.stop_engine()
