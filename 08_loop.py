# Component 8

# Loop the entire program from the beginning
# endlessly or until the user stops.
import random
# Initialize variables

# Manually set the calculation method, shape and dimensions for testing purposes,
# this would've been set by the user previously.
calculation_history = []
calculation_method = "area"
unit = "mm"

shape = "square"

keep_going = ""
while keep_going == "":
    x = random.randint(1, 10)
    current_calculation = ("{} of a {} | {:.0f} x {:.0f} = {:.0f}{}^2".format(calculation_method, shape, x, x, x*x, unit))
    calculation_history.append(current_calculation)

    print("=======================================")
    print("Area of a square".format(calculation_method.lower()))
    print("{:.0f} x {:.0f}".format(x, x))
    print("= {:.0f}".format(x * x))
    print("=======================================")
    print("Calculation History")
    for item in calculation_history:
        print(item)
    print("=======================================")

    print("")
    keep_going = input("Type <enter> to continue, or anything else to exit.")
