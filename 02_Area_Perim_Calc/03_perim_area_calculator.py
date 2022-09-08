# functions go here

# checks input is more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()

 
# Main Routine goes here
width = num_check("Width: ")
height = num_check("Height: ")

perimeter = (width + height) * 2
area = width * height

print()
print("Perimeter: ", perimeter)
print("Area: ", area)
print()

