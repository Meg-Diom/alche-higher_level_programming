#!/usr/bin/python3


def uniq_add.py(my_list=[]):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)

            j = 0
            total = 0

            while j < len(new_list):
                total = total + new_list[j]
                j += 1

        return total
