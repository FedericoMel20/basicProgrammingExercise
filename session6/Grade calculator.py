print("\n Welcome! Here you can find out what grade you have by simply putting in your percentage score.")
while True:
    print("1. Continue")
    print("\n2. Stop the program")
    choice = int(input("Please select an option 1 or 2: "))
    if choice == 1:
        score = int(input("Please input your percentage score to see what grade it is: "))
        if score >= 90 and score <= 100:
            print("Congratulations, you have an excellent score. This is grade A")
        elif score >= 80 and score <= 89:
            print("Wow, your grade is B. Well done!")
        elif score >= 70 and score <= 79:
            print("Your grade is C. Good job")
        elif score >= 60 and score <= 69:
            print("The grade of your score is D. Not bad but there is still room for improvement")
        elif score >= 0 and score <= 59:
            print("Alas, your grade is F. You can still improve.")
        else:
            print("This score is invalid. Please insert a correct score")
    elif choice == 2:
        print("Thank you for choosing this program. I hope it was helpful. You can come back anytime.")
        break
    else:
         ("This input is invalid. Please choose option 1 or 2")           