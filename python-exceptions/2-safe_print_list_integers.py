#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in range(x):
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end='')
                count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
