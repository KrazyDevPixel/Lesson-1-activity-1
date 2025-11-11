def binary_to_decimal(binary_str):
    try:
        decimal = int(binary_str, 2)
        print(f"Decimal: {decimal}")
    except ValueError:
        print("Invalid binary input. Please enter only 0s and 1s.")
binary_input = input("Enter your Binary: ")
binary_to_decimal(binary_input)
