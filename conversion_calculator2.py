def binary_to_decimal(binary):
    # Function for converting binary to decimal
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def decimal_to_binary(decimal):
    # Function for converting decimal to binary
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def hexadecimal_to_decimal(hexadecimal):
    # Function for converting hexadecimal to decimal
    decimal = 0
    for digit in hexadecimal[::-1]:
        if digit.isdigit():
            decimal += int(digit) * (16 ** (hexadecimal.index(digit)))
        else:
            decimal += (ord(digit.upper()) - 55) * (16 ** (hexadecimal.index(digit)))
    return decimal

def decimal_to_hexadecimal(decimal):
    # Function for converting decimal to hexadecimal
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(remainder + 55) + hexadecimal
        decimal //= 16
    return hexadecimal

def hexadecimal_to_binary(hexadecimal):
    # Function for converting hexadecimal to binary
    binary = ''
    for digit in hexadecimal:
        if digit.isdigit():
            binary += bin(int(digit))[2:].zfill(4)
        else:
            binary += bin(int(digit, 16))[2:].zfill(4)
    return binary

def binary_to_hexadecimal(binary):
    # Function for converting binary to hexadecimal
    hexadecimal = ''
    for i in range(0, len(binary), 4):
        nibble = binary[i:i+4]
        hexadecimal += hex(int(nibble, 2))[2:].upper()
    return hexadecimal

def octal_to_decimal(octal):
    # Function for converting octal to decimal
    decimal = 0
    power = 0
    for digit in octal[::-1]:
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal

def decimal_to_octal(decimal):
    # Function for converting decimal to octal
    octal = ''
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def display_menu():
    # To display menu
    print("Menu:")
    print("1. Binary to Decimal")
    print("2. Decimal to Binary")
    print("3. Hexadecimal to Decimal")
    print("4. Decimal to Hexadecimal")
    print("5. Hexadecimal to Binary")
    print("6. Binary to Hexadecimal")
    print("7. Octal to Decimal")
    print("8. Decimal to Octal")
    print("9. Quit")

def main():
    # Function to Work
    while True:
        display_menu()
        choice = input("Select a Conversion: ")

        if choice == '1':
            binary = input("Enter a binary number: ")
            if all(bit in '01' for bit in binary):
                decimal = binary_to_decimal(binary)
                print(f"The decimal equivalent of {binary} is {decimal}.")
            else:
                print("Invalid binary number. Please enter a binary number (containing only 0s and 1s).")

        elif choice == '2':
            decimal = int(input("Enter a decimal: "))
            binary = decimal_to_binary(decimal)
            print(f"The binary equivalent of {decimal} is {binary}.")

        elif choice == '3':
            hexadecimal = input("Enter a hexadecimal number: ")
            if all(char.upper() in '0123456789ABCDEF' for char in hexadecimal):
                decimal = hexadecimal_to_decimal(hexadecimal)
                print(f"The decimal equivalent of {hexadecimal} is {decimal}.")
            else:
                print("Invalid hexadecimal number. Please enter a hexadecimal number (containing digits and A-F).")

        elif choice == '4':
            decimal = int(input("Enter a decimal: "))
            hexadecimal = decimal_to_hexadecimal(decimal)
            print(f"The hexadecimal equivalent of {decimal} is {hexadecimal}.")

        elif choice == '5':
            hexadecimal = input("Enter a hexadecimal number: ")
            if all(char.upper() in '0123456789ABCDEF' for char in hexadecimal):
                binary = hexadecimal_to_binary(hexadecimal)
                print(f"The binary equivalent of {hexadecimal} is {binary}.")
            else:
                print("Invalid hexadecimal number. Please enter a hexadecimal number (containing digits and A-F).")

        elif choice == '6':
            binary = input("Enter a binary number: ")
            if all(bit in '01' for bit in binary):
                hexadecimal = binary_to_hexadecimal(binary)
                print(f"The hexadecimal equivalent of {binary} is {hexadecimal}.")
            else:
                print("Invalid binary number. Please enter a binary number (containing only 0s and 1s).")

        elif choice == '7':
            octal = input("Enter an octal number: ")
            if all(bit in '01234567' for bit in octal):
                decimal = octal_to_decimal(octal)
                print(f"The decimal equivalent of {octal} is {decimal}.")
            else:
                print("Invalid octal number. Please enter an octal number (containing only digits 0-7).")

        elif choice == '8':
            decimal = int(input("Enter a decimal: "))
            octal = decimal_to_octal(decimal)
            print(f"The octal equivalent of {decimal} is {octal}.")

        elif choice == '9':
            print("Exiting Program")
            break

        else:
            print("Invalid choice. Pick a number in the menu")

if __name__ == "__main__":
    main()
