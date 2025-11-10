def temp_converter():
    print("This ia a Temperature Converter, what would you like to convert? ")
    print("1. Degree Celcius to Degree Farenheit")
    print("2. Degree Celcius to Kelvin")
    print("3. Degree Farenheit to Degree Celcius")
    print("4. Kelvin to Degree Celcius")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = float(input("Enter the temperature in Degree Celcius: "))
        num1 = ((9 * num) / 5) + 32
        print(f"The corresponding temperature in Degree Farenheit is {num1}")
    elif choice == "2":
        num = float(input("Enter the temperature in Degree Celcius: "))
        num2 = num + 273
        print(f"The corresponding temperature in Kelvin is {num2}")
    elif choice == "3":
        num = float(input("Enter the temperature in Degree Farenheit: "))
        num3 = (5 / 9) * (num - 32)
        print(f"The corresponding temperature in Degree Celcius is {num3}")
    elif choice == "4":
        num = float(input("Enter the temperature in Kelvin: "))
        num4 = num - 273
        print(f"The corresponding temperature in Degree Celcius is {num4}")
    elif choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")


temp_converter()
