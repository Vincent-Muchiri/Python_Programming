from tkinter import messagebox
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        messagebox.showerror(title="Index error", message="Index doesn't exist")
        print("Fruit pie")
    else:
        print(fruit + " pie")

make_pie(4)
