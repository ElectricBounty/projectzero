def yes_no(question, error):
    """returns yes or no if user types y/n, loops if neither"""
    while True:
        answer = input(question).lower()[0]
        if answer in ["y","n"]:
            return answer
        else:
            print(error)
            continue

while True:
    yn = yes_no("yes/no ", "gotta say y / n")
    print(f"you said {yn}")