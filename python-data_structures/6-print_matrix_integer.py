#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in range(len(row)):
            if number == len(row) - 1:
                print("{:d}".format(row[number]))
            else:
                print("{:d}".format(row[number]), end=" ")
