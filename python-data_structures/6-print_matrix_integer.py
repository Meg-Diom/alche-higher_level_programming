#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(number))
            else:
                print("{:d}".format(number), end=" ")
