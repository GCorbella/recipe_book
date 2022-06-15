from pathlib import Path, PureWindowsPath
import os
rute = Path(Path.home(),"Recetas")
working = True

def welcome():
    n_recipes = 0
    for txt in Path(rute).glob("**/*.txt"):
        n_recipes += 1
    print("Welcome to the Python Recipe Book!")
    print("The Python Recipe Book is in: " + str(rute))
    print(f"There are {n_recipes} recipes.")
    print("1 - Read Recipe\n2 - New Recipe\n3 - New category\n4 - Remove Recipe\n5 - Remove Category\n6 - Close Python Recipe Book")
    chosed = input("What do you want to do? ")
    if int(chosed) not in range(1,7):
        print("Enter a valid option, please.")
        chosed = input("What do you want to do? ")
    return int(chosed)

def r_recipe():
    for folder in Path(rute).glob():
        print(folder)
    where = input("From what category? ")
def n_recipe():

def n_category():
    nc_name = input("What is the name of the new category? ")
    nc_rute = PureWindowsPath(Path(rute, nc_name))
    n_category = os.makedirs(nc_rute)
    print("Category created!")

def x_recipe():

def x_category():
    xc_name = input("What is the name of the category you want to remove? ")
    xc_rute = PureWindowsPath(Path(rute, xc_name))
    x_category = os.rmdir(xc_rute)
    print("Category removed!")

def shut_down():
    print("Thank you for using Python Recipe Book!")
    working = False

while working is True:
    #system(cls)
    welcome()
    if welcome() == 1:
        r_recipe()

    elif welcome() == 2:
        n_recipe()

    elif welcome() == 3:
        n_category()

    elif welcome() == 4:
        x_recipe()

    elif welcome() == 5:
        x_category()

    else:
        shut_down()

