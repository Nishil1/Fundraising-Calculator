# import libraries

# *** Functions go here ***

# checks that input is either a float or a integer that is more than 0
# Takes in custom error message
def num_check(question, error, num_type):
    while True:
        try:

            response = num_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


# Checks that user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    while True:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return var_item
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no... \n")


# main routine

# Get quantity of product
get_int = num_check("How many do you need? ",
                    "Please enter an amount more than 0\n", int)

# Get cost of product
get_cost = num_check("How much does it cost? $",
                     "Please enter a number for than 0\n", float)

print(f"You need: {get_int}")
print(f"It costs ${get_cost}")
