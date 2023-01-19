#!/usr/bin/python3
for x in range(100):
<<<<<<< HEAD
    print("{:02},".format(x), end=" ")
print("\n")
=======
    if x == 99:
        print("{:02}".format(x))
    else:
        print("{:02}".format(x), end=", ")
>>>>>>> dea4590fe622811ead1570a008ef18439bb04ebb
