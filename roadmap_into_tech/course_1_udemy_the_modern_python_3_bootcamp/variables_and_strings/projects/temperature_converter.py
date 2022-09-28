'''
The below takes the temperature in celsius and converts it into fahrenheit by
asking for user input on the temperature in celsius
'''

print("What's the temperature in celsius?")
celsius = input()

celsius = float(celsius)
fahrenheit = (celsius * 1.8) + 32
fahrenheit = round(fahrenheit, 2)

print(f"The temperature in {celsius}°C is {fahrenheit}°F")
