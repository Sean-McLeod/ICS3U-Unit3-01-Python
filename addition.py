#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can do addition for two numbers


def main():
    # this function can do addition

    # input
    first_number = int(input("Enter the 1st number you want to add: "))
    second_number = int(input("Enter the 2nd number you want to add: "))

    # process
    sum = first_number + second_number

    # output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, sum))


if __name__ == "__main__":
    main()
