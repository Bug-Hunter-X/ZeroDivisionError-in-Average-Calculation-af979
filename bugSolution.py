def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return total / count

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")
# Output: The average is: 0