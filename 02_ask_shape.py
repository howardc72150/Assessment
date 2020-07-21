# Component 2

# Asks the user which shape they want to be calculated
# either square, triangle, circle, rectangle or parallelogram.

# Initialize variables
accepted_shapes = ['square', 'triangle', 'circle', 'rectangle', 'parallelogram']


# Check if user input is a valid shape.
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
            return response


# Prints the list of available shapes.
print("Available shapes: Square, Triangle, Circle, Rectangle or Parallelogram.")
print("")

# Asks the user for which shape they want to use.
shape = check_shape("Which shape would you like to use? ")
print("You selected {}!".format(shape.lower()))