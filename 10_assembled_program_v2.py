# Assembled program
# Version 2

# Used for pi in some calculations
import math

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


# Function that checks if the user input is a valid
# shape. If not returns a error.
def check_shape(question):
    error = "Please enter either square, triangle, circle, rectangle or parallelogram."
    valid = False
    while not valid:
        response = input(question)
        has_errors = ""
        # Checks if the user input is not an acceptable shape from
        # the `accepted_shapes` variable.
        if response.lower() not in accepted_shapes:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


# Function that checks if the user input is a valid
# unit. If not returns a error.
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


# Function that checks if the user input is a valid
# calculation method. If not returns a error.
def check_method(response):
    error = "Please enter either area or perimeter."
    valid = False
    while not valid:
        response = input(response)
        has_errors = ""
        if response.lower() not in accepted_methods:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response.lower()


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
keep_going = ""
print_instructions()

# Loops while program
while keep_going == "":
    # Resets the `current_calculation` variable
    current_calculation = []
    print("Available shapes: square, triangle, circle, rectangle or parallelogram.")

    # Asks user for which shape they want to use.
    shape = check_shape("Which shape would you like to use? ")
    # Adds the shape the `current_calculation` list
    current_calculation.append(shape)
    # Asks user for which unit they want to use.
    unit = check_unit("What is the unit? ")
    # Asks user for the area or perimeter to be calculated.
    method = check_method("Area or perimeter? ")
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
        if method == "perimeter":
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
            side_three = number_checker("Side Three? ")
            side_four = number_checker("Side Four? ")
            neat_calculation = "{:.0f} + {:.0f} + {:.0f} + {:.0f}".format(side_one, side_two, side_three, side_four)
            answer = side_one + side_two + side_three + side_four
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
        if unit == "kilometers" or "km":
            unit = "kilometer"
        elif unit == "meters" or "m":
            unit = "meter"
        elif unit == "centimeters" or "cm":
            unit = "centimeter"
        elif unit == "millimeters" or "mm":
            unit = "millimeter"
    else:
        # If the unit is kilometer/km but the answer
        # is greater than 1 it will replace the unit
        # with kilometers.
        if unit == "kilometer" or "km":
            unit = "kilometers"
        elif unit == "meter" or "m":
            unit = "meters"
        elif unit == "centimeter" or "cm":
            unit = "centimeters"
        elif unit == "millimeter" or "mm":
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
    print("= {:.2f} {}".format(answer, unit))
    # If the size of the `calculations` list is
    # more than 1 print the history.
    if len(calculations) > 1:
        print("")
        print("Calculation History:")
        for item in calculations:
            print("{} = {:.2f} {}".format(item[2], item[3], item[4]))

    print("")
    # Asks the user if they want to make another calculation or close
    # the program.
    keep_going = input("Type <enter> to continue, or anything else to exit.")