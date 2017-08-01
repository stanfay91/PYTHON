print("Where V2 Starts")
    goToStart = "no"
        while goToStart == "no":
            name = input("Please enter you name: ")
            print("Nice to meet you ", name)
            color = input("{},what is your favorite color: ".format(name))
            print("{}?, That's a nice color.".format(color))
            food = input("{}, what is your favorite food: ".format(name))
            print("{} sounds yummy.".format(food))
            goToStart = input("{}, do you have to go? (yes/no) ".format(name))

print("BUH BYE")