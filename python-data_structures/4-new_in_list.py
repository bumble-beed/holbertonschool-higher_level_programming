#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # replace element in list at a specific position without modifying original list (i.e make a new list)
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list(idx) = element
    return new_list
