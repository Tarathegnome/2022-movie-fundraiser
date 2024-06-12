# functions go here


# main routine goes here
while True:
    want_instructions = input("Do you want to read the instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions goes here")
    elif want_instructions == "no" or want_instructions == "n":
        break
    else:
        print("please answer yes / no")
