def temp_converter():
    print("This ia a Temperature Converter, what would you like to convert? ")
    print("1. Degree Celcius to Degree Farenheit")
    print("2. Degree Celcius to Kelvin")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = float(input("Enter the temperature in Degree Celcius: "))
        num1 = ((9 * num) / 5) + 32
        print(f"The corresponding temperature in Degree Farenheit is {num1}")
    else:
        num = float(input("Enter the temperature in Degree Celcius: "))
        num2 = num + 273
        print(f"The corresponding temperature in Kelvin is {num2}")

temp_converter()
