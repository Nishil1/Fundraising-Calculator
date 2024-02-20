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


for item in range(0, 6):
    want_help = yes_no("Do you want to read the instructions? ")
    print(f"you said '{want_help}'\n")
