#!/usr/bin/env python3
# Calculator Program
# Created by: Brandon
# Created on: 12/09/25
# This program performs basic arithmetic operations


def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number


# Main function that controls program flow
def main():
    # Loop until valid input is entered
    while True:
        # Ask the user to enter an operation
        sign = input("Enter operation (+, -, *, /): ")
        # Check if the operation is valid
        if sign != "+" and sign != "-" and sign != "*" and sign != "/":
            print("Invalid operation. Please try again.\n")
            continue
        try:
            # Ask the user to enter two numbers
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
        # Catch errors if the input is not a number
        except ValueError:
            print("Invalid number entered. Please enter decimals only.\n")
            continue
        # Prevent division by zero
        if sign == "/" and second_number == 0:
            print("Error: Division by zero is not allowed.\n")
            continue
        # Call the calculate function and store the result
        result = calculate(sign, first_number, second_number)
        # Display the result to the user
        print("\nResult:", first_number, sign, second_number, "=", result)
        break


# Call the main function to start the program
if __name__ == "__main__":
    main()
