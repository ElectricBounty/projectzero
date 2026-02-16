def str_checker(question, available_choices, error):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question)
        if choice.lower() in available_choices:
            return choice.lower()
        else:
            print(error)