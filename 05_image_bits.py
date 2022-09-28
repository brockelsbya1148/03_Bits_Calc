from time import sleep

# checks input is a number more than a given value

def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than (or equal to) {} ".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()


# finds # of bits for 24 bit colour
def image_bits():

    # Get width and height
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)
    print()

    # Calculate # of bits
    num_pixels = image_width * image_height
    num_bits = num_pixels * 24

    # Output # of bits with working
    print("Image width is {}...".format(image_width))
    sleep(1)
    print("Image height is {}...".format(image_height))
    sleep(1)
    print("# of pixels is {} x {}...".format(image_width, image_height))
    sleep(1)
    print("# of bits is {} x 24...".format(num_pixels))
    sleep(1)
    print("We need {} bits to represent the image".format(num_bits))
    print()

    return ""

# Main routine goes here
image_bits()