# main.py

def greet_user(name):
    """
    Function to greet the user with their name.
    """
    if name:  # Check if the name is provided
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

def calculate_sum(a, b):
    """
    Function to calculate the sum of two numbers.
    """
    return a + b

if __name__ == "__main__":
    # Greet the user
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # Calculate the sum of two numbers
    num1 = 10
    num2 = "5"  # This is an intentional bug (string instead of int)
    total = calculate_sum(num1, num2)  # This will cause a TypeError
    print(f"The sum of {num1} and {num2} is {total}")
