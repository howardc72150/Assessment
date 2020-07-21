# Component 3

# Asks the user which unit they want to use
# either kilometer(s), km, meter(s), m, centimeter(s), cm, millimeter(s) or mm.

# Initialize variables
accepted_units = "kilometers", "kilometer", "km", "meters", "meter", "m", "centimeters", "centimeter", "cm", "millimeters", "millimeter", "mm"
units = "kilometer(s), km, meter(s), m, centimeter(s), cm, millimeter(s) or mm"


# Check if user input is a valid unit   .
def check_unit(response):
    error = "Please enter either {}".format(units)
    valid = False
    while not valid:
        response = input(response)
        has_errors = ""
        if response.lower() not in accepted_units:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


# Prints the list of available units.
print("Available units: {}".format(units))
print("")

# Asks the user for which shape they want to use.
unit = check_unit("Which unit would you like to use? ")
print("You selected {}!".format(unit.lower()))