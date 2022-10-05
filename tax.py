#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 3rd, 2022
# This program gets the subtotal from
# the user and then calculates the
# amount of dollars the user will
# pay in taxes if they make their purchase
# in Nunavut using the tax rate of 5%
# then the program calculates the amount
# the user will pay in total,
# subtotal and tax together.
import tax_constants


# this function calculates the dollars in tax
# and then the total cost including tax
# if the purchase is made in Nunavut.
def main():
    # getting the subtotal from the user.
    subtotal = float(input("Please enter the subtotal in CAD: "))

    # calculating the dollars spent in tax
    # and the total spent.
    tax_dollars = subtotal * tax_constants.TAX_RATE
    total = subtotal + tax_dollars

    # displaying the results of the above calculations
    # back to the user.
    print(
        "In Nunavut, the amount in tax added"
        " to your subtotal will be: ${:,.2f} CAD".format(tax_dollars)
        )
    print(
        "In Nunavut, with that subtotal, you will end up"
        " paying ${:,.2f} CAD in total with taxes added.".format(total)
        )


if __name__ == "__main__":
    main()
