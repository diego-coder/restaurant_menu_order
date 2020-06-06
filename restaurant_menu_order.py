

def get_table_number():
    table_number = int(input("What is the table number? "))
    print("You entered table #" + str(table_number) +".")
    return table_number

def get_number_of_diners_at_table():
    number_of_diners = 0
    while number_of_diners <= 0 or number_of_diners >= 5:
        number_of_diners = int(input("Enter the number of diners between 1 and 4: "))
        print("\nYou entered " + str(number_of_diners) + " as the number of diners.")
    return number_of_diners

def display_menu_of_food_items():

    print("\n1) eggs $3.25\n2) bacon $4.00\n3) pancakes $2.50\n4) orange juice $1.25\n5) oatmeal $3.99\n6) milk $1.25\n7) donut $2.00\n")

def get_menu_item():
    menu_item_number = 0
    while menu_item_number <=0 or menu_item_number >= 8:
        menu_item_number = int(input("\nEnter the menu item number between 1 and 7: "))
        print("\nYou entered item number " + str(menu_item_number) + ".\n")
    return menu_item_number

def get_diner_order():
    global table_total_before_tax
    global table_total_after_tax
    this_diners_total = 0.0
    display_menu_of_food_items()
    while input("Do you want to order an item? Answer y or n: ") == "y":
        order_choice = get_menu_item()
        if order_choice == 1:
            this_diners_total += float(3.25)
        elif order_choice == 2:
            this_diners_total += float(4.00)
        elif order_choice == 3:
            this_diners_total += float(2.50)
        elif order_choice == 4:
            this_diners_total += float(1.25)
        elif order_choice == 5:
            this_diners_total += float(3.99)
        elif order_choice == 6:
            this_diners_total += float(1.25)
        elif order_choice == 7:
            this_diners_total += float(2.00)
        print("This diner's total is now $" + str(round(this_diners_total, 2)) + ".\n")
    print("\nThe final cost of this diner's order is now $" + str(round(this_diners_total,2)) + ".\n")
    table_total_before_tax += this_diners_total
    round(table_total_before_tax, 2)
    return table_total_before_tax

def calculate_table_total(table_total_before_tax):
    global table_total_after_tax
    tax = .08
    total_tax = table_total_before_tax * tax
    table_total_after_tax = table_total_before_tax + total_tax
    round(table_total_after_tax, 2)
    return table_total_after_tax

def display_diners_totals(table_total_before_tax, table_total_after_tax):
    print("The total for the table before tax is $" + str(table_total_before_tax) + ", and the after tax total is $" + str(table_total_after_tax) + ".")

def display_table_total_info(table_total_before_tax):
    global grand_total_with_tip
    table_total = table_total_before_tax
    chosen_tip = 0.0
    print("\n10% tip: $" + str(round((table_total * .10), 2)) + "\n15% tip: $" + str(
        round((table_total * .15), 2)) + "\n20% tip: $" + str(round((table_total * .20), 2)) + "\n25% tip: $" + str(
        round((table_total * .25), 2)) + "\n")
    tip_amount = 0.0
    while tip_amount != 10 and tip_amount != 15 and tip_amount != 20 and tip_amount != 25:
        tip_amount = float(input("Please enter 10, 15, 20, or 25: "))
        if tip_amount == 10:
            chosen_tip = round((table_total * .10), 2)
        elif tip_amount == 15:
            chosen_tip = round((table_total * .15), 2)
        elif tip_amount == 20:
            chosen_tip = round((table_total * .20), 2)
        elif tip_amount == 25:
            chosen_tip = round((table_total * .25), 2)
    grand_total_with_tip = round((chosen_tip + table_total_after_tax), 2)
    print("\nThe grand total for this table with tip is $" + str(grand_total_with_tip) + ".")
    return grand_total_with_tip

def get_table_order(number_of_diners):
    global table_total_before_tax
    global table_total_after_tax
    table_total_before_tax = 0.0
    table_total_after_tax = 0.0
    diner = 1
    while diner <= number_of_diners:
        get_diner_order()
        diner += 1
    calculate_table_total(table_total_before_tax)
    display_diners_totals(table_total_before_tax, table_total_after_tax)
    display_table_total_info(table_total_before_tax)
    return table_total_after_tax

def main_program():
    after_tax_grand_total_for_the_day = 0.0
    while input("Do you want to add a table? Answer y or n: ") == "y":
        table_number = get_table_number()
        number_of_diners = get_number_of_diners_at_table()
        get_table_order(number_of_diners)
        after_tax_grand_total_for_the_day += table_total_after_tax
        after_tax_grand_total_for_the_day = round(after_tax_grand_total_for_the_day, 2)
    print("\nThe total sales (after tax) for the day are: $" + str(after_tax_grand_total_for_the_day) + ".")

main_program()