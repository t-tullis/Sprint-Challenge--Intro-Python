# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
class Vehicle():
    #base class
    pass

class FlightVehicle(Vehicle):
    pass

class Starship(FlightVehicle):
    pass

# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
class GroundVehicle(Vehicle):
    pass

class Airplane(FlightVehicle):
    pass
# [Car]  [Motorcycle]
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
