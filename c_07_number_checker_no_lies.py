def int_check(question, error):
    """only accept integers"""

    while True:
        try:
            # ask user for a number
            response = input(question)

            return int(response)

        # checks that number is valid
        except ValueError:
            print(error)

# testing goes here
while True:
    print()

    # get users name
    name = str(input("what's your name? "))

    # get users age
    age = int_check("how old are you: ", "please enter a valid integer")

    if 12 <= age <= 120:
        print(f"{name} bought a ticket ({age}y)")
    elif age < 12:
        print(f"you are too young! ({age}y)")
    else:
        print(f"you are too old! ({age}y)")