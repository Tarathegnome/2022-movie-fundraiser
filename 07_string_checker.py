# checks that users enter a valid response(e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_response):
    error = "Please choose {} or {}".format(valid_response[0], valid_response[1])

    while True:
        response = input(question).lower()

        for item in valid_response:
            if response == item[num_letters] or response == item:
                return item
        print(error)


# main routine goes here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the instructions (y/n):",
                                       1, yes_no_list)
    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = string_checker("Please enter a payment method, cash or credit: ",
                                2, payment_list)
    print("You chose", pay_method)
