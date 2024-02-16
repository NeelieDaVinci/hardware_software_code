def binary_to_decimal(binary):
    #Function for converting binary to decimal#
    decimal = 0
    power = 0
    for digit in binary[::-1]:
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

def decimal_to_binary(decimal):
    #Function for converting decimal to binary#
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def display_menu():
    #To display menu#
    print("Menu:")
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("5.")
    print("6.")
    print("7.")
    print("8.")
    print("9.")

        power = len(str(number)) - 1
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1
        return result

def main():
    num = input("Enter Binary Number:")
    print("Number entered: {}".format(num))
    print("Decimal to Binary: {}".format(binary_to_decimal(num)))

if __name__ == "__main__":
    main()
