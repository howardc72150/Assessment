# Component 4

# Asks the user for the dimensions of the shape

# Initialize variables

# Manually set the calculation method and shape for testing purposes,
# this would've been set by the user previously.
shape = "square"
calculation_method = "area"


# Check if user input is a number more than zero.
def check_input(question):
    error = "Please enter a number that is more than zero."
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Asks the user for the base of their shape.
x = check_input("Base length: ")
# Asks the user for the height of their shape.
y = check_input("Height length: ")

print("=======================================")
print("Formula for a square is base x height".format(calculation_method.lower()))
print("{:.0f} x {:.0f}".format(x, y))
print("= {:.0f}".format(x * y))
print("=======================================")