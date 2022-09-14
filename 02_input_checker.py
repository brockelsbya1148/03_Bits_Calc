# Checks user choice is 'integer', 'text', or 'image'
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
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()