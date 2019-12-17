# Celsius2fahrenhiet - function inside function

def temperature(t):
    def celsius2fahrenheit(x):
        return 9*x/5+32
    result = ' '.join(["it's",str(celsius2fahrenheit(t)),"degree!"])
    return result

print(temperature(20))

