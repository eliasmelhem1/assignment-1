while(True):
    def binary_to_decimal(binary):
        decimal = 0
        power = len(binary) - 1
        
        for digit in binary:
            if digit == '1':
                decimal += 2 ** power
            elif digit != '0':
                return None  # Return None for invalid input
            power -= 1
        
        return decimal

    # Get binary number input from the user
    binary_number = input("Enter a binary number: ")

    # Check if the input contains only 0s and 1s
    if all(bit in '01' for bit in binary_number):
        # Convert binary to decimal
        decimal_number = binary_to_decimal(binary_number)
        
        if decimal_number is not None:
            # Print the equivalent decimal number
            print("Equivalent decimal number:", decimal_number)
            break
        else:
            print("Invalid binary number!")
    else:
        print("Invalid input! Please enter a binary number containing only 0s and 1s.")
