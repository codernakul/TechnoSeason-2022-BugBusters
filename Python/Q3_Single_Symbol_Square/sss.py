import random

zero_and_X = ["X", "O"]
size_of_layout = int(input("Please enter size of layout: "))


def layout_maker(n):
    layout = []
    for i in range(n * n):
        layout.append(random.choice(zero_and_X))

    return layout


def layout_printer(layout_to_print, size):
    for i in range(size * size):
        if (i != 0 and i % size == 0):
            print()
        print(layout_to_print[i], end="")
    print()


def check(layout_to_check, layout_size, check_square_size):
    i = 0
    flag = 1;
    while (i < layout_size - check_square_size + 1):
        j = layout_size * i
        while (j < layout_size * (i + 1) - check_square_size + 1):
            if (layout_to_check[j] == "X" and layout_to_check[j + check_square_size - 1] == "X"
                    and layout_to_check[j + (layout_size * (check_square_size - 1))] == "X"
                    and layout_to_check[j + (layout_size * (check_square_size - 1)) + check_square_size - 1] == "X"):
                flag = 0
                break
            j = j + 1
        if (flag == 0):
            break
        i = i + 1

    return flag


# main
while (True):
    layout_made = layout_maker(size_of_layout)
    flag = 1
    for i in range(2, size_of_layout + 1):
        if (check(layout_made, size_of_layout, i) == 0):
            flag = 0
            break
    if (flag == 0):
        continue
    else:
        layout_printer(layout_made, size_of_layout)
        break