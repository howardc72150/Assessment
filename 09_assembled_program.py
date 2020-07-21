# Assembled program

# Initialize variables:

x = ""
y = ""
answer = ""
shape = ""
calculation = ""
current_calculation = ""

solved_calculation = []
calculation_history = []
accepted_units = ['kilometers', 'kilometer', 'km', 'meters', 'meter', 'm', 'centimeters', 'centimeter', 'cm', 'millimeters', 'millimeter', 'mm']
units = "kilometer(s), km, meter(s), m, centimeter(s), cm, millimeter(s), mm"
accepted_shapes = ['square', 'triangle', 'circle', 'rectangle', 'parallelogram']
accepted_methods = ['area', 'perimeter']


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


def check_input(question):
    error = "Please enter a number that is more than zero."
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


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


def ask_dimensions(shape, method):
    if shape == "square":
        if method == "area":
            x = check_input("Side length: ")
            answer = x**2
            calculation = "{:.0f}^2".format(x)
        elif method == "perimeter":
            x = check_input("Side length: ")
            answer = 4*x
            calculation = "4x{:.0f}".format(x)
    elif shape == "triangle":
        x = check_input("Base: ")
        y = check_input("Height: ")
    elif shape == "circle":
        x = check_input("Radius: ")
    return answer, calculation


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


def ask_area_perimeter(response):
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

# Main routine

keep_going = ""
print_instructions()

while keep_going == "":
    print("Available shapes: square, triangle, circle, rectangle or parallelogram.")

    shape = check_shape("Which shape would you like to use? ")
    calculation_method = ask_area_perimeter("Calculate the area or perimeter? ")
    unit = check_unit("What is the unit? ")
    answer, calculation = ask_dimensions(shape, calculation_method)

    if answer > 1:
        if unit == "kilometer":
            unit = "kilometers"
        elif unit == "meter":
            unit = "meters"
        elif unit == "centimeter":
            unit = "centimeters"
        elif unit == "millimeter":
            unit = "millimeters"
    else:
        if unit == "kilometers":
            unit = "kilometer"
        elif unit == "meters":
            unit = "meter"
        elif unit == "centimeters":
            unit = "centimeter"
        elif unit == "millimeters":
            unit = "millimeter"

    solved_calculation.append(calculation)
    solved_calculation.append(unit)

    current_calculation.append(solved_calculation)
    print("ashfaishf")
    print(current_calculation)

    add_to_history = ("({} | {} of a {}) {}={}".format(calculation_method, unit, shape, calculation, answer))
    calculation_history.append(add_to_history)

    print("")
    print("=======================================")
    print("Calculating the {} of a {}".format(calculation_method, shape.lower()))
    print("=======================================")
    print("")
    print("{}".format(calculation))
    print("= {} {}".format(answer, unit))
    list = len(calculation_history)
    if list > 1:
        print("")
        print("Calculation History:")
        for item in calculation_history:
            print(item)


    print("")
    keep_going = input("Type <enter> to continue, or anything else to exit.")