def decimal_to_binary():
    try:
        decimal = int(input("Enter the decimal number : "))
        if decimal == 0:
            return "0"
        else:
            result = ""
            while decimal > 0:
                result += str(decimal % 2)
                decimal = decimal // 2

            return result[::-1]
    except ValueError:
        print("Proper inputs please...")
        return decimal_to_binary()


def binary_to_decimal():
    binary = input("Enter the binary number : ")
    try:
        int(binary)
        number = 0
        for h in range(len(binary)):
            number += int(binary[h]) * (2 ** (len(binary) - h - 1))
        return number

    except ValueError:
        print("Proper inputs please...")
        return binary_to_decimal()



def binary_substraction():
    binary1 = input("Enter the greater binary number : ")
    binary2 = input("Enter the less binary number : ")
    binary2_ones_complement = ""
    for h in binary2:
        binary2_ones_complement += str(1-int(h))
    binary2_twos_complement = binary_addition_with_arg(binary2_ones_complement, "1")
    return binary_addition_with_arg(binary1, binary2_twos_complement)







def binary_addition():
    binary1 = input("Enter the first binary number : ")
    binary2 = input("Enter the second binary number : ")
    if len(binary1) < len(binary2):
        binary1 = (len(binary2) - len(binary1)) * "0" + binary1
    elif len(binary2) < len(binary1):
        binary2 = (len(binary1) - len(binary2)) * "0" + binary2
    result = ""
    remain = 0
    for h in range(len(binary1) -1, -1, -1):
        resultnum = 0
        resultnum += remain
        remain = (int(binary1[h]) + int(binary2[h])) // 2
        resultnum = (int(binary1[h]) + int(binary2[h])) % 2
        result += str(resultnum)
    if remain == 1:
        result += str(remain)
    return result[::-1]


def binary_addition_with_arg(binary1, binary2):
    if len(binary1) < len(binary2):
        binary1 = (len(binary2) - len(binary1)) * "0" + binary1
    elif len(binary2) < len(binary1):
        binary2 = (len(binary1) - len(binary2)) * "0" + binary2
    result = ""
    remain = 0
    for h in range(len(binary1) -1, -1, -1):
        resultnum = 0
        resultnum += remain
        remain = (int(binary1[h]) + int(binary2[h])) // 2
        resultnum = (int(binary1[h]) + int(binary2[h])) % 2
        result += str(resultnum)
    if remain == 1:
        result += str(remain)
    return result[::-1]


def main_menu():
    print("Choose the operation that you want:")
    print("1) Decimal to Binary")
    print("2) Binary to Decimal")
    print("3) Binary Addition")
    print("4) Binary Subtraction")
    print("5) Binary Multiplication")
    print("6) Binary Division")
    print("Any Other Key To Exit")
    chosen_option = input("Which: ")
    match chosen_option:
        case "1":
            result = decimal_to_binary()
            print(f"Result is {result}")
            main_menu()
        case "2":
            result = binary_to_decimal()
            print(f"Result is {result}")
            main_menu()
        case "3":
            result = binary_addition()
            print(f"Result is {result}")
            main_menu()
        case "4":
            result = binary_substraction()
            print(f"Result is {result}")
            main_menu()
        case "5":
            print("a")
        case "6":
            print("a")
        case _:
            quit()

def main():
    main_menu()

main()