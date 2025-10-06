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
def is_prime(n):
    """
    Checks if a single integer 'n' is a prime number.
    
    A number is prime if it is greater than 1 and has no positive divisors 
    other than 1 and itself.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Check for divisibility from 2 up to the square root of n
    # We only need to check up to the square root because if 'n' has a divisor
    # larger than its square root, it must also have one smaller.
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False  # Found a divisor, so it's not prime
        i += 1
        
    return True  # If no divisors were found, it is prime

# --- Main Program ---

# Define the set of numbers to check
number_set = {2, 7, 10, 13, 25, 41, 1}

print(f"Set of numbers to check: {number_set}")
print("-" * 30)

# Iterate through the set and check each number
results = {}
for number in number_set:
    if is_prime(number):
        results[number] = "Prime"
    else:
        results[number] = "Not Prime"

# Print the results
for number, status in results.items():
    print(f"The number {number} is: {status}")

print("-" * 30)
