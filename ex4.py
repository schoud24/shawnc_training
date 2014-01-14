# First section of code creates the variables with fixed inputs
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# Cars not driven is comparing the number of cars available and the number of 
# drivers available, and figuring out what the excess number of cars is
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

