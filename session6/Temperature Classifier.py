def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif temp >= 0 and temp < 10:
        return "Very Cold"
    elif temp >= 10 and temp < 20:
        return "Cold"
    elif temp >= 20 and temp < 25:
        return "Moderate"
    elif temp >= 25 and temp < 30:
        return "Hot"
    elif temp >= 30:
        return "Very Hot"
    else:
        return "Invalid temperature"

print("Welcome! Here, you can check the condition of the weather when you insert the tempertaure")
while True:     
    print("1. Continue")
    print("2. Stop the program")
    choice = int(input("Please select 1 or 2: "))
    if choice == 1:
        temperature = float(input("Enter the temperature in Celsius: "))
        condition = classify_temperature(temperature)
        print("The temperature condition today is :", condition)
    elif choice == 2:
        print("Thank you for using this program. I hope it was helpful. You can come back anytime.")
        break
    else:
         ("This input is invalid. Please choose option 1 or 2")    