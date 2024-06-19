# taxi_simulation.py
class Taxi:
    def __init__(self, taxi_id, location):
        self.taxi_id = taxi_id
        self.location = location
        self.passenger = None

    def assign_passenger(self, passenger):
        self.passenger = passenger

    def move_to(self, new_location):
        self.location = new_location
        if self.passenger:
            self.passenger.location = new_location

class Passenger:
    def __init__(self, passenger_id, location, destination):
        self.passenger_id = passenger_id
        self.location = location
        self.destination = destination
