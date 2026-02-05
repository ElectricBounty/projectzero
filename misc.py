def statement_generator(statement, decoration, multiplier):
    """Displays a statement with a certain number of decorations on each side"""
    print(f"\n{decoration * multiplier} {statement} {decoration * multiplier}")

def int_check(question, error, low, high, exitcode):
    """Catches any integers that are invalid or in a range, return false on high for it to have no maximum"""

    while True:

        try:
            # ask user for a number
            response = input(question)
            if response.lower() == exitcode:
                return exitcode
            # check that number is more than low number and that there IS a low number
            if low is not None and int(response) < low or int(response) > high:
                print(error)
                continue
            return int(response)

        # checks that number is valid
        except ValueError:
            print(error)
            continue

def str_checker(question, available_choices):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question)
        if choice.lower() in available_choices:
            return choice.lower()[0]
        else:
            print("That is not a valid choice.")
            continue

def yes_no(question, error):
    """returns true if user types yes, returns false if no, loops if neither"""
    while True:
        yes = ["yes", "y"]
        no = ["no", "n"]
        response = input(question).lower()
        if response in yes:
            return True
        elif response in no:
            return "no"
        else:
            print(error)