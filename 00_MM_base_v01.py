# functions go here
# Checks if users response is blank or not
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# checks users enter and integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# calculate the ticket price based on the age


def calc_ticket_price(var_age):
    # tickets is $7.50 for users under 16
    if var_age < 16:
        price = 7.50

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.50

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.50

    return price


# checks that users enter a valid response(e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_response):
    error = "Please choose {} or {}".format(valid_response[0], valid_response[1])
    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_response:
            if response == item[short_version] or response == item:
                return item
        print(error)


# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read the instructions(y/n)?: ", 1, yes_no_list)

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions goes here")

print()

# loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("sorry you are too young to watch this movie")
        continue

    else:
        print("?? That looks like a typo, please try again")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket prices: ${:.2f}".format(age, ticket_cost))

    # get payment method
    pay_method = string_checker("Please enter a payment method, cash or credit: ",
                                2, payment_list)

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket's. There is {} ticket'\
    remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
