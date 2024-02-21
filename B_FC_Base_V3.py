# import libraries
import pandas

# functions go here

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

# makes sure an input is not blank
def not_blank(question, error):
    while True:

        response = input(question)

        if response == "":
            print(f"{error}. \nPlease try again. \n")
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


def expense_print(heading, frame, subtotal):
    print()
    print(f"**** {heading} Costs ****")
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


def get_expenses(var_fixed):
    # *** Main routine starts here  ***

    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {

        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Get user data
    product_name = not_blank("Product name: ", "The product name cannot be blank")

    item_name = ""
    while item_name.lower() != "xxx":

        print()

        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name cant be blank.")

        if item_name.lower() == "xxx":
            break
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":

            quantity = num_check("Quantity: ",
                                 "The amount must be a whole number more than zero.", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $",
                          "The price must be a number more than 0", float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict).set_index("Item")

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ["Price", "Cost"]
    for item in add_dollars:
        expense_frame['Item'] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# *** Main routine starts here ***

# Get product name

product_name = not_blank("Product name: ", "The product name cannot be blank")

print()
print("Please enter your variable costs below...")


# Get variable costs
variable_expenses = get_expenses("Variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fuxed costs (y / n)? ")

if have_fixed == "yes":
    # get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = variable_expenses[0]
    fixed_sub = variable_expenses[1]
else:
    fixed_sub = 0




# *** Printing Area ****

print()
print(f"**** Fund Raising - {product_name} *****")
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)





