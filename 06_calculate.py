
current_calculation = []
print("Available shapes: square, triangle, circle, rectangle or parallelogram.")

shape = input("Which shape would you like to use? ")
current_calculation.append(shape)
unit = input("What is the unit? ")
method = input("Area or perimeter? ")
current_calculation.append(method)

if shape == "square":
    if method == "area":
        length = int(input("Length? "))
        neat_calculation = "{:.0f} x {:.0f}".format(length, length)
        answer = length * length
    elif method == "perimeter":
        length = int(input("Length? "))
        neat_calculation = "4x{:.0f}".format(length)
        answer = length * 4
    current_calculation.append(neat_calculation)
elif shape == "triangle":
    if method == "area":
        base = int(input("Base? "))
        height = int(input("Height? "))
        neat_calculation = "1/2 x {:.0f} x {:.0f}".format(base, height)
        answer = 0.5 * base * height
    if method == "perimeter":
        side_one = int(input("Side One? "))
        side_two = int(input("Side Two? "))
        side_three = int(input("Side Three? "))
        neat_calculation = "{:.0f} + {:.0f} + {:.0f} ".format(side_one, side_two, side_three)
        answer = side_one + side_two + side_three
    current_calculation.append(neat_calculation)

current_calculation.append(answer)
print("{} = {}".format(neat_calculation, answer))