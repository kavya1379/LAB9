def check_even_or_odd(numbers):
    """
    Checks if each number in a set is even or odd.

    Args:
        numbers: A set of integers.

    Returns:
        A dictionary where keys are the numbers and values are 'Even' or 'Odd'.
    """
    results = {}
    for number in numbers:
        if number % 2 == 0:
            results[number] = "Even"
        else:
            results[number] = "Odd"
    return results

# Example usage:
number_set = {5, 12, 8, 17, 4, 9}
status = check_even_or_odd(number_set)
print(status)
# Output will be something like: {8: 'Even', 4: 'Even', 12: 'Even', 5: 'Odd', 17: 'Odd', 9: 'Odd'}
