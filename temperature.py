#This code converts temperatures in Celsius , Fahrenheit and Kelvin

def Celsius_to_Kelvin(temperature): #To convert Celsius to Kelvin
    result = temperature+273.15
    return result
def Kelvin_to_Celsius(temperature): #To convert Kelvin to Celsius
    result = temperature-273.15
    return result
def Celsius_to_Fahrenheit(temperature): #To convert Celsius to Fahrenheit
    result = temperature*9/5+32
    return result
def Fahrenheit_to_Celsius(tempurature): #To convert Fahrenheit to Celsius 
    result = (tempurature-32)*5/9
    return result
def Kelvin_to_Fahrenheit(tempurature): #To convert Kelvin to Fahrenheit
    result = Celsius_to_Fahrenheit(Kelvin_to_Celsius(tempurature))
    return result
def Fahrenheit_to_Kelvin(tempurature): #To convert Fahrenheit to Kelvin
    result = Celsius_to_Kelvin(Fahrenheit_to_Celsius(tempurature))
    return result

temperature=float(input("Enter the value for Temperature : "))
unit=input("Enter the unit (C-Celsius,F-Fahrenheit,K-Kelvin) : ")
unit=unit.lower()
print("Entered : ",temperature,unit)
if unit=="c":
    print(f"Temperature in Fahrenheit : {Celsius_to_Fahrenheit(temperature):.2f} F")
    print(f"Temperature in Kelvin : {Celsius_to_Kelvin(temperature):.2f} K")
elif unit=="f":
    print(f"Temperature in Celsius : {Fahrenheit_to_Celsius(temperature):.2f} C")
    print(f"Temperature in Kelvin : {Fahrenheit_to_Kelvin(temperature):.2f} K")
elif unit=="k":
    print(f"Temperature in Celsius : {Kelvin_to_Celsius(temperature):.2f} C")
    print(f"Temperature in Fahrenheit : {Kelvin_to_Fahrenheit(temperature):.2f} F")
else: print("Invalid input")
