def ask_number(question, low, high, step = 1):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response
