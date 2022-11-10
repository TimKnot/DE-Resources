input_conversion = input("Convert to Celsius or Fahrenheit (C/F): ")
conversion = input_conversion.upper()
if conversion not in ['C', 'F']:
    print("Unknown conversion.")
else:
    input_temperature = input("Temperature: ")
    temperature = float(input_temperature)
    if conversion == "C":
        # F -> C
        c = (temperature - 32) * (5/9)
        print(f"{c}c")
    else:
        # C -> F
        f = (temperature * 1.8) + 32
        print(f"{f}f")
