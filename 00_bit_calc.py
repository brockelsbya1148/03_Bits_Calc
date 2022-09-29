from time import sleep
# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# Checks user choice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:

        response = input("File type (integer / text / image): ").lower()

        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        image_ok = ["image", "img", "pix", "picture", "pic", "p"]
        if response in image_ok:
            return "image"

        integer_ok = ["integer", "int"]
        if response in integer_ok:
            return "integer"

        elif response == "i":
            want_integer = input("Press <enter> for integer or anything else for image ")
            if want_integer == "":
                return "integer"
            else:
                return "image"
        
        else:
            print("Please choose a valid file type!")
            print()


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


# Calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # Ask user for a string...
    var_text = input("Enter some text: ")

    # Calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # Output answer with working
    print()
    print("\'{}\' has {} characters ...".format(var_text, var_length))
    sleep(1)
    print("# of bits is {} x 8...".format(var_length))
    sleep(1)
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""


# Finds # of bits for 24 bit colour
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


# Converts decimal to binary and states how many bits are needed to represent the original integer
def int_bits():

    # Get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    var_binary = "{0:b}".format(var_integer)

    # Calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # Output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    sleep(1)
    print("# of bits is {}".format(num_bits))
    print()

    return ""



# Main Routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print()
    print("You chose", data_type)
    print()

    # For integers, ask for integer
    # (must be an integer more than / equal to 0)
    if data_type =="integer":
        int_bits()
    
    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "image":
        image_bits()
    
    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()