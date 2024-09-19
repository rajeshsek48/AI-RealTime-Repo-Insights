# buggy_code.py

def divide_numbers(a, b):
    """
    Function to divide two numbers.
    Args:
    a (int): The numerator.
    b (int): The denominator.
    
    Returns:
    float: The result of the division.
    """
    # Bug: No error handling for division by zero
    result = a / b
    return result

def main():
    num1 = 10
    num2 = 0  # This will cause a division by zero error
    print(f"The result of {num1} divided by {num2} is: {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()
