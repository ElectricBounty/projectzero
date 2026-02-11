def str_checker(question, available_choices, num_letters, error):
    """returns the string if it meets anything in available_choices"""
    while True:
        choice = input(question).lower()
        for item in available_choices:

            if choice == item:
                return item
            
            # check first num_letters of letters to see if they tried to write the answer
            elif choice == item[:num_letters]:
                return item
            
        print(error)
        continue

answers = ["broken", "beyond repair", "banana"]

while True:
    ans = str_checker("say broken, \"beyond repair\" or banana: ", answers, 3, "WRONG")
    print(ans)