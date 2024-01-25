#!/usr/bin/python3
for first_number in range(0, 8):
    for second_number in range(first_number, 10):
        if first_number != second_number:
            print("{}{}".format(first_number, second_number), end=", ")
print(89)
