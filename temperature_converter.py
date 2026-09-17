ask_temperature = int(input("what is the temperature outside? "))
ask_unit = input("f or C : ")

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


if ask_unit == "f":
    print(fahrenheit_to_celsius(ask_temperature))
else:
    print(celsius_to_fahrenheit(ask_temperature))