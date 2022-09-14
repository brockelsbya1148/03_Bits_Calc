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


# Main Routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    # For integers, ask for integer
    # (must be an integer more than / equal to 0)

    # For images, ask for width and height
    