# Component 3

# Asks the user if they want the program to calculate
# the area or perimeter of the shape.

# Initialize variables
accepted_inputs = ['perimeter', 'area']


# Check if user input is a valid method.
def check_input(question):
    error = "Please enter either area or perimeter."
    valid = False
    while not valid:
        response = input(question)
        has_errors = ""
        # Checks if the user input is not an acceptable method from
        # the `accepted_inputs` variable.
        if response.lower() not in accepted_inputs:
            has_errors = "yes"
        if has_errors != "":
            print(error)
            continue
        else:
            return response


# Prints the list of available methods.
print("Available forms of calculation: Area or Perimeter.")
print("")

# Asks the user for which method they want to use.
calculation_method = check_input("Which calculation method would you like to use? ")
print("You selected {}!".format(calculation_method.lower()))