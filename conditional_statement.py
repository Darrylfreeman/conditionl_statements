def check_number_sign(number):
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print("The number is zero.")

# Ask the user for a number
user_input = int(input("Enter a number: "))
check_number_sign(user_input)