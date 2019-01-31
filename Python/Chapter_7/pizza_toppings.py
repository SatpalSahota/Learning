prompt = "\nPlease let us know what toppings you would like on your pizza: "
prompt += "\n(Please type 'finished' when you have added all of your desired toppings.) "


while True:
    topping = input(prompt)
    if topping == 'done':
        break
    else:
        print("Adding " + topping.title() + " to your pizza!")
