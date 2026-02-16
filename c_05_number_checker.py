def num_check(question, error, num_type, exitcode=None):
    """Catches any numbers that are invalid or in a range, allow programmer to set num_type"""

    # define change_to variable as either the int function or the float function
    if num_type == "int":
        change_to = int
    else:
        change_to = float

    while True:
        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode
            return change_to(response)

        # checks that number is valid
        except ValueError:
            print(error)


while True:
    number = num_check("type number ", "you screwed up big fulla", "int")
    print(number)
