rows = 1
while rows <= 4:
    spaces = 4 - rows
    stars = 2 * rows - 1

    # print spaces
    s = 0
    while s < spaces:
        print(" ", end="")
        s += 1

    # print stars
    st = 0
    while st < stars:
        print("*", end="")
        st += 1

    print()  # new line
    rows += 1
