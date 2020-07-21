# Assembled program
# Version 3

# Used for pi in some calculations
import math


# Function that prints the instructions of the program
# to the user.
def print_instructions():
    print("==============================================")
    print("                 Instructions")
    print("==============================================")
    print("Enter the shape you are wanting to use then")
    print("enter whether you're calculating the area or")
    print("the perimeter of the shape. Enter the shapes")
    print("      dimensions. Repeat if desired!")
    print("==============================================")
    print("")


def check_response(to_check, response):
    valid = False
    while not valid:
        response = input(response).lower()
        if to_check == "shape":
            if response == "s" or response == "square":
                return "square"
            elif response == "t" or response == "triangle":
                return "triangle"
            elif response == "c" or response == "circle":
                return "circle"
            elif response == "r" or response == "rectangle":
                return "rectangle"
            elif response == "p" or response == "parallelogram":
                return "parallelogram"
            else:
                print("Please enter either square (s), triangle (t), circle (c), rectangle (r) or parallelogram (p).")
        elif to_check == "unit":
            if response == "kilometers" or response == "kilometer" or response == "km":
                return response
            elif response == "meters" or response == "meter" or response == "m":
                return response
            elif response == "centimeters" or response == "centimeter" or response == "cm":
                return response
            elif response == "millimeters" or response == "millimeter" or response == "mm":
                return response
            else:
                print("Please enter either kilometer(s), km, meter(s), m, centimeter(s), cm or millimeter(s)")
        elif to_check == "method":
            if response == "area" or response == "a":
                return "area"
            elif response == "perimeter" or response == "p":
                return "perimeter"
            else:
                print("Please enter either area (a) or perimeter (p)")


# Function that checks if the user input is a valid
# number. If not returns a error.
def number_checker(response):
    error = "Please enter a number that is more than zero."
    valid = False
    while not valid:
        try:
            response = float(input(response))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# Main routine
# Initialize variables
accepted_methods = ["area", "perimeter"]
accepted_shapes = ["square", "triangle", "circle", "rectangle", "parallelogram"]
accepted_units = "kilometers", "kilometer", "km", "meters", "meter", "m", "centimeters", "centimeter", \
                 "cm", "millimeters", "millimeter", "mm"

units = "kilometer(s), km, meter(s), m, centimeter(s), cm, millimeter(s) or mm"
current_calculation = []
calculations = []

neat_calculation = ""
answer = ""

keep_going = ""
print_instructions()

