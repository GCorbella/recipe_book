from pathlib import Path
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
    chosed = input("What do you want to do? ")
    if int(chosed) not in range(1,7):
        print("Enter a valid option, please.")
        chosed = input("What do you want to do? ")
    return int(chosed)

def r_recipe():

def n_recipe():

def n_category():

def x_recipe():

def x_category():

def shut_down():
    print("Thank you for using Python Recipe Book!")
    working = False

while working is True:
    #system(cls)
    welcome()
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
        shut_down()

