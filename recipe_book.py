import shutil
from pathlib import Path, PureWindowsPath
import os
from os import system
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
    print("-" * 50)
    chosed = input("What do you want to do? ")
    if int(chosed) not in range(1,7):
        print("Enter a valid option, please.")
        chosed = input("What do you want to do? ")
    print("*" * 50)
    return int(chosed)

def r_recipe():
    root, dirs, files = os.walk(rute).__next__()
    print(dirs)
    print("-" * 50)
    where = input("From what category? ")
    print("*" * 50)
    for txt in Path(rute, where).glob("**/*.txt"):
        print(str(txt.name))
    print("-" * 50)
    recipe = input("What recipe? ") + ".txt"
    print("*" * 50)
    print(Path(rute, where, recipe).read_text())
    input("Press enter to continue")

def n_recipe():
    root, dirs, files = os.walk(rute).__next__()
    print(dirs)
    print("-" * 50)
    where = input("From what category? ")
    print("*" * 50)
    name_recipe = input("What's the name of the recipe? ") + ".txt"
    print("*" * 50)
    n_recipe = open(Path(rute, where, name_recipe),"w")
    text_recipe = input("What's the content of the recipe? ")
    print("*" * 50)
    n_recipe.write(text_recipe)
    n_recipe.close()
    input("Press enter to continue")

def n_category():
    nc_name = input("What is the name of the new category? ")
    nc_rute = PureWindowsPath(Path(rute, nc_name))
    n_category = os.makedirs(nc_rute)
    print("*" * 50)
    print("Category created!")
    input("Press enter to continue")

def x_recipe():
    root, dirs, files = os.walk(rute).__next__()
    print(dirs)
    print("-" * 50)
    where = input("From what category? ")
    print("*"*50)
    for txt in Path(rute, where).glob("**/*.txt"):
        print(str(txt.name))
    print("-" * 50)
    recipe = input("What recipe? ") + ".txt"
    print("*" * 50)
    x_recipe = os.remove(Path(rute, where, recipe))
    print("Recipe removed!")
    input("Press enter to continue")

def x_category():
    root, dirs, files = os.walk(rute).__next__()
    print(dirs)
    print("-" * 50)
    xc_name = input("What is the name of the category you want to remove? ")
    xc_rute = PureWindowsPath(Path(rute, xc_name))
    x_category = shutil.rmtree(xc_rute)
    print("*" * 50)
    print("Category removed!")
    input("Press enter to continue")

def shut_down():
    print("Thank you for using Python Recipe Book!")
    return False

while working is True:
    system("cls")
    chosed = welcome()
    if chosed == 1:
        r_recipe()

    elif chosed == 2:
        n_recipe()

    elif chosed == 3:
        n_category()

    elif chosed == 4:
        x_recipe()

    elif chosed == 5:
        x_category()

    else:
        working = shut_down()