# Loops while program
while keep_going == "":
    # Resets the `current_calculation` variable
    current_calculation = []
    print("Available shapes: square, triangle, circle, rectangle or parallelogram.")

    # Asks user for which shape they want to use.
    shape = check_response("shape", "Which shape would you like to use? ")
    # Adds the shape the `current_calculation` list
    current_calculation.append(shape)
    # Asks user for which unit they want to use.
    unit = check_response("unit", "What is the unit? ")
    # Asks user for the area or perimeter to be calculated.
    method = check_response("method", "Area or perimeter? ")
    # Adds the method the `current_calculation` list
    current_calculation.append(method)

    # Checks what the shape is and figures out how to
    # calculate the area or perimeter of the shape.
    if shape == "square":
        if method == "area":
            length = number_checker("Side Length? ")
            neat_calculation = "{:.0f} x {:.0f}".format(length, length)
            answer = length * length
        elif method == "perimeter":
            length = number_checker("Length? ")
            neat_calculation = "{:.0f} x 4".format(length)
            answer = length * 4
        # Adds the "neat calculation" to the
        # `current_calculation` list
        current_calculation.append(neat_calculation)
    elif shape == "triangle":
        if method == "area":
            base = number_checker("Base? ")
            height = number_checker("Height? ")
            neat_calculation = "1/2 x {:.0f} x {:.0f}".format(base, height)
            answer = 0.5 * base * height
        elif method == "perimeter":
            side_one = number_checker("Side One? ")
            side_two = number_checker("Side Two? ")
            side_three = number_checker("Side Three? ")
            neat_calculation = "{:.0f} + {:.0f} + {:.0f}".format(side_one, side_two, side_three)
            answer = side_one + side_two + side_three
        # Adds the "neat calculation" to the
        # `current_calculation` list
        current_calculation.append(neat_calculation)
    elif shape == "circle":
        if method == "area":
            radius = number_checker("Radius? ")
            neat_calculation = "π{:.0f}^2".format(radius)
            answer = math.pi * radius ** 2
        elif method == "perimeter":
            radius = number_checker("Radius? ")
            neat_calculation = "2π{:.0f}".format(radius)
            answer = 2 * math.pi * radius
        # Adds the "neat calculation" to the
        # `current_calculation` list
        current_calculation.append(neat_calculation)
    elif shape == "rectangle":
        if method == "area":
            length = number_checker("Length? ")
            width = number_checker("Width? ")
            neat_calculation = "{:.0f} x {:.0f}".format(length, width)
            answer = length * width
        elif method == "perimeter":
            side_one = number_checker("Side One? ")
            side_two = number_checker("Side Two? ")
            neat_calculation = "{:.0f} x {:.0f}".format(side_one, side_two)
            answer = side_one * side_two
        # Adds the "neat calculation" to the
        # `current_calculation` list
        current_calculation.append(neat_calculation)
    elif shape == "parallelogram":
        if method == "area":
            length = number_checker("Length? ")
            height = number_checker("Height? ")
            neat_calculation = "{:.0f} x {:.0f}".format(length, height)
            answer = length * height
        elif method == "perimeter":
            length = number_checker("Length? ")
            side = number_checker("Side Length? ")
            neat_calculation = "2({:.0f} + {:.0f})".format(length, side)
            answer = 2*(length + side)
        # Adds the "neat calculation" to the
        # `current_calculation` list
        current_calculation.append(neat_calculation)

    # Adds the answer to the `current_calculation` list
    current_calculation.append(answer)
    # Adds the calculation to the master list
    calculations.append(current_calculation)

    # Checks to see if the unit is logical.
    if 1 >= answer:
        # If the unit is kilometers/km and the answer is
        # less than or equal to 1 will replace the unit
        # with kilometer.
        if unit == "kilometers" or unit == "km":
            unit = "kilometer"
        elif unit == "meters" or unit == "m":
            unit = "meter"
        elif unit == "centimeters" or unit == "cm":
            unit = "centimeter"
        elif unit == "millimeters" or unit == "mm":
            unit = "millimeter"
    else:
        # If the unit is kilometer/km but the answer
        # is greater than 1 it will replace the unit
        # with kilometers.
        if unit == "kilometer" or unit == "km":
            unit = "kilometers"
        elif unit == "meter" or unit == "m":
            unit = "meters"
        elif unit == "centimeter" or unit == "cm":
            unit = "centimeters"
        elif unit == "millimeter" or unit == "mm":
            unit = "millimeters"
    # Add the unit to the `current_calculation` list
    current_calculation.append(unit)

    # Print the calculation
    print("")
    print("=======================================")
    print("Calculating the {} of a {}".format(method, shape.lower()))
    print("=======================================")
    print("")
    print("{}".format(neat_calculation))
    if method == "area":
        print("= {:.2f} {}^2".format(answer, unit))
    else:
        print("= {:.2f} {}".format(answer, unit))
    print("")
    # Asks the user if they want to make another calculation or close
    # the program.
    keep_going = input("Type <enter> to continue, or anything else to exit.")

# Prints the calculation history to the user
# when the program has ended.
print("")
print("Calculation History:")
# Loops through the `calculations` list.
for item in calculations:
    # Prints each calculation to the user.
    if item[1] == "area":
        print("{} of a {} | {} = {:.2f} {}^2".format(item[1], item[0], item[2], item[3], item[4]))
    else:
        print("{} of a {} | {} = {:.2f} {}".format(item[1], item[0], item[2], item[3], item[4]))