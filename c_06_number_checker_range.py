def num_check(question, num_type, high, low, error, exitcode=None):
    """only accept numbers within a certain range"""

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

            # check if in range
            if low <= change_to(response) <= high:
                return change_to(response)
            else: print(error)

        # checks that number is valid
        except ValueError:
            print(error)


while True:
    number = num_check("type number ", "float", 10,0,"you screwed up big fulla", "int")
    print(number)
