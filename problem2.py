def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    print("Temperature Converter")
    print("-" * 30)

    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("❌ Error: You must enter a number.")
        return

    unit = input("Enter the current unit (C/F): ").strip().upper()

    if unit == "C":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp:.2f} °C = {result:.2f} °F")
    elif unit == "F":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp:.2f} °F = {result:.2f} °C")
    else:
        print("❌ Error: Unit must be 'C' or 'F'.")

if __name__ == "__main__":
    print("Running tests...")
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!\n")
    temperature_converter()
