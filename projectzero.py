def int_check(question, error, low, high, exitcode):
    """Catches any integers that are invalid or in a range, return false on high for it to have no maximum"""

    while True:

        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode
            # check that number is more than low number and that there IS a low number
            # if low is not None and int(response) < low or int(response) > high:
            #     print(error)
            #     continue
            return int(response)

        # checks that number is valid
        except ValueError:
            print(error)
            continue

def str_checker(question, available_choices, error):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question)
        if choice.lower() in available_choices:
            return choice.lower()
        else:
            print(error)
            continue

def yes_no(question, error):
    """returns yes or no if user types y/n, loops if neither"""
    answer = str_checker(question, ["y","yes","n","no"], error)
    if answer in ["y", "yes"]:
        return "yes"
    else:
        return "no"