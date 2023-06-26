#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                num += 1
            except (TypeError, ValueError):
                pass
    except TypeError:
        pass
    finally:
        print()
        return (num)
