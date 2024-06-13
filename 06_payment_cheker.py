# functions go here
# Checks user has entered yes / no to a question
def payment_checker(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "CA":
            return "cash"
        elif response == "credit" or response == "cr":
            return "credit"
        else:
            print("please enter a valid payment method")


# main routine goes here
while True:
    payment_method = payment_checker("Please enter a payment method, cash or credit: ")

    print("You have chosen to pay with", payment_method)

    print("program continues")
    print()
