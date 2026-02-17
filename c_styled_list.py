def styled_instructions(symbol, array):
    """takes an array of sentences and formats them into a bullet-pointed list"""

    # iterate through array and print items with a
    for item in array:
        print(f"{symbol} {item}")